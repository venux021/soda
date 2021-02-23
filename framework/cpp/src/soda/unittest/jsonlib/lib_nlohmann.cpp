#include "lib_nlohmann.h"

namespace soda::unittest {

bool operator==(const JsonValueNm& v1, const JsonValueNm& v2)
{
    return v1.ptr == v2.ptr || *v1.ptr == *v2.ptr;
}

} // namespace soda::unittest
