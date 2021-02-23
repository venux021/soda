#ifndef _SODA_UNITTEST_CUSTOM_NLOHMANN_H_
#define _SODA_UNITTEST_CUSTOM_NLOHMANN_H_

#include <optional>
#include <vector>

#include "nlohmann/json.hpp"

namespace nlohmann {
    template <typename T>
    struct adl_serializer<std::vector<std::optional<T>>> {
        static void to_json(json& j, const std::vector<std::optional<T>>& v) {
            j = json::array();
            for (auto& i : v) {
                if (i) {
                    j.push_back(*i);
                } else {
                    j.push_back(nullptr);
                }
            }   
        }   
        static void from_json(const json& j, std::vector<std::optional<T>>& v) {
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

#endif
