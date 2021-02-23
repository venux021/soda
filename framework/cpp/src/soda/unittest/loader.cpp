#include "loader.h"

namespace soda::unittest {

std::string StdinWorkLoader::load() {
    std::string line, content;
    while (std::getline(std::cin, line)) {
        content += line;
    }
    return content;
}

} // namespace soda::unittest
