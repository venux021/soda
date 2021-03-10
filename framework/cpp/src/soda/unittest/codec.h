#ifndef _SODA_UNITTEST_CODEC_H_
#define _SODA_UNITTEST_CODEC_H_

#include <optional>
#include <string>
#include <vector>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

#include "soda/leetcode/bitree.h"
#include "soda/leetcode/list.h"
#include "soda/unittest/jsonlib/nmjson_serial.h"

using namespace soda::leetcode;

namespace soda::unittest {

template <typename Object>
class CommonCodec {
public:
    using serial_t = Object;
    serial_t encode(const Object& obj) const {
        return obj;
    }
    Object decode(const serial_t& serial) const {
        return serial;
    }
};

template <typename Object>
struct SerialTypeByObject {
    using type = typename CommonCodec<Object>::serial_t;
};

template <>
class CommonCodec<TreeNode*> {
public:
    using serial_t = vector<optional<int>>;
    serial_t encode(TreeNode* root) const {
        return BiTree::inLevelOrder(root);
    }
    TreeNode* decode(const serial_t& data) const {
        return BiTree::create(data);
    }
};

template <>
class CommonCodec<ListNode*> {
public:
    using serial_t = vector<int>;
    serial_t encode(ListNode* head) const {
        return ListHelper::dump(head);
    }
    ListNode* decode(const serial_t& data) const {
        return ListHelper::create(data);
    }
};

template <>
class CommonCodec<char> {
public:
    using serial_t = std::string;
    serial_t encode(char ch) const {
        return std::string(1, ch);
    }
    char decode(const std::string& str) const {
        return str[0];
    }
};

class CodecFactory {
public:
    template <typename Object>
    static CommonCodec<Object> create() {
        return CommonCodec<Object>();
    }
};

} // namespace soda::unittest

#endif
