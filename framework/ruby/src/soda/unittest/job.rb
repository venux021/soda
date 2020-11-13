require 'json'
require 'time'

require 'soda/unittest/codec'

module Soda end

module Soda::Unittest

class JobEntry
    def self.run(function, ret_type, arg_types)
        runJob(function, ret_type, arg_types, false, nil, nil)
    end

    def self.runWithObjectCheck(function, ret_type, arg_types, object_validator)
        runJob(function, ret_type, arg_types, true, object_validator, nil)
    end

    def self.runWithSerialCheck(function, ret_type, arg_types, serial_validator)
        runJob(function, ret_type, arg_types, false, nil, serial_validator)
    end

    def self.runJob(function, ret_type, arg_types, validate_by_object=false, object_validator=nil, serial_validator=nil)
        jspec = JobSpec.new(function, ret_type, arg_types)
        jspec.validate_by_object = validate_by_object
        jspec.object_validator = object_validator
        jspec.serial_validator = serial_validator
        JobRunner.new.run(jspec)
    end
end

class InputData
    def initialize(_js)
        @json = _js
    end

    def expected
        @json['expected']
    end

    def id
        @json['id']
    end

    def args
        @json['args']
    end

    def arg(index)
        @json['args'][index]
    end
end

class JobSpec
    def initialize(function, ret_type, arg_types)
        @function = function
        @ret_type = ret_type
        @arg_types = arg_types
        @validate_by_object = false
        @object_validator = nil
        @serial_validator = nil
    end

    attr_accessor :function, :ret_type, :arg_types, :validate_by_object, :object_validator, :serial_validator
end

class JobRunner
    def run(jspec)
        input_data = InputData.new(JSON.parse(ARGF.read))
        args = jspec.arg_types.each_with_index.map { |t,i|
            decode(t, input_data.arg(i))
        }

        start_time = Time.now
        res = jspec.function.call(*args)
        end_time = Time.now

        serial_res = encode(jspec.ret_type, res)
        elapse_ms = (end_time - start_time) * 1000.0

        resp = {
            'id' => input_data.id,
            'result' => serial_res,
            'elapse' => elapse_ms
        }

        success = true
        if !input_data.expected.nil?
            if jspec.validate_by_object
                expc = decode(jspec.ret_type, input_data.expected)
                vf = jspec.object_validator || -> (e, r) { e == r }
                success = vf.call(expc, res)
            else
                vf = jspec.serial_validator || -> (e, r) { e == r }
                success = vf.call(input_data.expected, serial_res)
            end
        end

        resp['success'] = success

        puts resp.to_json
    end

    def encode(obj_type, obj)
        CodecFactory.create(obj_type).encode(obj)
    end

    def decode(obj_type, ser)
        CodecFactory.create(obj_type).decode(ser)
    end
end

end  # module Soda::Unittest
