#ifndef _LEETCODE_UTILS
#define _LEETCODE_UTILS

#include <vector>
#include <iostream>
#include <string>
using namespace std;

class Leetcode {
public:

    void trimLeftTrailingSpaces(string &input) {
        input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
            return !isspace(ch);
        }));
    }
    
    void trimRightTrailingSpaces(string &input) {
        input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
            return !isspace(ch);
        }).base(), input.end());
    }
    
    vector<int> stringToIntegerVector(const string &input) {
        vector<int> output;
        trimLeftTrailingSpaces(input);
        trimRightTrailingSpaces(input);
        input = input.substr(1, input.length() - 2);
        stringstream ss;
        ss.str(input);
        string item;
        char delim = ',';
        while (getline(ss, item, delim)) {
            output.push_back(stoi(item));
        }
        return output;
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
