#ifndef _SODA_UNITTEST_LIB_NLOHMANN_H_
#define _SODA_UNITTEST_LIB_NLOHMANN_H_

#include <memory>
#include <string>

#include "nlohmann/json.hpp"

#include "custom_nlohmann.h"

namespace soda::unittest {

class JsonValueNm {

    using json = nlohmann::json;

    friend class JsonDataNm;
    friend bool operator==(const JsonValueNm& v1, const JsonValueNm& v2);

    json* ptr;

    bool shared;

public:
    JsonValueNm(json* j): ptr{j}, shared{true} {}

    JsonValueNm(): ptr{new json}, shared{false} {}

    ~JsonValueNm() { if (!shared) delete ptr; }

    template <typename T>
    T get() const { return ptr->get<T>(); }

    template <typename T>
    void set(const T& t) {
        *ptr = t;
    }

    bool isNull() const { return ptr->is_null(); }
};

bool operator==(const JsonValueNm& v1, const JsonValueNm& v2);

class JsonDataNm {

    using json = nlohmann::json;

    json jobject;

public:
    JsonDataNm(const std::string& str):
        jobject(json::parse(str))
    {}

    JsonDataNm(): jobject{} {}

    std::shared_ptr<JsonValueNm> query(const std::string& str) const {
        if (str.length() == 0) {
            return std::shared_ptr<JsonValueNm>();
        }

        if (str[str.length()-1] == ']') {
            auto idx = str.find("[");
            auto key = str.substr(0, idx);
            int index = stoi(str.substr(idx+1, str.length()-idx-2));
            return std::make_shared<JsonValueNm>(const_cast<json*>(&jobject[key][index]));
        } else {
            return jobject.contains(str) 
                ? std::make_shared<JsonValueNm>(const_cast<json*>(&jobject[str]))
                : std::make_shared<JsonValueNm>();
        }
    }

    void set(const std::string& key, JsonValueNm& v) {
        jobject[key] = *v.ptr;
    }

    template <typename T>
    void setval(const std::string& key, const T& t) {
        jobject[key] = t;
    }

    std::string dump() const {
        return jobject.dump();
    }
};

} // namespace soda::unittest

#endif
