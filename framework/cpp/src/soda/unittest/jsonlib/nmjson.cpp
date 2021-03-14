#include "nmjson.h"

using namespace std;

namespace soda::unittest {

namespace nmjson {

JsonObject2::JsonObject2(): ptr{new json}, shared{false} {}

JsonObject2::JsonObject2(const std::string& jstr):
    ptr{new json(json::parse(jstr))}, shared{false} {}

JsonObject2::JsonObject2(json *j): ptr{j}, shared{true} {}

JsonObject2::~JsonObject2()
{
    if (!shared) {
        delete ptr;
    }
}

JsonObject2::JsonObject2(const JsonObject2& jobj): ptr{new json(*jobj.ptr)}, shared{false} {}

JsonObject2& JsonObject2::operator=(const JsonObject2& jobj)
{
    *ptr = *jobj.ptr;
    return *this;
}

bool JsonObject2::operator==(const JsonObject2& j2) const
{
    return *ptr == *j2.ptr;
}

std::shared_ptr<JsonObject2> JsonObject2::operator[](const std::string& key) const
{
    return make_shared<JsonObject2>(&(*ptr)[key]);
}

std::shared_ptr<JsonObject2> JsonObject2::operator[](int index) const
{
    return make_shared<JsonObject2>(&(*ptr)[index]);
}

int JsonObject2::size() const
{
    return ptr->size();
}

bool JsonObject2::isNull() const
{
    return !ptr || ptr->is_null();
}

bool JsonObject2::contains(const std::string& key) const
{
    return ptr->contains(key);
}

string JsonObject2::dump() const
{
    return ptr->dump();
}

JsonObject2 JsonObject2::array()
{
    JsonObject2 obj;
    *obj.ptr = json::array();
    return obj;
}

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
