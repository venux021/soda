#ifndef _SODA_UNITTEST_JSON_ACCESS_H_
#define _SODA_UNITTEST_JSON_ACCESS_H_

#include "jsonlib/lib_nlohmann.h"

namespace soda::unittest {

template <typename T>
T json_value_access<T>::get(std::shared_ptr<JsonValueAdapter> v)
{
    return v->get<T>();
}

template <typename T>
void json_value_access<T>::set(std::shared_ptr<JsonValueAdapter> v, const T& t)
{
    v->set(t);
}

} // namespace soda::unittest

#define SODA_JSON_ACCESS_TYPE(type) template class soda::unittest::json_value_access<type>;

#endif
