#ifndef _SODA_UNITTEST_JSON_ACCESS_H_
#define _SODA_UNITTEST_JSON_ACCESS_H_

namespace soda::unittest {

// template <typename T>
// T json_value_access<T>::get(std::shared_ptr<json_ptr_t> v)
// {
//     return v->get<T>();
// }
// 
// template <typename T>
// void json_value_access<T>::set(std::shared_ptr<json_ptr_t> v, const T& t)
// {
//     v->set(t);
// }

template <typename T>
T json_pointer_access<T>::get(std::shared_ptr<json_ptr_t> v)
{
    return v->get<T>();
}

template <typename T>
void json_pointer_access<T>::set(std::shared_ptr<json_ptr_t> v, const T& t)
{
    v->set(t);
}

} // namespace soda::unittest

// #define SODA_JSON_ACCESS_TYPE(type) template class soda::unittest::json_value_access<type>;
#define SODA_JSON_ACCESS_TYPE(type) template class soda::unittest::json_pointer_access<type>;

#endif
