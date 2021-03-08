#ifndef _SODA_UNITTEST_JSONPARSE_H_
#define _SODA_UNITTEST_JSONPARSE_H_

#include <memory>
#include <string>
#include <type_traits>
#include <utility>

namespace soda::unittest {

class JsonValueNm;
class JsonDataNm;
using JsonValueAdapter = JsonValueNm;
using JsonDataAdapter = JsonDataNm;

template <typename T>
struct json_value_access {
    static T get(std::shared_ptr<JsonValueAdapter> v);
    static void set(std::shared_ptr<JsonValueAdapter> v, const T& t);
};

class JsonValue {

    friend class WorkOutput;
    friend bool operator==(const JsonValue& v1, const JsonValue& v2);

    std::shared_ptr<JsonValueAdapter> v;

public:
    JsonValue(std::shared_ptr<JsonValueAdapter> v);

    JsonValue();

    template <typename T>
    JsonValue(T&& t): v{emptyValue()} {
        set(std::forward<T>(t));
    }

    template <typename T>
    T get() {
        return json_value_access<std::remove_reference_t<T>>::get(v);
    }

    template <typename T>
    void set(const T& t) {
        json_value_access<std::remove_reference_t<T>>::set(v, t);
    }

    bool isNull() const;

private:
    static std::shared_ptr<JsonValueAdapter> emptyValue();
};

bool operator==(const JsonValue& v1, const JsonValue& v2);

class WorkInput {

    std::shared_ptr<JsonDataAdapter> d;

public:
    WorkInput(const std::string& jstr);

    int getId() const;

    bool hasExpected() const;

    JsonValue getExpected() const;

    JsonValue getArg(int index) const;

};

class WorkOutput {

    std::shared_ptr<JsonDataAdapter> d;

public:
    WorkOutput();
    
    void setResult(JsonValue& res);

    void setId(int id);

    void setSuccess(bool s);

    void setElapse(double e);

    std::string toJSONString() const;

};

} // namespace soda::unittest

#endif
