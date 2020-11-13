module Soda end

module Soda::Unittest

class BaseCodec
    def encode(obj)
        raise "Not implemented"
    end
    def decode(ser)
        raise "Not implemented"
    end
end

class DefaultCodec < BaseCodec
    def encode(obj)
        obj
    end
    def decode(ser)
        ser
    end
end

class CodecFactory
    @@cmap = {}
    @@cmap.default = DefaultCodec.new

    def self.create(obj_type)
        @@cmap[obj_type]
    end
end

end  # module Soda::Unittest
