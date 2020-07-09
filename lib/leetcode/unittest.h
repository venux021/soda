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
struct DataParser
{
    static T parse(const std::string &text) {
        istringstream input(text);
        T t;
        input >> t;
        return t;
    }
};

template <typename T>
struct DataParser<vector<T>>
{
    static vector<T> parse(const string &text) {
        return Array::load<T>(text);
    }
};

template <typename T>
struct DataParser<vector<vector<T>>>
{
    static vector<vector<T>> parse(const string &text) {
        return Array::load2d<T>(text);
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
        size_t argsCount = std::tuple_size<std::tuple<Args...>>::value;
        while (true) {
            std::vector<std::string> args;
            while (args.size() < argsCount + 1) {
                std::string line;
                if (!std::getline(input, line)) {
                    return;
                }
                line = String::trim(line);
                if (line.size() == 0 || line[0] == '#') {
                    continue;
                }
                args.push_back(line);
            }
            std::string answer = args.back();
            args.pop_back();

            std::tuple<Args...> tp;
            parse_data<decltype(tp),0,Args...>(args, tp);

            if (answer != "null") {
                R ans = DataParser<R>::parse(answer);
                auto caller = [this,&ans,solution](auto&&... arguments) {
                    return this->test(ans, solution, std::forward<decltype(arguments)>(arguments)...);
                };
                std::apply(caller, tp);
            } else {
                auto caller = [this,solution](auto&&... arguments) {
                    return this->run(solution, std::forward<decltype(arguments)>(arguments)...);
                };
                std::apply(caller, tp);
            }
        }
    }

    template <typename Func>
    void all(Func solution, const std::string &filepath = "input_data.txt") {
        std::ifstream fin(filepath);
        if (!fin) {
            std::cerr << "[ERROR] Unable to read file " << filepath << std::endl;
            return;
        }
        all(solution, fin);
    }

    template <typename Func>
    void all(Func solution, const std::vector<std::string> &filepathList) {
        for (auto &filepath : filepathList) {
            all(solution, filepath);
        }
    }

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

    // template <typename Tuple, int I, typename T, typename... _Args>
    template <typename Tuple, int I, typename T, typename... _Args>
    void parse_data(const std::vector<std::string> &args, Tuple &tp) {
        parse_element(args[I], std::get<I>(tp));
        parse_data<Tuple,I+1,_Args...>(args, tp);
    }

    template <typename E>
    void parse_element(const std::string &text, E &e) {
        e = DataParser<E>::parse(text);
    }

    // template <typename Tuple, int I>
    template <typename Tuple, int I>
    void parse_data(const std::vector<std::string> &args, Tuple &tp) {
    }
};

#include "unittest_impl.h"

}

#endif
