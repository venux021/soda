#include <iostream>
using namespace std;

int max_sum(int *arr, int n)
{
    int sum = arr[0], mx = sum;
    for (int i = 1; i < n; ++i) {
        if (sum >= 0) {
            sum += arr[i];
            if (sum > mx) {
                mx = sum;
            }
        } else {
            sum = arr[i];
        }
    }
    return mx;
}

int main()
{
    int a[] = {1,-2,3,10,-4,7,2,-5};
    cout << max_sum(a, sizeof(a)/sizeof(int)) << endl;
    return 0;
}
