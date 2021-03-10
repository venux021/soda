#include "nmjson.h"

using namespace std;

namespace soda::unittest {

namespace nmjson {

JsonPtr::JsonPtr(json* j): ptr{j} {}

JsonPtr JsonPtr::operator[](const string& key) const
{
    return JsonPtr{&(*ptr)[key]};
}

JsonPtr JsonPtr::operator[](int index) const
{
    return JsonPtr{&(*ptr)[index]};
}

int JsonPtr::size() const
{
    return ptr->size();
}

bool JsonPtr::isNull() const
{
    return !ptr || ptr->is_null();
}

bool JsonPtr::hasField(const std::string& key) const
{
    return ptr->contains(key) && !(*ptr)[key].is_null();
}

void JsonPtr::updateUnderlying(JsonPtr other)
{
    *ptr = *other.ptr;
}

bool operator==(const JsonPtr& r1, const JsonPtr& r2)
{
    return r1.ptr == r2.ptr || r1.ptr && r2.ptr && *r1.ptr == *r2.ptr;
}

JsonObject::JsonObject(): jobject{} {}

JsonObject::JsonObject(const std::string& jstr): jobject(json::parse(jstr)) {}

JsonPtr JsonObject::pointer()
{
    return JsonPtr{&jobject};
}

string JsonObject::dump() const
{
    return jobject.dump();
}

} // namespace nmjson

} // namespace soda::unittest
