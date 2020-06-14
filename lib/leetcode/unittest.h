#ifndef _LEETCODE_UNITTEST
#define _LEETCODE_UNITTEST

#include <chrono>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <utility>

namespace leetcode {

void show_args();

template <typename T>
struct Serializer
{
    static std::string serialize(const T &t)
    {
        std::ostringstream out;
        out << t;
        return out.str();
    }
};

template <typename T, typename ...Args>
void show_args(const T &t, Args&&... args)
{
    std::cout << Serializer<T>::serialize(t) << std::endl;
    show_args(std::forward<Args>(args)...);
}

class Tester {

    static int testNumber;

public:
    bool showArgs {true};
    bool showResult {true};

    template <typename R, typename TFunc, typename ...Args>
    void test(const R &correct, TFunc func, Args&&... args)
    {
        auto validateFunc = [&] (const R &res) { 
            if (res != correct) {
                std::cerr << "Wrong answer " << res << ", but " << correct << " expected" << std::endl;
                return false;
            }
            return true;
        };
        validate(validateFunc, func, std::forward<Args>(args)...);
    }

    template <typename TFunc, typename ...Args>
    void test(TFunc func, Args&&... args)
    {
        validate([](auto &res){return true;}, func, std::forward<Args>(args)...);
    }

    template <typename VFunc, typename TFunc, typename ...Args>
    void validate(VFunc validate, TFunc func, Args&&... args)
    {
        execute(validate, func, std::forward<Args>(args)...);
    }

private:

    template <typename VFunc, typename TFunc, typename ...Args>
    void execute(VFunc validate, TFunc func, Args&&... args)
    {
        ++testNumber;
        std::cout << "**[" << testNumber << "]**\n";

        if (showArgs) {
            std::cout << "input:" << std::endl;
            show_args(std::forward<Args>(args)...);
        }

        auto start = std::chrono::steady_clock::now();
        auto res = func(std::forward<Args>(args)...);
        auto end = std::chrono::steady_clock::now();

        ;

        if (!validate(res)) {
            std::cerr << "Test failed\n";
            return;
        }

        auto elapse_us = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
        std::cout << std::fixed << std::setprecision(3) << (elapse_us / 1000.0) << " ms\n";
    }
};

}

#endif
