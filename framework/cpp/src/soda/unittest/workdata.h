#ifndef _SODA_UNITTEST_JSONPARSE_H_
#define _SODA_UNITTEST_JSONPARSE_H_

#include <memory>
#include <string>
#include <type_traits>
#include <utility>

namespace soda::unittest {

namespace nmjson {
    class JsonPtr;
    class JsonObject;
}

using json_ptr_t = nmjson::JsonPtr;
using json_obj_t = nmjson::JsonObject;

template <typename T>
struct json_pointer_access {
    static T get(std::shared_ptr<json_ptr_t> v);
    static void set(std::shared_ptr<json_ptr_t> v, const T& t);
};

class JsonPointer {
    friend bool operator==(const JsonPointer& p1, const JsonPointer& p2);
    std::shared_ptr<json_ptr_t> p;
public:
    JsonPointer();

    JsonPointer(std::shared_ptr<json_ptr_t> p);

    template <typename T>
    T get() const {
        return json_pointer_access<std::remove_reference_t<T>>::get(p);
    }

    template <typename T>
    void set(const T& t) {
        json_pointer_access<std::remove_reference_t<T>>::set(p, t);
    }

    int size() const;

    bool isNull() const;

    bool hasField(const std::string& key) const;

    JsonPointer operator[](const std::string& key) const;

    JsonPointer operator[](int index) const;

    void updateUnderlying(JsonPointer other);
};

bool operator==(const JsonPointer& p1, const JsonPointer& p2);

class JsonObject {

    std::shared_ptr<json_obj_t> ptr;

public:
    JsonObject();

    JsonObject(const std::string& jstr);

    template <typename T>
    JsonObject(const T& t): JsonObject() {
        pointer().set(t);
    }

    JsonPointer pointer() const;

    std::string dump() const;

};

// class JsonValueNm;
// class JsonDataNm;
// using JsonValueAdapter = JsonValueNm;
// using JsonDataAdapter = JsonDataNm;
// 
// template <typename T>
// struct json_value_access {
//     static T get(std::shared_ptr<JsonValueAdapter> v);
//     static void set(std::shared_ptr<JsonValueAdapter> v, const T& t);
// };
// 
// class JsonValue {
// 
//     friend class WorkOutput;
//     friend bool operator==(const JsonValue& v1, const JsonValue& v2);
// 
//     std::shared_ptr<JsonValueAdapter> v;
// 
// public:
//     JsonValue(std::shared_ptr<JsonValueAdapter> v);
// 
//     JsonValue();
// 
//     template <typename T>
//     JsonValue(T&& t): v{emptyValue()} {
//         set(std::forward<T>(t));
//     }
// 
//     template <typename T>
//     T get() {
//         return json_value_access<std::remove_reference_t<T>>::get(v);
//     }
// 
//     template <typename T>
//     void set(const T& t) {
//         json_value_access<std::remove_reference_t<T>>::set(v, t);
//     }
// 
//     bool isNull() const;
// 
// private:
//     static std::shared_ptr<JsonValueAdapter> emptyValue();
// };
// 
// bool operator==(const JsonValue& v1, const JsonValue& v2);

// class WorkInput {
// 
//     std::shared_ptr<JsonDataAdapter> d;
// 
// public:
//     WorkInput(const std::string& jstr);
// 
//     int getId() const;
// 
//     bool hasExpected() const;
// 
//     JsonValue getExpected() const;
// 
//     JsonValue getArg(int index) const;
// 
// };
// 
// class WorkOutput {
// 
//     std::shared_ptr<JsonDataAdapter> d;
// 
// public:
//     WorkOutput();
//     
//     void setResult(JsonValue& res);
// 
//     void setId(int id);
// 
//     void setSuccess(bool s);
// 
//     void setElapse(double e);
// 
//     std::string toJSONString() const;
// 
// };

class WorkInput {

    JsonObject obj;

public:
    WorkInput(const std::string& jstr);

    int getId() const;

    bool hasExpected() const;

    JsonPointer getExpected() const;

    JsonPointer getArg(int index) const;

};

class WorkOutput {

    JsonObject obj;

public:
    WorkOutput();
    
    void setResult(JsonObject& res);
    // template <typename T>
    // JsonPointer setResult(const T& t) {
    //     auto p = resultField();
    //     p.set(t);
    //     return p;
    // }

    void setId(int id);

    void setSuccess(bool s);

    void setElapse(double e);

    std::string toJSONString() const;

private:
    JsonPointer root();
};

} // namespace soda::unittest

#endif
