#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

int nof(int n)
{
    int number = 0;
    while (n) {
        if (n % 10 == 1) {
            ++number;
        }
        n = n / 10;
    }
    return number;
}

int numberof(int n)
{
    int num = 0;
    for (int i = 1; i <=n; ++i) {
        num += nof(i);
    }
    return num;
}

int PowerBase10(int n)
{
    int result = 1;
    for (int i = 0; i < n; ++i) {
        result *= 10;
    }
    return result;
}

int NumberOf1(const char *strN)
{
    int first = *strN - '0';
    int length = strlen(strN);
    
    if (length == 1 && first == 0) {
        return 0;
    } else if (length == 1 && first > 0) {
        return 1;
    }

    int numFirstDigit = 0;
    if (first > 1)
        numFirstDigit = PowerBase10(length -1);
    else if (first == 1)
        numFirstDigit = atoi(strN+1) + 1;

    int numOtherDigits = first * (length-1) * PowerBase10(length-2);
    int numRecursive = NumberOf1(strN + 1);

    return numFirstDigit + numOtherDigits + numRecursive;
}

int fk(int n)
{
    char strN[50];
    sprintf(strN, "%d", n);
    return NumberOf1(strN);
}

int main()
{
    cout << fk(21345) << endl;
    return 0;
}
