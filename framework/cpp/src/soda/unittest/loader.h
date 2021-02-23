#ifndef _SODA_UNITTEST_LOADER_H_
#define _SODA_UNITTEST_LOADER_H_

#include <iostream>
#include <memory>
#include <string>

namespace soda::unittest {

class WorkLoader {
public:
    virtual ~WorkLoader() = default;

    virtual std::string load() = 0;

    virtual void store(const std::string& jstr) = 0;
};

class StdinWorkLoader : public WorkLoader {
public:
    std::string load() override;

    void store(const std::string& jstr) override {
        std::cout << jstr;
    }
};

class LoaderFactory {
public:
    static std::shared_ptr<WorkLoader> byStdin() {
        return std::make_shared<StdinWorkLoader>();
    }
};

} // namespace soda::unittest

#endif
