#ifndef _LEETCODE_ARRAY
#define _LEETCODE_ARRAY

#include <functional>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

#include "string.h"

namespace leetcode {

class Array {
public:
    template <typename T> static vector<T> load(istream &in);
    template <typename T> static vector<T> load(string input) {
        istringstream _sin(input);
        return load<T>(_sin);
    }

    template <typename T> static string dump(const vector<T> &arr) {
        return dump<T>(arr, [](const T &elem){ return to_string(elem); });
    }
    template <typename T> static string dump(const vector<vector<T>> &arr) {
        return dump<vector<T>>(arr, [](const vector<T> &elem){ return Array::dump<T>(elem); });
    }

    template <typename T>
    static vector<T> load(istream &in, function<T(const string &)> conv) {
        string line;
        if (getline(in, line)) {
            return load(line, conv);
        } else {
            throw "Invalid json list format";
        }
    }

    template <typename T>
    static vector<T> load(string input, function<T(const string&)> conv) {
        vector<T> output;
        String::trimLeftTrailingSpaces(input);
        String::trimRightTrailingSpaces(input);
        input = input.substr(1, input.length() - 2);
        stringstream ss;
        ss.str(input);
        string item;
        char delim = ',';
        while (getline(ss, item, delim)) {
            String::trimLeftTrailingSpaces(item);
            String::trimRightTrailingSpaces(item);
            if (item.size() == 0) {
                break;
            }
            output.push_back(conv(item));
        }
        return output;
    }

    template <typename T>
    static vector<vector<T>> load2d(istream &in) {
        string line;
        if (getline(in, line)) {
            return load2d<T>(line);
        } else {
            throw "Invalid json list format";
        }
    }

    template <typename T>
    static vector<vector<T>> load2d(const string &input) {
        vector<vector<T>> output;
        int pos = 0, end = int(input.size());
        auto skipW = [end](const string &s, int &pos) {
            while (pos < end && s[pos] == ' ') {
                ++pos;
            }
        };
        if (pos == end) {
            throw "Invalid json array format";
        }
        skipW(input, pos);
        ++pos;
        skipW(input, pos);
        if (input[pos] == ']') {
            return output;
        }
        while (true) {
            skipW(input, pos);
            int start = pos;
            while (input[pos++] != ']')
                ;;
            output.push_back(load<T>(input.substr(start, pos-start)));
            skipW(input, pos);
            if (input[pos] == ']') {
                break;
            }
            ++pos;  // skip ','
        }
        return output;
    }

    template <typename T>
    static string dump(const vector<T> &list, function<string(const T&)> conv) {
        string buffer("[");
        for (int i = 0; i < int(list.size()); ++i) {
            buffer.append(conv(list[i]));
            if (i < int(list.size()) - 1) {
                buffer.append(", ");
            }
        }
        buffer.push_back(']');
        return buffer;
    }
};

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

#endif
