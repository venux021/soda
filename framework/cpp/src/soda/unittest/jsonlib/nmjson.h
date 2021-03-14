#ifndef _SODA_UNITTEST_NMJSON_H_
#define _SODA_UNITTEST_NMJSON_H_

#include <memory>
#include <string>

#include "nlohmann/json.hpp"

#include "nmjson_serial.h"

namespace soda::unittest {

namespace nmjson {

class JsonObject2 {

    using json = nlohmann::json;

    json* const ptr;

    const bool shared;

public:
    JsonObject2();

    explicit JsonObject2(const std::string& jstr);

    explicit JsonObject2(json* j);

    ~JsonObject2();

    JsonObject2(const JsonObject2& jobj);

    JsonObject2& operator=(const JsonObject2& jobj);

    bool operator==(const JsonObject2& j2) const;

    template <typename T>
    T get() const { return ptr->get<T>(); }

    template <typename T>
    void set(const T& t) {
        *ptr = t;
    }

    std::shared_ptr<JsonObject2> operator[](const std::string& key) const;

    std::shared_ptr<JsonObject2> operator[](int index) const;

    int size() const;

    static JsonObject2 array();

    bool isNull() const;

    bool contains(const std::string& key) const;

    std::string dump() const;

};

class JsonPtr {

    using json = nlohmann::json;

    friend bool operator==(const JsonPtr& r1, const JsonPtr& r2);

    json* ptr;

public:
    explicit JsonPtr(json* j);

    ~JsonPtr() = default;
    JsonPtr(const JsonPtr& p) = default;
    JsonPtr& operator=(const JsonPtr& p) = default;

    template <typename T>
    T get() const { return ptr->get<T>(); }

    template <typename T>
    void set(const T& t) {
        *ptr = t;
    }

    JsonPtr operator[](const std::string& key) const;

    JsonPtr operator[](int index) const;

    int size() const;

    bool isNull() const;

    bool hasField(const std::string& key) const;

    void updateUnderlying(JsonPtr other);

};

bool operator==(const JsonPtr& r1, const JsonPtr& r2);

class JsonObject {
    using json = nlohmann::json;
    json jobject;
public:
    JsonObject();
    explicit JsonObject(const std::string& jstr);

    ~JsonObject() = default;
    JsonObject(const JsonObject&) = default;
    JsonObject& operator=(const JsonObject&) = default;

    JsonPtr pointer();

    std::string dump() const;
};

} // namespace nmjson

} // namespace soda::unittest

#endif
