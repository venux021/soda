#ifndef _LEETCODE_UNITTEST
#define _LEETCODE_UNITTEST

#include <any>
#include <chrono>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <utility>

#include "array.h"
#include "string.h"

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
struct DataSerializer
{
    static std::string serialize(const T &t);
    static T deserialize(const std::string &s);
};

template <>
struct DataSerializer<bool>
{
    static std::string serialize(bool res) { return res ? "true" : "false"; }
    static bool deserialize(const std::string &s) { return s == "true"; }
};

template <typename T>
struct DataSerializer<vector<T>>
{
    static std::string serialize(const std::vector<T> &v) { return Array::dump(v); }
    static std::vector<T> deserialize(const std::string &s) { return Array::load<T>(s); }
};

template <typename T>
struct DataSerializer<std::vector<std::vector<T>>>
{
    static std::string serialize(const std::vector<std::vector<T>> &v) { return Array::dump(v); }
    static std::vector<std::vector<T>> deserialize(const std::string &s) { return Array::load2d<T>(s); }
};

template <>
struct DataSerializer<std::string>
{
    static std::string serialize(const std::string &s) { return s; }
    static std::string deserialize(const std::string &s) { return s.substr(1, s.size()-2); }
};

// Test case counter
extern int __testNumber;

template <typename R, typename... Args>
class Tester {
public:
    // if show args
    bool showArgs {true};
    // if show result
    bool showResult {true};
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
    void all(Func solution, std::istream &input);

    template <typename Func>
    void all(Func solution, const std::string &filepath = "input_data.txt");

    template <typename Func>
    void all(Func solution, const std::vector<std::string> &filepathList) {
        for (auto &filepath : filepathList) {
            all(solution, filepath);
        }
    }

private:

    template <typename Func, typename... RealArgs>
    R execute(const R*, Func solution, RealArgs&&... args);

    template <typename... RealArgs>
    void default_args_player(RealArgs&&... args);

    void show_args() {}

    template <typename E>
    std::string to_str(const E &e) {
        return DataSerializer<E>::serialize(e);
    }

    template <typename T, typename... _Args>
    void show_args(const T &t, _Args&&... args)
    {
        std::cout << to_str(t) << std::endl;
        show_args(std::forward<_Args>(args)...);
    }

    template <typename Tuple, int I, typename T, typename... _Args>
    void parse_data(const std::vector<std::string> &args, Tuple &tp) {
        parse_element(args[I], std::get<I>(tp));
        parse_data<Tuple,I+1,_Args...>(args, tp);
    }

    template <typename E>
    void parse_element(const std::string &text, E &e) {
        e = DataSerializer<E>::deserialize(text);
    }

    template <typename Tuple, int I>
    void parse_data(const std::vector<std::string> &args, Tuple &tp) {
    }

};

#include "unittest_impl.h"

}

#endif
