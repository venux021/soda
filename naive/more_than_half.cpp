#include <iostream>
#include <vector>
using namespace std;

bool find_more_than_half(vector<int> &v, int *result);

void test(vector<int> &v)
{
    int result = 0;
    if (find_more_than_half(v, &result)) {
        cout << "got it: " << result << endl;
    } else {
        cout << "not found" << endl;
    }
}

int main()
{
    vector<int> v1{1,2,3,4,5,4,3,2,2,2,3,2,4,2,2,2,2},
        v2{1,2,2,1},
        v3{1,2,1,3,1},
        v4{1},
        v5{},
        v6{0,5,0},
        v7{5,0};
    test(v1);
    test(v2);
    test(v3);
    test(v4);
    test(v5);
    test(v6);
    test(v7);
    return 0;
}

int partition(vector<int> &v, int start, int end)
{
    int k = v[start];
    int i = start;
    while (i < end && v[i] < k) {
        ++i;
    }

    for (int j = i + 1; j < end; ++j) {
        if (v[j] < k) {
            if (i != j) {
                int temp = v[j];
                v[j] = v[i];
                v[i] = temp;
            }
            ++i;
        }
    }

    return i;
}

bool find_more_than_half(vector<int> &v, int *result)
{
    int N = static_cast<int>(v.size());
    int mid = (N-1)/2;

    if (N== 0) {
        return false;
    } else if (N == 1) {
        *result = v[0];
        return true;
    }

    int b = 0, e = N;
    int i = partition(v, b, e);
    while (i != mid) {
        if (i < mid) {
            b = i + 1;
        } else {
            e = i;
        }
        i = partition(v, b, e);
    }
    *result = v[mid];
    return true;
}
