#include <iostream>
using namespace std;

bool min_k(int *in, int n, int *out, int k)
{
    if (!in || !out || n < 0 || n < k) {
        return false;
    }

    if (n == k) {
        for (int i = 0; i < n; ++i) {
            out[i] = in[i];
        }
        return true;
    }

    int *h = out - 1;
    int i = 0;
    for (; i < k; ++i) {
        h[i+1] = in[i];
        int j = i + 1;
        while (j > 1) {
            int p = j / 2;
            if (h[j] > h[p]) {
                int t = h[j];
                h[j] = h[p];
                h[p] = t;
            } else {
                break;
            }
            j = p;
        }
    }

    for (; i < n; ++i) {
        if (in[i] < h[1]) {
            h[1] = in[i];
            int j = 1;
            while (true) {
                int L = j * 2, R = L + 1;
                if (L <= k && h[L] >= h[R] && h[L] > h[j]) {
                    int t = h[L];
                    h[L] = h[j];
                    h[j] = t;
                    j = L;
                } else if (R <= k && h[R] >= h[L] && h[R] > h[j]) {
                    int t = h[R];
                    h[R] = h[j];
                    h[j] = t;
                    j = R;
                } else {
                    break;
                }
            }
        }
    }

    return true;
}

void test(int *in, int n, int *out, int k)
{
    if (min_k(in, n, out, k)) {
        for (int i = 0; i < k; ++i) {
            cout << out[i] << ' ';
        }
        cout << endl;
    } else {
        cout << "error\n";
    }
}

int main()
{
    int out[100];
    int a1[] = {3,2,1,9,1,2,6,4,8,10};

    test(a1, sizeof(a1)/sizeof(int), out, 3);
    test(a1, sizeof(a1)/sizeof(int), out, 5);
    test(a1, sizeof(a1)/sizeof(int), out, 1);
    test(a1, sizeof(a1)/sizeof(int), out, 0);
    test(a1, sizeof(a1)/sizeof(int), out, 10);
    test(a1, sizeof(a1)/sizeof(int), out, 20);

    return 0;
}
