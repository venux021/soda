#ifndef _SODA_UNITTEST_PARSE_H_
#define _SODA_UNITTEST_PARSE_H_

#include <type_traits>

#include "jsonproxy.h"

namespace soda::unittest {

template <typename T>
struct json_type_of {
    typedef T type;
};

template <typename T>
using json_type_of_t = typename json_type_of<T>::type;

template <typename T>
struct use_custom_serializer : public std::false_type {
};

class DataParser {
public:
    virtual ~DataParser() = default;
};

template <typename T, typename Enable = void>
class TypedDataParser : public DataParser {
public:
    virtual T parse(const JsonProxy& v) {
        return v.get<json_type_of_t<T>>();
    }
};

template <typename T>
class TypedDataParser<T, typename std::enable_if<use_custom_serializer<T>::value>::type> : public DataParser {
public:
    virtual T parse(const JsonProxy& v) {
        return T();
    }
};

template <typename From, typename To, typename Func>
class CustomDataParser : public TypedDataParser<To> {
    Func func;
public:
    CustomDataParser(Func fn): func{fn} {}

    To parse(const JsonProxy& v) override {
        return func(v.get<From>());
    }
};

class DataSerializer {
public:
    virtual ~DataSerializer() = default;
};

template <typename T, typename Enable = void>
class TypedDataSerializer : public DataSerializer {
public:
    virtual JsonProxy serialize(const T& data) {
        return JsonProxy{data};
    }
};

template <typename T>
class TypedDataSerializer<T, typename std::enable_if<use_custom_serializer<T>::value>::type> : public DataSerializer {
public:
    virtual JsonProxy serialize(const T& data) {
        return JsonProxy{};
    }
};

template <typename T, typename Func>
class CustomDataSerializer : public TypedDataSerializer<T> {
    Func func;
public:
    CustomDataSerializer(Func fn): func(fn) {}

    JsonProxy serialize(const T& data) override {
        return JsonProxy{func(data)};
    }
};

} // soda::unittest

#define USE_CUSTOM_SERIAL(type) \
    namespace soda::unittest { \
        template<> struct use_custom_serializer<type> : public std::true_type {}; \
    }

#endif
