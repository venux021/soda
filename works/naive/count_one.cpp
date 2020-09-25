#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;

void top_digit(int n, int *a, int *k, int *remain)
{
    int m = n;
    *k = 1;
    while (m >= 10) {
        m /= 10;
        ++*k;
    }
    
    *remain = n - pow(10, *k-1) * m;
    *a = m;
}

int count_one(int n)
{
    if (n < 10) {
        return n > 0;
    }

    int a, k, remain;
    top_digit(n, &a, &k, &remain);
//    cout << n << ": " << a << ',' << k << ',' << remain << endl;

    int x1 = pow(10, k-2) * (k-1) * a;
    cout << n << "," << x1 << endl;

    int x2;
    if (a > 1) {
        x2 = pow(10, k - 1);
    } else {
        x2 = remain + 1;
    }

    return x1 + x2 + count_one(remain);
}

int main(int argc, char **argv)
{
    if (argc == 1) {
        cout << "usage: ./a.out <number>" << endl;
        return 1;
    }

    int n = atoi(argv[1]);
    cout << "n = " << n << endl;
    cout << count_one(n) << endl;
    return 0;
}
