#include "workdata.h"

namespace soda::unittest {

bool operator==(const JsonValue& v1, const JsonValue& v2)
{
    return v1.v == v2.v || *v1.v == *v2.v;
}

} // namespace soda::unittest
