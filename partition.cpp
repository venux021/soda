#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

void print(const vector<int> &v)
{
    cout << '(';
    for (auto i : v) {
        cout << i << ' ';
    }
    cout << ')';
}

vector<int>::size_type partition(vector<int> &v);

void test(vector<int> &v)
{
    print(v);
    cout << "k = " << "|  ";
    auto p = partition(v);
    print(v);
    cout << ": " << p << endl;
}

int main()
{
    vector<int> v1{},
        v2{1},
        v3{8,7,4,6,9},
        v4{5,2},
        v5{10,9,6},
        v6{0,0,0,1,1,1,0,0,0,1,1,1},
        v7{1,1,1,1,1,1,1,1},
        v8{8,7,6,5,4,3,2,1},
        v9{5,7,6,5,4,3,2,1},
        v10{4,2,3,4,5,6,7,8};

    test(v1);
    test(v2);
    test(v3);
    test(v4);
    test(v5);
    test(v6);
    test(v7);
    test(v8);
    test(v9);
    test(v10);
}

vector<int>::size_type partition(vector<int> &v)
{
    auto first = v.begin(), last = v.end();
    if (first == last) {
        return 0;
    }

    int k = *first;

    for (auto i = std::next(first); i != last; ++i) {
        if (*i < k) {
            std::iter_swap(i, first);
            ++first;
        }
    }

    return std::distance(v.begin(), first);
}

/*
vector<int>::size_type partition(vector<int> &v)
{
    if (v.size() == 0 || v.size() == 1) {
        return 0;
    }

    auto e = v.size() - 1;
    swap(v[0], v[e]);

    vector<int>::size_type i = 0, j = 0;
    do {
        if (v[j] <= v[e]) {
            if (j != i) {
                swap(v[i], v[j]);
            }
            ++i;
        }
        ++j;
    } while (j < e);
    swap(v[e], v[i]);
    return i;
}
*/

/*
vector<int>::size_type partition(vector<int> &v)
{
    if (v.size() == 0) {
        return 0;
    }

    vector<int>::size_type i = 0, j = v.size();
    int k = v[0];

    while (i < j) {
        --j;
        while (i < j && v[j] > k) {
            --j;
        }
        if (i < j) {
            v[i] = v[j];
        } else {
            break;
        }

        ++i;
        while (i < j && v[i] < k) {
            ++i;
        }
        if (i < j) {
            v[j] = v[i];
        } else {
            break;
        }
    }
    v[i] = k;
    return i;
}
*/

