# step [1]: implement solution function

if __FILE__ == $0
    require 'soda/unittest/job'
    su = Soda::Unittest
    # step [2]: setup function/return/arguments
    # class, method name, return type, arg types
    su::JobEntry.run(method(:FUNCTION), _, _)

    # su::JobEntry.runWithObjectCheck(func, ret, args, obj_validator)
    # su::JobEntry.runWithSerialCheck(func, ret, args, ser_validator)
end
