#ifndef _SODA_UNITTEST_JSONPROXY_H_
#define _SODA_UNITTEST_JSONPROXY_H_

#include <memory>
#include <string>
#include <type_traits>
#include <utility>

namespace soda::unittest {

namespace nmjson {
    class JsonObject2;
}

using js_obj_t = nmjson::JsonObject2;

template <typename T>
struct json_proxy_access {
    static T get(std::shared_ptr<js_obj_t> v);
    static void set(std::shared_ptr<js_obj_t> v, const T& t);
};

class JsonProxy {

    std::shared_ptr<js_obj_t> obj;

public:
    JsonProxy();

    explicit JsonProxy(const std::string& jstr);

    JsonProxy(std::shared_ptr<js_obj_t> p);

    JsonProxy(const JsonProxy& jp);

    template <typename T>
    explicit JsonProxy(const T& t): JsonProxy() {
        set(t);
    }

    JsonProxy& operator=(const JsonProxy& jp);

    bool operator==(const JsonProxy& jp) const;

    template <typename T>
    T get() const {
        return json_proxy_access<std::remove_reference_t<T>>::get(obj);
    }

    template <typename T>
    void set(const T& t) {
        json_proxy_access<std::remove_reference_t<T>>::set(obj, t);
    }

    template <typename T>
    JsonProxy& operator=(const T& t) {
        set(t);
        return *this;
    }

    int size() const;

    bool isNull() const;

    bool contains(const std::string& key) const;

    JsonProxy operator[](const std::string& key) const;

    JsonProxy operator[](int index) const;

    std::string dump() const;

};

} // namespace soda::unittest

#endif
