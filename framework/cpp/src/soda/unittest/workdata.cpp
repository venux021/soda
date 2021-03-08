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

JsonValue::JsonValue(shared_ptr<JsonValueAdapter> v): v{v} {}

JsonValue::JsonValue(): v{new JsonValueAdapter} {}

std::shared_ptr<JsonValueAdapter> JsonValue::emptyValue()
{
    return make_shared<JsonValueAdapter>();
}

bool JsonValue::isNull() const
{
    return v->isNull();
}

bool operator==(const JsonValue& v1, const JsonValue& v2)
{
    return v1.v == v2.v || *v1.v == *v2.v;
}

WorkInput::WorkInput(const std::string& jstr): d{std::make_shared<JsonDataAdapter>(jstr)} {}

int WorkInput::getId() const
{
    return d->query("id")->get<int>();
}

bool WorkInput::hasExpected() const
{
    return !d->query("expected")->isNull();
}

JsonValue WorkInput::getExpected() const 
{
    return JsonValue{d->query("expected")};
}

JsonValue WorkInput::getArg(int index) const
{
    std::ostringstream out;
    out << "args[" << index << "]";
    return JsonValue{d->query(out.str())};
}

WorkOutput::WorkOutput(): d{std::make_shared<JsonDataAdapter>()} {}

void WorkOutput::setResult(JsonValue& res)
{
    d->set("result", *res.v);
}

void WorkOutput::setId(int id)
{
    d->setval("id", id);
}

void WorkOutput::setSuccess(bool s)
{
    d->setval("success", s);
}

void WorkOutput::setElapse(double e)
{
    d->setval("elapse", e);
}

std::string WorkOutput::toJSONString() const
{
    return d->dump();
}

} // namespace soda::unittest
