#ifndef _LEETCODE_ARRAY
#define _LEETCODE_ARRAY

#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
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
    static vector<T> load(istream &in, function<T(const string &)> conv);

    template <typename T>
    static vector<T> load(string input, function<T(const string&)> conv);

    template <typename T>
    static vector<vector<T>> load2d(istream &in);

    template <typename T>
    static vector<vector<T>> load2d(const string &input);

    template <typename T>
    static string dump(const vector<T> &list, function<string(const T&)> conv);
};

template <> vector<int> Array::load(istream &in);
template <> vector<double> Array::load(istream &in);
template <> vector<float> Array::load(istream &in);
template <> vector<char> Array::load(istream &in);
template <> vector<string> Array::load(istream &in);
template <> string Array::dump(const vector<string> &arr);
template <> string Array::dump(const vector<char> &arr);

#include "array_impl.h"

} // namespace leetcode

#endif
