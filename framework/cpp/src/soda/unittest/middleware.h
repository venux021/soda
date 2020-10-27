#ifndef _SODA_UNITTEST_MIDDLEWARE_H_
#define _SODA_UNITTEST_MIDDLEWARE_H_

#include <iostream>
#include <string>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

namespace soda::unittest {

class TestRequest
{
    json object;
public:
    TestRequest(const std::string &text) :
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

struct TestResponse
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

template <typename Result, typename ResultSerial = Result>
class JobTemplate {
public:
    using ResultType = Result;
    using ResultSerialType = ResultSerial;

    void run(const TestRequest& req, TestResponse& resp) {
        resp.setResult(serialize(execute(req, resp)));
    }

    virtual ResultType execute(const TestRequest& req, TestResponse& resp) = 0;

    virtual ResultSerialType serialize(const ResultType& res) = 0;

    virtual bool validate(const TestRequest& req, const TestResponse& resp) = 0;

};

class Runner {
public:
    template <typename R, typename RS>
    void run(JobTemplate<R,RS>& job) {
        std::string line, content;
        while (std::getline(std::cin, line)) {
            content += line;
        }

        TestRequest req(content);
        TestResponse resp;
        resp.id = req.id();

        auto startMicro = std::chrono::steady_clock::now();
        job.run(req, resp);
        auto endMicro = std::chrono::steady_clock::now();
        auto elapseMicro = std::chrono::duration_cast<std::chrono::microseconds>(endMicro - startMicro).count();

        resp.elapse = elapseMicro / 1000.0;

        if (req.hasExpected()) {
            resp.success = job.validate(req, resp);
        } else {
            resp.success = true;
        }

        std::cout << resp.toJSONString();
    }
};

} // namespace soda::unittest

#endif
