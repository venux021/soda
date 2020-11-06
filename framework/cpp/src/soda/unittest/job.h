#ifndef _SODA_UNITTEST_JOB_H_
#define _SODA_UNITTEST_JOB_H_

#include <chrono>
#include <functional>
#include <iostream>
#include <string>
#include <tuple>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

#include "codec.h"

namespace soda::unittest {

class InputData
{
    json object;
public:
    InputData(const std::string &text) :
        object(json::parse(text))
    {
    }

    int id() const {
        return object["id"];
    }

    bool hasExpected() const {
        return object.contains("expected") && !object["expected"].is_null();
    }

    template <typename T>
    T getExpected() const {
        return object["expected"].get<T>();
    }

    template <typename T>
    T arg(int index) const {
        return object["args"][index].get<T>();
    }
};

struct OutputData
{
private:
    json resultObject;

public:
    int id {0};
    bool success {false};
    double elapse {0.0};

    template <typename T>
    void setResult(const T& res) {
        resultObject = res;
    }

    template <typename T>
    T getResult() const {
        return resultObject.get<T>();
    }

    std::string toJSONString() const {
        json object;
        object["id"] = id;
        object["success"] = success;
        object["elapse"] = elapse;
        object["result"] = resultObject;
        return object.dump();
    }
};

template <int N, typename Tuple>
struct ArgDecoder {
    static void decode(InputData& input, Tuple& tuple) {
        ArgDecoder<N-1,Tuple>::decode(input, tuple);
        using object_t = typename tuple_element<N,Tuple>::type;
        using serial_t = typename SerialTypeByObject<object_t>::type;
        auto codec = CodecFactory::create<object_t>();
        std::get<N>(tuple) = codec.decode(input.arg<serial_t>(N));
    }   
};

template <typename Tuple>
struct ArgDecoder<0, Tuple> {
    static void decode(InputData& input, Tuple& tuple) {
        using object_t = typename tuple_element<0,Tuple>::type;
        using serial_t = typename SerialTypeByObject<object_t>::type;
        auto codec = CodecFactory::create<object_t>();
        std::get<0>(tuple) = codec.decode(input.arg<serial_t>(0));
    }   
};

class JobEntry {
public:
    template <typename Class, typename Return, typename... Args>
    static void run(Return (Class::*pmFun)(Args...)) {
        using serial_t = typename SerialTypeByObject<Return>::type;
        run(pmFun, false, std::equal_to<Return>(), std::equal_to<serial_t>());
    }

    template <typename Class, typename Return, typename... Args, typename OV>
    static void runWithObjectCheck(Return (Class::*pmFun)(Args...), OV object_validator) {
        using serial_t = typename SerialTypeByObject<Return>::type;
        run(pmFun, true, object_validator, std::equal_to<serial_t>());
    }

    template <typename Class, typename Return, typename... Args, typename SV>
    static void runWithSerialCheck(Return (Class::*pmFun)(Args...), SV serial_validator) {
        run(pmFun, false, std::equal_to<Return>(), serial_validator);
    }

    template <typename Class, typename Return, typename... Args, typename OV, typename SV>
    static void run(
            Return (Class::*pmFun)(Args...),
            bool validate_by_object,
            OV object_validator,
            SV serial_validator)
    {
        std::string line, content;
        while (std::getline(std::cin, line)) {
            content += line;
        }

        InputData inputData(content);

        Class solution;

        std::tuple<typename std::remove_reference<Args>::type ...> arguments;
        decode(inputData, arguments);

        auto caller = [&](auto&&... args) {
            return (solution.*pmFun)(std::forward<decltype(args)>(args)...);
        };

        using namespace std::chrono;
        auto startMicro = chrono::steady_clock::now();
        Return res = std::apply(caller, arguments);
        auto endMicro = chrono::steady_clock::now();
        auto elapseMicro = chrono::duration_cast<chrono::microseconds>(endMicro - startMicro).count();

        auto elapseMillis = elapseMicro / 1000.0;
        auto serial_res = CodecFactory::create<Return>().encode(res);

        OutputData outputData;
        outputData.id = inputData.id();
        outputData.setResult(serial_res);
        outputData.elapse = elapseMillis;

        bool success = true;
        if (inputData.hasExpected()) {
            using ex_type = typename SerialTypeByObject<Return>::type;
            auto serial_expc = inputData.getExpected<ex_type>();
            if (validate_by_object) {
                Return expc = CodecFactory::create<Return>().decode(serial_expc);
                success = object_validator(expc, res);
            } else {
                success = serial_validator(serial_expc, serial_res);
            }
        }
        outputData.success = success;

        std::cout << outputData.toJSONString();
    }

private:
    template <typename Tuple>
    static void decode(InputData& input, Tuple& tuple) {
        ArgDecoder<tuple_size<Tuple>::value-1,Tuple>::decode(input, tuple);
    }
};

} // namespace soda::unittest

#endif
