#include <optional>
#include <sstream>

#include "workdata.h"
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

// JsonPointer::JsonPointer(): p{} {}
// 
// JsonPointer::JsonPointer(std::shared_ptr<json_ptr_t> p): p{p} {}
// 
// int JsonPointer::size() const
// {
//     return p->size();
// }
// 
// bool JsonPointer::isNull() const
// {
//     return !p || p->isNull();
// }
// 
// bool JsonPointer::hasField(const string& key) const
// {
//     return p->hasField(key);
// }
// 
// JsonPointer JsonPointer::operator[](const std::string& key) const
// {
//     return JsonPointer{make_shared<json_ptr_t>((*p)[key])};
// }
// 
// JsonPointer JsonPointer::operator[](int index) const
// {
//     return JsonPointer{make_shared<json_ptr_t>((*p)[index])};
// }
// 
// void JsonPointer::updateUnderlying(JsonPointer other)
// {
//     p->updateUnderlying(*other.p);
// }
// 
// bool operator==(const JsonPointer& p1, const JsonPointer& p2)
// {
//     return p1.p == p2.p || *p1.p == *p2.p;
// }
// 
// JsonObject::JsonObject(): ptr{make_shared<json_obj_t>()} {}
// 
// JsonObject::JsonObject(const string& jstr): ptr{make_shared<json_obj_t>(jstr)} {}
// 
// JsonPointer JsonObject::pointer() const
// {
//     return JsonPointer{make_shared<json_ptr_t>(ptr->pointer())};
// }
// 
// string JsonObject::dump() const
// {
//     return ptr->dump();
// }

// WorkInput::WorkInput(const std::string& jstr): obj{jstr} {}
// 
// int WorkInput::getId() const
// {
//     return obj.pointer()["id"].get<int>();
// }
// 
// bool WorkInput::hasExpected() const
// {
//     return obj.pointer().hasField("expected");
// }
// 
// JsonPointer WorkInput::getExpected() const 
// {
//     return obj.pointer()["expected"];
// }
// 
// JsonPointer WorkInput::getArg(int index) const
// {
//     return obj.pointer()["args"][index];
// }

WorkInput::WorkInput(const std::string& jstr): proxy{jstr} {}

int WorkInput::getId() const
{
    return proxy["id"].get<int>();
}

bool WorkInput::hasExpected() const
{
    return proxy.contains("expected") && !proxy["expected"].isNull();
}

JsonProxy WorkInput::getExpected() const 
{
    return proxy["expected"];
}

JsonProxy WorkInput::getArg(int index) const
{
    return proxy["args"][index];
}

// WorkOutput::WorkOutput(): obj{} {}
// 
// void WorkOutput::setResult(JsonObject& res)
// {
//     root()["result"].updateUnderlying(res.pointer());
// }
// 
// void WorkOutput::setId(int id)
// {
//     root()["id"].set(id);
// }
// 
// void WorkOutput::setSuccess(bool s)
// {
//     root()["success"].set(s);
// }
// 
// void WorkOutput::setElapse(double e)
// {
//     root()["elapse"].set(e);
// }
// 
// std::string WorkOutput::toJSONString() const
// {
//     return obj.dump();
// }
// 
// JsonPointer WorkOutput::root()
// {
//     return obj.pointer();
// }

WorkOutput::WorkOutput(): proxy{} {}

void WorkOutput::setResult(const JsonProxy& res)
{
    proxy["result"] = res;
}

void WorkOutput::setId(int id)
{
    proxy["id"] = id;
}

void WorkOutput::setSuccess(bool s)
{
    proxy["success"] = s;
}

void WorkOutput::setElapse(double e)
{
    proxy["elapse"] = e;
}

std::string WorkOutput::toJSONString() const
{
    return proxy.dump();
}

} // namespace soda::unittest
