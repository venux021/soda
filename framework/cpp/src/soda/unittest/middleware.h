#ifndef _SODA_UNITTEST_MIDDLEWARE_H_
#define _SODA_UNITTEST_MIDDLEWARE_H_

#include <string>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

namespace soda::unittest {

class UnitTestRequest
{
    json object;
public:
    UnitTestRequest(const std::string &text) :
        object(json::parse(text))
    {
    }

    int id() const {
        return object["id"];
    }

    bool hasAnswer() const {
        return object.contains("answer") && !object["answer"].is_null();
    }

    template <typename T>
    T getAnswer() const {
        return object["answer"].get<T>();
    }

    template <typename T>
    T arg(int index) const {
        return object["args"][index].get<T>();
    }
};

struct UnitTestResponse
{
private:
    json object;

public:
    int id {0};
    bool success {false};
    double elapse {0.0};

    template <typename T>
    void setResult(const T& res) {
        object["result"] = res;
    }

    std::string toJSONString() {
        object["id"] = id;
        object["success"] = success;
        object["elapse"] = elapse;
        return object.dump();
    }
};

} // namespace soda::unittest

#endif
