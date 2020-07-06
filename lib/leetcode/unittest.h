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

template <typename T>
struct DataLoader
{
    static T load(std::istream &input) {
        T t;
        input >> t;
        return t;
    }
};

// Test case counter
extern int __testNumber;

template <typename R, typename... Args>
class Tester {

    std::unordered_map<int,std::any> serialMap;

public:
    // if show args
    bool showArgs {true};
    // if show result
    bool showResult {true};
    // function to show result
    std::function<void(const R&)> resultPlayer;

    // function to validate result
    std::function<bool(const R*, const R*)> validator;

    Tester();

    template <typename Func, typename... RealArgs>
    R test(const R &answer, Func solution, RealArgs&&... args) {
        return this->execute(&answer, solution, std::forward<RealArgs>(args)...);
    }

    template <typename Func, typename... RealArgs>
    R run(Func solution, RealArgs&&... args) {
        return this->execute(nullptr, solution, std::forward<RealArgs>(args)...);
    }

    template <typename Func>
    void all(Func solution, std::istream &input) {
        std::tuple<Args...> tp;
        //cout << "tuple size: " << std::tuple_size<std::tuple<Args...>>::value << endl;
        load_data<decltype(tp),0,Args...>(input, tp);
        std::apply(solution, tp);
    }

    template <typename Func>
    void all(Func solution, const std::string &filepath) {
        ifstream input(filepath);
        all(solution, input);
    }

    template <typename Func>
    void all(Func solution, const std::vector<std::string> &filepathList);

    // set serializer, the return old
    template <typename T> std::function<std::string(const T&)> serializer(std::function <std::string(const T&)> s);

    // get serializer
    template <typename T> std::function<std::string(const T&)> serializer();

private:

    template <typename Func, typename... RealArgs>
    R execute(const R*, Func solution, RealArgs&&... args);

    template <typename... RealArgs>
    void default_args_player(RealArgs&&... args);

    void default_result_player(const R &res);

    void show_args() {}

    template <typename T, typename... _Args>
    void show_args(const T &t, _Args&&... args)
    {
        std::cout << serializer<T>()(t) << std::endl;
        show_args(std::forward<_Args>(args)...);
    }

    template <typename Tuple, int I, typename T, typename... _Args>
    void load_data(std::istream &input, Tuple &tp) {
        load_element(input, std::get<I>(tp));
        load_data<Tuple,I+1,_Args...>(input, tp);
    }

    template <typename E>
    void load_element(std::istream &input, E &e) {
        e = DataLoader<E>::load(input);
    }

    template <typename Tuple, int I>
    void load_data(std::istream &input, Tuple &tp) {
    }
};

#include "unittest_impl.h"

}

#endif
