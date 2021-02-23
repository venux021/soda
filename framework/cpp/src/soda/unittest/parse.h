#ifndef _SODA_UNITTEST_PARSE_H_
#define _SODA_UNITTEST_PARSE_H_

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

class DataParser {
public:
    virtual ~DataParser() = default;
};

template <typename T>
class TypedDataParser : public DataParser {
public:
    virtual T parse(JsonValue v) {
        return v.get<json_type_of_t<T>>();
    }
};

template <typename From, typename To, typename Func>
class CustomDataParser : public TypedDataParser<To> {
    Func func;
public:
    CustomDataParser(Func fn): func{fn} {}

    To parse(JsonValue v) override {
        return func(v.get<From>());
    }
};

class DataSerializer {
public:
    virtual ~DataSerializer() = default;
};

template <typename T>
class TypedDataSerializer : public DataSerializer {
public:
    virtual JsonValue serialize(const T& data) {
        return JsonValue{data};
    }
};

template <typename T, typename Func>
class CustomDataSerializer : public TypedDataSerializer<T> {
    Func func;
public:
    CustomDataSerializer(Func fn): func(fn) {}

    JsonValue serialize(const T& data) override {
        return JsonValue{func(data)};
    }
};


template <>
class TypedDataParser<TreeNode*> : public DataParser {
public:
    virtual TreeNode* parse(JsonValue v) {
        return BiTree::create(v.get<std::vector<std::optional<int>>>());
    }
};

template <>
class TypedDataSerializer<TreeNode*> : public DataSerializer {
public:
    virtual JsonValue serialize(TreeNode* root) {
        return JsonValue{BiTree::inLevelOrder(root)};
    }
};

template <>
class TypedDataParser<ListNode*> : public DataParser {
public:
    virtual ListNode* parse(JsonValue v) {
        return ListHelper::create(v.get<std::vector<int>>());
    }
};

template <>
class TypedDataSerializer<ListNode*> : public DataSerializer {
public:
    virtual JsonValue serialize(ListNode* head) {
        return JsonValue{ListHelper::dump(head)};
    }
};

template <>
class TypedDataParser<char> : public DataParser {
public:
    virtual char parse(JsonValue v) {
        return v.get<std::string>()[0];
    }
};

template <>
class TypedDataSerializer<char> : public DataSerializer {
public:
    virtual JsonValue serialize(char ch) {
        return JsonValue{std::string(1, ch)};
    }
};

} // soda::unittest

#endif
