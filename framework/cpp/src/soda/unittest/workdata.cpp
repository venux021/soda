#include <optional>
#include <sstream>

#include "workdata.h"

#include "jsonlib/nmjson.h"
#include "json_access.h"  // must included after workdata.h

using namespace std;

SODA_JSON_ACCESS_TYPE(bool)
SODA_JSON_ACCESS_TYPE(short)
SODA_JSON_ACCESS_TYPE(int)
SODA_JSON_ACCESS_TYPE(long long)
SODA_JSON_ACCESS_TYPE(float)
SODA_JSON_ACCESS_TYPE(double)
SODA_JSON_ACCESS_TYPE(long double)
SODA_JSON_ACCESS_TYPE(string)
SODA_JSON_ACCESS_TYPE(vector<int>)
SODA_JSON_ACCESS_TYPE(vector<vector<int>>)
SODA_JSON_ACCESS_TYPE(vector<optional<int>>)
SODA_JSON_ACCESS_TYPE(vector<string>)
SODA_JSON_ACCESS_TYPE(vector<vector<string>>)
SODA_JSON_ACCESS_TYPE(vector<optional<string>>)

namespace soda::unittest {

JsonPointer::JsonPointer(): p{} {}

JsonPointer::JsonPointer(std::shared_ptr<json_ptr_t> p): p{p} {}

int JsonPointer::size() const
{
    return p->size();
}

bool JsonPointer::isNull() const
{
    return !p || p->isNull();
}

bool JsonPointer::hasField(const string& key) const
{
    return p->hasField(key);
}

JsonPointer JsonPointer::operator[](const std::string& key) const
{
    return JsonPointer{make_shared<json_ptr_t>((*p)[key])};
}

JsonPointer JsonPointer::operator[](int index) const
{
    return JsonPointer{make_shared<json_ptr_t>((*p)[index])};
}

void JsonPointer::updateUnderlying(JsonPointer other)
{
    p->updateUnderlying(*other.p);
}

bool operator==(const JsonPointer& p1, const JsonPointer& p2)
{
    return p1.p == p2.p || *p1.p == *p2.p;
}

JsonObject::JsonObject(): ptr{make_shared<json_obj_t>()} {}

JsonObject::JsonObject(const string& jstr): ptr{make_shared<json_obj_t>(jstr)} {}

JsonPointer JsonObject::pointer() const
{
    return JsonPointer{make_shared<json_ptr_t>(ptr->pointer())};
}

string JsonObject::dump() const
{
    return ptr->dump();
}
// JsonValue::JsonValue(shared_ptr<JsonValueAdapter> v): v{v} {}
// 
// JsonValue::JsonValue(): v{new JsonValueAdapter} {}
// 
// std::shared_ptr<JsonValueAdapter> JsonValue::emptyValue()
// {
//     return make_shared<JsonValueAdapter>();
// }
// 
// bool JsonValue::isNull() const
// {
//     return v->isNull();
// }
// 
// bool operator==(const JsonValue& v1, const JsonValue& v2)
// {
//     return v1.v == v2.v || *v1.v == *v2.v;
// }

WorkInput::WorkInput(const std::string& jstr): obj{jstr} {}

int WorkInput::getId() const
{
    // return d->query("id")->get<int>();
    return obj.pointer()["id"].get<int>();
}

bool WorkInput::hasExpected() const
{
    // return !d->query("expected")->isNull();
    return obj.pointer().hasField("expected");
}

JsonPointer WorkInput::getExpected() const 
{
    // return JsonValue{d->query("expected")};
    return obj.pointer()["expected"];
}

JsonPointer WorkInput::getArg(int index) const
{
    // std::ostringstream out;
    // out << "args[" << index << "]";
    // return JsonValue{d->query(out.str())};
    return obj.pointer()["args"][index];
}

WorkOutput::WorkOutput(): obj{} {}

void WorkOutput::setResult(JsonObject& res)
{
    root()["result"].updateUnderlying(res.pointer());
}

void WorkOutput::setId(int id)
{
//    d->setval("id", id);
    root()["id"].set(id);
}

void WorkOutput::setSuccess(bool s)
{
    // d->setval("success", s);
    root()["success"].set(s);
}

void WorkOutput::setElapse(double e)
{
    // d->setval("elapse", e);
    root()["elapse"].set(e);
}

std::string WorkOutput::toJSONString() const
{
    return obj.dump();
}

JsonPointer WorkOutput::root()
{
    return obj.pointer();
}

} // namespace soda::unittest
