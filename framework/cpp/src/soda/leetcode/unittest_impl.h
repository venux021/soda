template <typename T>
std::string DataSerializer<T>::serialize(const T &t)
{
    std::ostringstream common_out;
    common_out << t;
    return common_out.str();
}

template <typename T>
T DataSerializer<T>::deserialize(const std::string &text)
{
    istringstream input(text);
    T t;
    input >> t;
    return t;
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
    validator = [](const R* res, const R* ans){
        return *res == *ans;
    };
}

template <typename R, typename... Args>
    template <typename Func>
void Tester<R,Args...>::all(Func solution, std::istream &input) {
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
            R ans = DataSerializer<R>::deserialize(answer);
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

template <typename R, typename... Args>
    template <typename Func>
void Tester<R,Args...>::all(Func solution, const std::string &filepath/* = "input_data.txt" */) {
    std::ifstream fin(filepath);
    if (!fin) {
        std::cerr << "[ERROR] Unable to read file " << filepath << std::endl;
        return;
    }
    all(solution, fin);
}

template <typename R, typename... Args>
    template <typename Func, typename... RealArgs>
R Tester<R,Args...>::execute(const R* answer, Func solution, RealArgs&&... args) {
    ++__testNumber;
    std::cout << "**[" << __testNumber << "]**" << std::endl;

    if (showArgs) {
        default_args_player(std::forward<RealArgs>(args)...);
    }

    auto start = std::chrono::steady_clock::now();
    R res = solution(std::forward<RealArgs>(args)...);
    auto end = std::chrono::steady_clock::now();

    if (!answer) {
        std::cerr << "[WARNING] No answer presented\n";
    } else if (!validator(&res, answer)) {
        std::cerr << "[ERROR] Testing failed\n";
        std::cerr << "output: " << to_str(res) << '\n';
        std::cerr << "expect: " << to_str(*answer) << '\n';
        std::exit(2);
    }

    if (showResult) {
        std::cout << "output:\n" << to_str(res) << std::endl;
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

