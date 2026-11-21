from types import (
    MappingProxyType, ModuleType, 
    FrameType, TracebackType, 
    GeneratorType, AsyncGeneratorType, CoroutineType, 
    CellType, CodeType, 
    FunctionType, BuiltinFunctionType, 
    MethodType, MethodWrapperType, 
    MethodDescriptorType, ClassMethodDescriptorType, WrapperDescriptorType, 
    MemberDescriptorType, GetSetDescriptorType, 
    
    LambdaType, BuiltinMethodType, 
    )
import sys
sys.path.append(__file__.rsplit("futilities", 1)[0])
from abcd._abcd_ import (
    FrameLocalsProxy, 
    dict_keys, dict_values, dict_items, 
    bytes_iterator, bytearray_iterator, dict_keyiterator, dict_valueiterator, dict_itemiterator, list_iterator, list_reverseiterator, range_iterator, longrange_iterator, set_iterator, str_iterator, tuple_iterator, zip_iterator, 
    )

str_ascii_iterator = str_iterator


['bytearray_iterator', 'bytes_iterator', 'dict_itemiterator', 'dict_items', 'dict_keyiterator', 'dict_keys', 'dict_valueiterator', 'dict_values', 'list_iterator', 'list_reverseiterator', 'longrange_iterator', 'range_iterator', 'set_iterator', 'str_iterator', 'tuple_iterator', 'zip_iterator']


__doc__ = "Alternative to python’s types module where the each type is registered under its actual, lowercase .__name__ attribute, with some minor exceptions and additional aliases."


__all__ = [
    "module", 
    "mappingproxy", 
    "frame", "traceback", "FrameLocalsProxy", 
    "generator", "async_generator", "coroutine", 
    "cell", "code", 
    "function", "builtin_function_or_method", 
    "slot_wrapper", 
    "method", "method_wrapper", 
    "method_descriptor", "classmethod_descriptor", "wrapper_descriptor", 
    "member_descriptor", "getset_descriptor", 
    
    "dict_keys", "dict_values", "dict_items", 
    
    "str_iterator", "str_ascii_iterator", "bytes_iterator", "bytearray_iterator", 
    "tuple_iterator", "list_iterator", "list_reverseiterator", 
    "set_iterator", "dict_keyiterator", "dict_valueiterator", "dict_itemiterator", 
    "range_iterator", "longrange_iterator", "zip_iterator", 
    
    "membertypes", "methodtypes", "descriptortypes", "wrappertypes", "membertypes_all", 
    ]

slot_wrapper = type(int.__eq__)

######## ######## ######## ######## ######## ######## ######## ########
########  ↓↓↓↓ (copied and modified from the types module) ↓↓↓↓  ########
######## ######## ######## ######## ######## ######## ######## ########

# Iterators in Python aren't a matter of type but of protocol.  A large
# and changing number of builtin types implement *some* flavor of
# iterator.  Don't check the type!  Use hasattr to check for both
# "__iter__" and "__next__" attributes instead.

def _f(): pass
function = type(_f)
lambda_type = type(lambda: None)         # Same as FunctionType
try:
    assert (lambda_type is function)
except AssertionError:
    __all__.insert(__all__.index("function") + 1, "lambda_type")
else:
    del lambda_type
code = type(_f.__code__)
mappingproxy = type(type.__dict__)
#SimpleNamespace = type(sys.implementation)

def _cell_factory():
    a = 1
    def f():
        nonlocal a
    return f.__closure__[0]
cell = type(_cell_factory())

def _g():
    yield 1
generator = type(_g())

async def _c(): pass
_c = _c()
coroutine = type(_c)
_c.close()  # Prevent ResourceWarning

async def _ag():
    yield
_ag = _ag()
async_generator = type(_ag)

class _C:
    def _m(self): pass
method = type(_C()._m)


builtin_function_or_method = type(len)
#builtin_method = type([].append)     # Same as BuiltinFunctionType

wrapper_descriptor = type(object.__init__)
method_wrapper = type(object().__str__)
method_descriptor = type(str.join)
classmethod_descriptor = type(dict.__dict__['fromkeys'])

module = type(sys)

try:
    raise TypeError
except TypeError:
    tb = sys.exc_info()[2]
    traceback = type(tb)
    frame = type(tb.tb_frame)
    tb = None; del tb

# For Jython, the following two types are identical
getset_descriptor = type(function.__code__)
member_descriptor = type(function.__globals__)

del sys, _f, _g, _C, _c, _ag  # Not for export

######## ######## ######## ######## ######## ######## ######## ########
######## ######## ######## ######## ######## ######## ######## ########

def _accuracy_test():
    
    for _name in filter(globals().__contains__, __all__):
        _typeobj = globals()[_name]
        if (_typeobj.__name__ != _name):
            print(f"{_name} = {_typeobj.__name__}")
    exit()



membertypes = (member_descriptor, getset_descriptor, property)
methodtypes = (method, method_descriptor, method_wrapper, classmethod, classmethod_descriptor, staticmethod) + (function, builtin_function_or_method)
descriptortypes = (member_descriptor, wrapper_descriptor, getset_descriptor, method_descriptor, classmethod_descriptor)
wrappertypes = (wrapper_descriptor, method_wrapper, slot_wrapper)

membertypes_all = (method, method_descriptor, method_wrapper, classmethod, classmethod_descriptor, staticmethod, function, builtin_function_or_method, wrapper_descriptor, method_wrapper, slot_wrapper, member_descriptor, wrapper_descriptor, getset_descriptor, method_descriptor, classmethod_descriptor, property)

