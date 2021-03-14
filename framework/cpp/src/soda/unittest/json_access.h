#ifndef _SODA_UNITTEST_JSON_ACCESS_H_
#define _SODA_UNITTEST_JSON_ACCESS_H_

#include "jsonlib/nmjson.h"

namespace soda::unittest {

// template <typename T>
// T json_pointer_access<T>::get(std::shared_ptr<json_ptr_t> v)
// {
//     return v->get<T>();
// }
// 
// template <typename T>
// void json_pointer_access<T>::set(std::shared_ptr<json_ptr_t> v, const T& t)
// {
//     v->set(t);
// }

template <typename T>
T json_proxy_access<T>::get(std::shared_ptr<js_obj_t> v)
{
    return v->get<T>();
}

template <typename T>
void json_proxy_access<T>::set(std::shared_ptr<js_obj_t> v, const T& t)
{
    v->set(t);
}

} // namespace soda::unittest

// #define SODA_JSON_ACCESS_TYPE(type) template class soda::unittest::json_pointer_access<type>;
#define SODA_JSON_ACCESS_TYPE(type) template class soda::unittest::json_proxy_access<type>;

#endif
