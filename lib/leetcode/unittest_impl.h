template <typename T>
std::string DefaultSerializer<T>::serialize(const T &t)
{
    std::ostringstream common_out;
    common_out << t;
    return common_out.str();
}

std::string DefaultSerializer<bool>::serialize(bool res)
{
    std::ostringstream out;
    out << std::boolalpha << res;
    return out.str();
}

template <typename T>
std::string DefaultSerializer<vector<T>>::serialize(const vector<T> &v)
{
    return Array::dump(v);
}

template <typename T>
int TypeId<T>::_id = 0;

template <typename T>
int TypeId<T>::id() {
    if (_id == 0) {
        _id = IdGen::nextId();
    }
    return _id;
}

template <typename R, typename... Args>
Tester<R,Args...>::Tester() {
    argsPlayer = [this](auto&&... args) {
        this->default_args_player(std::forward<Args>(args)...);
    };
    resultPlayer = [this](const R &res) {
        this->default_result_player(res);
    };
    validator = [](const R&){return true;};
}

template <typename R, typename... Args>
void Tester<R,Args...>::test(std::function<R(Args&&...)> solution, Args&&... args, const R &correct) {
    auto validateFunc = [&] (const R &res) { 
        if (res != correct) {
            std::cerr << "Wrong answer " << res << ", but " << correct << " expected" << std::endl;
            return false;
        }
        return true;
    };
    execute(solution, std::forward<Args>(args)..., validateFunc);
}

template <typename R, typename... Args>
    template <typename T>
std::function<std::string(const T&)> Tester<R,Args...>::serializer(std::function <std::string(const T&)> s) {
    int id = TypeId<T>::id();
    auto old = serializer<T>();
    serialMap[id] = s;
    return old;
}

template <typename R, typename... Args>
    template <typename T>
std::function<std::string(const T&)> Tester<R,Args...>::serializer() {
    int id = TypeId<T>::id();
    auto p = serialMap.find(id);
    if (p == serialMap.end()) {
        std::function<std::string(const T&)> func = DefaultSerializer<T>::serialize;
        serialMap[id] = func;
    }
    return std::any_cast<std::function<std::string(const T&)>>(serialMap[id]);
}

template <typename R, typename... Args>
void Tester<R,Args...>::execute(std::function<R(Args&&...)> solution, Args&&... args, std::function<bool(const R&)> validateFunc) {
    ++__testNumber;
    std::cout << "**[" << __testNumber << "]**\n";

    if (showArgs) {
        argsPlayer(std::forward<Args>(args)...);
    }

    auto start = std::chrono::steady_clock::now();
    auto res = solution(std::forward<Args>(args)...);
    auto end = std::chrono::steady_clock::now();

    if (!validateFunc(res)) {
        throw std::runtime_error("Test Failed");
        //std::cerr << "Test failed\n";
        //return;
    }

    if (showResult) {
        resultPlayer(res);
    }

    std::cout << "----\n";

    auto elapse_us = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout << std::fixed << std::setprecision(3) << (elapse_us / 1000.0) << " ms\n";

    std::cout << '\n';
}

template <typename R, typename... Args>
void Tester<R,Args...>::default_args_player(Args&&... args) {
    std::cout << "input:" << std::endl;
    show_args(std::forward<Args>(args)...);
}

template <typename R, typename... Args>
void Tester<R,Args...>::default_result_player(const R &res) {
    std::cout << "output:" << std::endl;
    show_args(res);
}
