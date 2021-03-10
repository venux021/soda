#ifndef _SODA_UNITTEST_PARSE_H_
#define _SODA_UNITTEST_PARSE_H_

#include <type_traits>

#include "soda/leetcode/bitree.h"
#include "soda/leetcode/list.h"

#include "workdata.h"

using namespace soda::leetcode;

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
    virtual T parse(JsonPointer v) {
        return v.get<json_type_of_t<T>>();
    }
};

template <typename T>
class TypedDataParser<T, typename std::enable_if<use_custom_serializer<T>::value>::type> : public DataParser {
public:
    virtual T parse(JsonPointer v) {
        return T();
    }
};

template <typename From, typename To, typename Func>
class CustomDataParser : public TypedDataParser<To> {
    Func func;
public:
    CustomDataParser(Func fn): func{fn} {}

    To parse(JsonPointer v) override {
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
    virtual JsonObject serialize(const T& data) {
        return JsonObject{data};
    }
};

template <typename T>
class TypedDataSerializer<T, typename std::enable_if<use_custom_serializer<T>::value>::type> : public DataSerializer {
public:
    virtual JsonObject serialize(const T& data) {
        return JsonObject{};
    }
};

template <typename T, typename Func>
class CustomDataSerializer : public TypedDataSerializer<T> {
    Func func;
public:
    CustomDataSerializer(Func fn): func(fn) {}

    JsonObject serialize(const T& data) override {
        return JsonObject{func(data)};
    }
};


template <>
class TypedDataParser<TreeNode*> : public DataParser {
public:
    virtual TreeNode* parse(JsonPointer v) {
        return BiTree::create(v.get<std::vector<std::optional<int>>>());
    }
};

template <>
class TypedDataSerializer<TreeNode*> : public DataSerializer {
public:
    virtual JsonObject serialize(TreeNode* root) {
        return JsonObject{BiTree::inLevelOrder(root)};
    }
};

template <>
class TypedDataParser<ListNode*> : public DataParser {
public:
    virtual ListNode* parse(JsonPointer v) {
        return ListHelper::create(v.get<std::vector<int>>());
    }
};

template <>
class TypedDataSerializer<ListNode*> : public DataSerializer {
public:
    virtual JsonObject serialize(ListNode* head) {
        return JsonObject{ListHelper::dump(head)};
    }
};

template <>
class TypedDataParser<char> : public DataParser {
public:
    virtual char parse(JsonPointer v) {
        return v.get<std::string>()[0];
    }
};

template <>
class TypedDataSerializer<char> : public DataSerializer {
public:
    virtual JsonObject serialize(char ch) {
        return JsonObject{std::string(1, ch)};
    }
};

} // soda::unittest

#define USE_CUSTOM_SERIAL(type) \
    namespace soda::unittest { \
        template<> struct use_custom_serializer<type> : public std::true_type {}; \
    }

#endif
