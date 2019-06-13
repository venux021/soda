#ifndef _LEETCODE_UTILS
#define _LEETCODE_UTILS

#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

#include "array.h"
#include "string.h"
using namespace leetcode;

class Leetcode {
public:

    static int readInt(ifstream &in) {
        string line;
        getline(in, line);
        return stoi(trim(line));
    }

    static vector<int> readIntArray(ifstream &in) {
        return Array::loadIntArray(in);
    }

    static string trim(const string &str) {
        return String::trim(str);
    }

    static void trimLeftTrailingSpaces(string &input) {
        String::trimLeftTrailingSpaces(input);
    }
    
    static void trimRightTrailingSpaces(string &input) {
        String::trimRightTrailingSpaces(input);
    }
    
    static vector<int> stringToIntegerVector(string &input) {
        return Array::loadIntArray(input);
    }

    template <typename T>
    static void print(const vector<T> &vec) {
        print1d(vec);
        cout << '\n';
    }

    template <typename T>
    static void print(const vector<vector<T>> &vec2d) {
        if (vec2d.size() == 0) {
            cout << "[]\n";
            return;
        }
        cout << "[\n";
        for (int i = 0; i < int(vec2d.size()) - 1; ++i) {
            cout << "  ";
            print1d(vec2d[i]);
            cout << ",\n";
        }
        cout << "  ";
        print1d(vec2d.back());
        cout << '\n';
        cout << "]\n";
    }

private:
    template <typename T>
    static void print1d(const vector<T> &vec) {
        cout << '[';
        for (int i = 0; i < int(vec.size()) - 1; ++i) {
            cout << vec[i] << ", ";
        }
        if (vec.size() > 0) {
            cout << vec.back();
        }
        cout << "]";
    }

};

#endif
