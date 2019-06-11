#ifndef _LEETCODE_UTILS
#define _LEETCODE_UTILS

#include <vector>
#include <iostream>
using namespace std;

class Leetcode {
public:

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
