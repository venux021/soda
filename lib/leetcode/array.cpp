#include "array.h"

namespace leetcode {

template <>
vector<int> Array::load(istream &in)
{
    return load<int>(in, [](const string &s){ return stoi(s); });
}

template <>
vector<double> Array::load(istream &in)
{
    return load<double>(in, [](const string &s){ return stod(s); });
}

template <>
vector<float> Array::load(istream &in)
{
    return load<float>(in, [](const string &s){ return stof(s); });
}

template <>
vector<string> Array::load(istream &in)
{
    auto conv = [](const string &s) {
        string elem = s;
        String::trimLeftTrailingSpaces(elem);
        String::trimRightTrailingSpaces(elem);
        return elem.substr(1, elem.size()-2);
    };
    return load<string>(in, conv);
}

template <>
string Array::dump(const vector<string> &arr)
{
    auto conv = [](const string &elem) {
        string buf;
        buf.push_back('"');
        buf.append(elem);
        buf.push_back('"');
        return buf;
    };
    return dump<string>(arr, conv);
}

} // namespace leetcode
