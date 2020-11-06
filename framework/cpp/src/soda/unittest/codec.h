#ifndef _SODA_UNITTEST_CODEC_H_
#define _SODA_UNITTEST_CODEC_H_

#include <optional>
#include <string>
#include <vector>

#include "nlohmann/json.hpp"
using json = nlohmann::json;

#include "soda/leetcode/bitree.h"

using namespace soda::leetcode;

namespace nlohmann {
    template <typename T>
    struct adl_serializer<vector<optional<T>>> {
        static void to_json(json& j, const vector<optional<T>>& v) {
            j = json::array();
            for (auto& i : v) {
                if (i) {
                    j.push_back(*i);
                } else {
                    j.push_back(nullptr);
                }
            }   
        }   
        static void from_json(const json& j, vector<optional<T>>& v) {
            for (auto& e : j) {
                if (!e.is_null()) {
                    v.emplace_back(e.get<T>());
                } else {
                    v.emplace_back();
                }   
            }   
        }   
    };  
}

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
    TreeNode* decode(const serial_t& data) {
        return BiTree::create(data);
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
