
template <typename T>
vector<T> Array::load(istream &in, function<T(const string &)> conv) {
    string line;
    if (getline(in, line)) {
        return load(line, conv);
    } else {
        throw runtime_error("Invalid json list format");
    }
}

template <typename T>
vector<T> Array::load(string input, function<T(const string&)> conv) {
    vector<T> output;
    String::trimLeftTrailingSpaces(input);
    String::trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        String::trimLeftTrailingSpaces(item);
        String::trimRightTrailingSpaces(item);
        if (item.size() == 0) {
            break;
        }
        output.push_back(conv(item));
    }
    return output;
}

template <typename T>
vector<vector<T>> Array::load2d(istream &in) {
    string line;
    if (getline(in, line)) {
        return load2d<T>(line);
    } else {
        throw runtime_error("Invalid json list format");
    }
}

template <typename T>
vector<vector<T>> Array::load2d(const string &input) {
    vector<vector<T>> output;
    int pos = 0, end = int(input.size());
    auto skipW = [end](const string &s, int &pos) {
        while (pos < end && s[pos] == ' ') {
            ++pos;
        }
    };
    if (pos == end) {
        throw runtime_error("Invalid json array format");
    }
    skipW(input, pos);
    ++pos;
    skipW(input, pos);
    if (input[pos] == ']') {
        return output;
    }
    while (true) {
        skipW(input, pos);
        int start = pos;
        while (input[pos++] != ']')
            ;;
        output.push_back(load<T>(input.substr(start, pos-start)));
        skipW(input, pos);
        if (input[pos] == ']') {
            break;
        }
        ++pos;  // skip ','
    }
    return output;
}

template <typename T>
string Array::dump(const vector<T> &list, function<string(const T&)> conv) {
    string buffer("[");
    for (int i = 0; i < int(list.size()); ++i) {
        buffer.append(conv(list[i]));
        if (i < int(list.size()) - 1) {
            buffer.append(", ");
        }
    }
    buffer.push_back(']');
    return buffer;
}
