#include <iostream>
#include <vector>
using namespace std;

bool find_more_than_half(const vector<int> &v, int *result);

void test(const vector<int> &v)
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

bool find_more_than_half(const vector<int> &v, int *result)
{
}
