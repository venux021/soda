#ifndef _LEETCODE_UNITTEST
#define _LEETCODE_UNITTEST

#include <any>
#include <chrono>
#include <exception>
#include <functional>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <utility>

#include "array.h"

namespace leetcode {

class IdGen
{
    static int seq;
public:
    static int nextId() {
        return ++seq;
    }
};

template <typename T>
class TypeId
{
    static int _id;
public:
    static int id();
};

template <typename T>
struct DefaultSerializer
{
    static std::string serialize(const T &t);
};

template <>
struct DefaultSerializer<bool>
{
    static std::string serialize(bool res);
};

template <typename T>
struct DefaultSerializer<vector<T>>
{
    static std::string serialize(const vector<T> &v);
};

// Test case counter
extern int __testNumber;

template <typename R, typename... Args>
class Tester {

    std::unordered_map<int,std::any> serialMap;

public:
    // if show args
    bool showArgs {true};
    // function to show args
    std::function<void(Args&&...)> argsPlayer;

    // if show result
    bool showResult {true};
    // function to show result
    std::function<void(const R&)> resultPlayer;

    // function to validate result
    std::function<bool(const R&)> validator;

    Tester();

    void test(std::function<R(Args&&...)> solution, Args&&... args, const R &correct);

    void test(std::function<R(Args&&...)> solution, Args&&... args) {
        execute(solution, std::forward<Args>(args)..., validator);
    }

    // set serializer, the return old
    template <typename T> std::function<std::string(const T&)> serializer(std::function <std::string(const T&)> s);

    // get serializer
    template <typename T> std::function<std::string(const T&)> serializer();

private:

    void execute(std::function<R(Args&&...)> solution, Args&&... args, std::function<bool(const R&)> validateFunc);

    void default_args_player(Args&&... args);

    void default_result_player(const R &res);

    void show_args() {}

    template <typename T, typename... _Args>
    void show_args(const T &t, _Args&&... args)
    {
        std::cout << serializer<T>()(t) << std::endl;
        show_args(std::forward<_Args>(args)...);
    }
};

#include "unittest_impl.h"

}

#endif
