#ifndef _SODA_UNITTEST_JSONPARSE_H_
#define _SODA_UNITTEST_JSONPARSE_H_

#include <memory>
#include <string>
#include <type_traits>
#include <utility>

#include "jsonproxy.h"

namespace soda::unittest {

// namespace nmjson {
//     class JsonPtr;
//     class JsonObject;
// }
// 
// using json_ptr_t = nmjson::JsonPtr;
// using json_obj_t = nmjson::JsonObject;
// 
// template <typename T>
// struct json_pointer_access {
//     static T get(std::shared_ptr<json_ptr_t> v);
//     static void set(std::shared_ptr<json_ptr_t> v, const T& t);
// };
// 
// class JsonPointer {
//     friend bool operator==(const JsonPointer& p1, const JsonPointer& p2);
//     std::shared_ptr<json_ptr_t> p;
// public:
//     JsonPointer();
// 
//     JsonPointer(std::shared_ptr<json_ptr_t> p);
// 
//     template <typename T>
//     T get() const {
//         return json_pointer_access<std::remove_reference_t<T>>::get(p);
//     }
// 
//     template <typename T>
//     void set(const T& t) {
//         json_pointer_access<std::remove_reference_t<T>>::set(p, t);
//     }
// 
//     int size() const;
// 
//     bool isNull() const;
// 
//     bool hasField(const std::string& key) const;
// 
//     JsonPointer operator[](const std::string& key) const;
// 
//     JsonPointer operator[](int index) const;
// 
//     void updateUnderlying(JsonPointer other);
// };
// 
// bool operator==(const JsonPointer& p1, const JsonPointer& p2);
// 
// class JsonObject {
// 
//     std::shared_ptr<json_obj_t> ptr;
// 
// public:
//     JsonObject();
// 
//     JsonObject(const std::string& jstr);
// 
//     template <typename T>
//     JsonObject(const T& t): JsonObject() {
//         pointer().set(t);
//     }
// 
//     JsonPointer pointer() const;
// 
//     std::string dump() const;
// 
// };

// class WorkInput {
// 
//     JsonObject obj;
// 
// public:
//     WorkInput(const std::string& jstr);
// 
//     int getId() const;
// 
//     bool hasExpected() const;
// 
//     JsonPointer getExpected() const;
// 
//     JsonPointer getArg(int index) const;
// 
// };
// 
// class WorkOutput {
// 
//     JsonObject obj;
// 
// public:
//     WorkOutput();
//     
//     void setResult(JsonObject& res);
// 
//     void setId(int id);
// 
//     void setSuccess(bool s);
// 
//     void setElapse(double e);
// 
//     std::string toJSONString() const;
// 
// private:
//     JsonPointer root();
// };

class WorkInput {

    JsonProxy proxy;

public:
    WorkInput(const std::string& jstr);

    int getId() const;

    bool hasExpected() const;

    JsonProxy getExpected() const;

    JsonProxy getArg(int index) const;

};

class WorkOutput {

    JsonProxy proxy;

public:
    WorkOutput();
    
    void setResult(const JsonProxy& res);

    void setId(int id);

    void setSuccess(bool s);

    void setElapse(double e);

    std::string toJSONString() const;

};

} // namespace soda::unittest

#endif
