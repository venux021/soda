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
    resultPlayer = [this](const R &res) {
        this->default_result_player(res);
    };
    validator = [](const R* res, const R* ans){
        return *res == *ans;
    };
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
    template <typename Func, typename... RealArgs>
R Tester<R,Args...>::execute(const R* answer, Func solution, RealArgs&&... args) {
    ++__testNumber;
    std::cout << "**[" << __testNumber << "]**\n";

    if (showArgs) {
        default_args_player(std::forward<RealArgs>(args)...);
    }

    auto start = std::chrono::steady_clock::now();
    R res = solution(std::forward<RealArgs>(args)...);
    auto end = std::chrono::steady_clock::now();

    if (!answer) {
        std::cerr << "[WARNING] No answer presented\n";
    } else if (!validator(&res, answer)) {
        throw std::runtime_error("Test Failed");
    }

    if (showResult) {
        resultPlayer(res);
    }

    std::cout << "----\n";

    auto elapse_us = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout << std::fixed << std::setprecision(3) << (elapse_us / 1000.0) << " ms\n";

    std::cout << '\n';
    return res;
}

template <typename R, typename... Args>
    template <typename... RealArgs>
void Tester<R,Args...>::default_args_player(RealArgs&&... args) {
    std::cout << "input:" << std::endl;
    show_args(std::forward<RealArgs>(args)...);
}

template <typename R, typename... Args>
void Tester<R,Args...>::default_result_player(const R &res) {
    std::cout << "output:" << std::endl;
    show_args(res);
}
