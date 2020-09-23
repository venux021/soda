#include "array.h"

namespace soda::leetcode {

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

template <> vector<char> Array::load(istream &in)
{
    vector<string> strArr = load<string>(in);
    vector<char> chars(strArr.size());
    for (int i = 0; i < int(strArr.size()); ++i) {
        chars[i] = strArr[i][0];
    }
    return chars;
}

template <> string Array::dump(const vector<char> &arr)
{
    vector<string> strArr(arr.size());
    for (int i = 0; i < int(arr.size()); ++i) {
        strArr[i].push_back(arr[i]);
    }
    return dump(strArr);
}

} // namespace soda::leetcode
