#include <iostream>
using namespace std;

void dice_n(int n)
{
    if (n <= 0) {
        return;
    }

    int *p1 = new int[6*n+1], *p2 = new int[6*n+1];
    for (int i = 1; i <= 6; ++i) {
        p2[i] = 1;
    }

    for (int k = 2; k <= n; ++k) {
        int *tmp = p1;
        p1 = p2;
        p2 = tmp;
        int x1 = k-1, y1 = (k-1)*6;
        int x2 = k, y2 = k * 6;
        for (int i = x2; i <= y2; ++i) {
            int T = 0;
            p2[i] = 0;
            for (int j = i - 6; j < i; ++j) {
                if (j >= x1 && j <= y1) {
                    T += p1[j];
                }
            }
            p2[i] = T;
        }

//        for (int b = x2; b <= y2; ++b) {
//            cout << p2[b] << ' ';
//        }
//        cout << endl;
    }

    int Max = n*6, total = 0;
    for (int i = n; i <= Max; ++i) {
        total += p2[i];
    }

    for (int i = n; i <= Max; ++i) {
        cout << p2[i] << ", " << p2[i]/static_cast<double>(total) << endl;
    }

    delete[] p1;
    delete[] p2;
}

int main()
{
    int n;
    while (cin >> n) {
        dice_n(n);
    }
    return 0;
}
