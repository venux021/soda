#ifndef _SODA_UNITTEST_JSONPARSE_H_
#define _SODA_UNITTEST_JSONPARSE_H_

#include <memory>
#include <sstream>
#include <string>
#include <utility>

#include "jsonlib/lib_nlohmann.h"

namespace soda::unittest {

using JsonValueAdapter = JsonValueNm;
using JsonDataAdapter = JsonDataNm;

class JsonValue {

    friend class WorkOutput;
    friend bool operator==(const JsonValue& v1, const JsonValue& v2);

    std::shared_ptr<JsonValueAdapter> v;

public:
    JsonValue(std::shared_ptr<JsonValueAdapter> v): v{v} {}

    JsonValue(): v{new JsonValueAdapter} {}

    template <typename T>
    JsonValue(T&& t): v{new JsonValueAdapter} {
        set(std::forward<T>(t));
    }

    template <typename T>
    T get() { return v->get<T>(); }

    template <typename T>
    void set(const T& t) {
        v->set(t);
    }

    bool isNull() { return v->isNull(); }
};

bool operator==(const JsonValue& v1, const JsonValue& v2);

class WorkInput {

    JsonDataAdapter* d;

public:
    WorkInput(const std::string& jstr):
        d{new JsonDataAdapter(jstr)}
    {}

    int getId() {
        return d->query("id")->get<int>();
    }

    bool hasExpected() {
        return !d->query("expected")->isNull();
    }

    JsonValue getExpected() {
        return JsonValue{d->query("expected")};
    }

    JsonValue getArg(int index) {
        std::ostringstream out;
        out << "args[" << index << "]";
        return JsonValue{d->query(out.str())};
    }

};

class WorkOutput {

    JsonDataAdapter* d;

public:
    WorkOutput(): d{new JsonDataNm} {}
    
    void setResult(JsonValue& res) {
        d->set("result", *res.v);
    }

    void setId(int id) {
        d->setval("id", id);
    }

    void setSuccess(bool s) {
        d->setval("success", s);
    }

    void setElapse(double e) {
        d->setval("elapse", e);
    }

    std::string toJSONString() {
        return d->dump();
    }
};

} // namespace soda::unittest

#endif
