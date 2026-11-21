
import sys, os
sys.path.append(__file__.rsplit("futilities", 1)[0])
from futilities.aliases import function, method, mappingproxy
from futilities.miscellaneous_debris import rename_function, copy_function
from _collections import _tuplegetter
from math import floor, ceil, trunc
from operator import itemgetter, attrgetter, __call__
from itertools import chain
from abcd._mathdomains_abcd_ import ABCDMeta


__globals__ = (lambda:x).__globals__


__all__ = []
def ꓸꓸregistriesꓸꓸ(ˍˍᴀʟʟˍˍ: list, /, *names: str):
    if names:  return ˍˍᴀʟʟˍˍ.extend(names)
    return (lambda f: (ˍˍᴀʟʟˍˍ.append(f.__name__) or f))
ꓸꓸregisterꓸꓸ = method(ꓸꓸregistriesꓸꓸ, __all__)
ꓸꓸregisteredꓸꓸ = ꓸꓸregisterꓸꓸ()



@ꓸꓸregisteredꓸꓸ
class AbstractOperatorHacks(metaclass=ABCDMeta):
    _abc_registry: set[type|object] = set()
    @classmethod
    def __contains__(cls, item):
        return (item in cls._abc_registry) or (type(item) in cls._abc_registry)
    @classmethod
    def _op_hack_decorator(cls, subclass: type):
        cls._abc_registry.add(subclass)
        return subclass
operator_hack = AbstractOperatorHacks._op_hack_decorator
ꓸꓸregisterꓸꓸ('operator_hack')


opmethodnames_ref = {
    getattr: "__getattribute__", setattr: "__setattr__", delattr: "__delattr__",
    ':': "__get__", ':=': "__set__", 'del': "__delete__", 'del ': "__delete__", 
    '.': '__getattribute__', '.=': "__setattr__", 'del .': "__delattr__", 
    '[]': '__getitem__', '[]=': '__setitem__', 'del []': '__delitem__',  
    '[T]': '__class_getitem__', 'cls_getitem': '__class_getitem__', 
    '()': '__call__', 
    'in': '__contains__', ' in ': '__contains__', 
    len: "__len__", iter: "__iter__", reversed: "__reversed__", 
    str: "__str__", repr: "__repr__", format: "__format__", 
    bool: "__bool__", int: "__int__", float: "__float__", complex: "__complex__", bytes: "__bytes__", 
    floor: "__floor__", ceil: "__ceil__", trunc: "__trunc__", 
    round: "__round__", abs: "__abs__", 
    '~': '__invert__', '-': '__neg__', '+': '__pos__', '**-1': '__mulinv__', 
    '==': '__eq__', '!=': '__ne__', '<': '__lt__', '>': '__gt__', '<=': '__le__', '>=': '__ge__', 
    'or_': '__or__', 'and_': '__and__', 
    }|{
    f"{['','r',''][ꘌ]}{ꕺ}{['','','='][ꘌ]}": f"__{['','r','i'][ꘌ]}{μ}__" for ꘌ in range(3) 
    for ꕺ, μ in {'|': 'or', '&': 'and', '^': 'xor', 
                        '<<': 'lshift', '>>': 'rshift', '@': 'matmul', 
                        ' + ': 'add', ' - ': 'sub', '*': 'mul', '/': 'truediv', '**': 'pow', 
                        '//': 'floordiv', '%': 'mod', '/%/': 'divmod'}.items()}
opmethodnames_ref.update({v.strip('_'): v for k,v in opmethodnames_ref.items()})
opmethodnames_ref = mappingproxy(opmethodnames_ref)
opmethodnames_ref_keys_isdisjoint = opmethodnames_ref.keys().isdisjoint
opmethodnames_ref_keys_intersect = opmethodnames_ref.keys().__and__
@ꓸꓸregisteredꓸꓸ
def quiktyp(name: str="_ᴄʟꜱ", base: type=None, namespace: dict=None, 
*, bases: tuple[type]=(), type_:type=type, instantiate: bool=True, **kwargs):
    "Convenience definer for quick nasty types."
    if type(name) is not str:
        name, base, namespace = sorted([name, base, namespace], key=lambda x: 
                                                                    (isinstance(x, type) - isinstance(x, dict)))
    if (base is not None):
        bases = base if (type(base) is tuple) else (((base,)+bases) if bases else (base,))
    if (namespace is None):
        namespace = (kwargs or {})
    elif kwargs:
        namespace.update(kwargs)
    if ('op_eval_priority' not in namespace):
        namespace['op_eval_priority'] = 20
    if commonkeys := opmethodnames_ref_keys_intersect(namespace):
        namespace.update({opmethodnames_ref[k]: namespace.pop(k) for k in commonkeys})
    T = operator_hack(type_(name, bases, namespace))
    return T() if instantiate else T

@ꓸꓸregisteredꓸꓸ
def rightarg_passthrough(func: function):
    "Convenience hack for quiktyp methods which makes a static unary function assigned to a binary operator recieve the right-hand/ʻotherʼ parameter.  Like, for the hack ᴘǃ := quiktyp(and_=print)(), ᴘǃ&output would print both ᴘǃ and output.  You could define and_=lambda _,x: print(x), or use this function, which also comes in the form of an ophack with appropriately confusing unicode:  (_ꓹᯬ), which uses '>' as its operator, making the above example:  ᴘǃ = quiktyp(and_=_ꓹᯬ>print)()"
    ǁꜰᴜɴᴄǁ = func
    def _passthru(_,x):  return ǁꜰᴜɴᴄǁ(x)
    return _passthru

_ꓹᯬ = quiktyp("(pasθru)", tuple, gt=property(itemgetter(0)), instantiate=0)((rightarg_passthrough,))

#ᴘǃ = quiktyp(base=tuple, and_=_ꓹᯬ>print, or_=property(itemgetter(0)))((print,))
#ᴘǃ&((1,2,3))
#ᴘǃ|((1,2,3))
operator_hack(_ꓹᯬ)
ꓸꓸregisterꓸꓸ("_ꓹᯬ")


#@ꓸꓸregisteredꓸꓸ
#@operator_hack
#class ǂ(tuple):
#    ǀ0ǀ = _tuplegetter(0, "[0]")
#    ⲷ =
#    def __class_getitem__(cls, key):  return key
#    def __getitem__(self, key):  return ǂ((itemgetter(key),))
#    def __or__(self, other):  return __call__(*self, other)
@ꓸꓸregisteredꓸꓸ
@operator_hack
class ǂ(tuple):
    op_eval_priority: int = 20
    
    def __class_getitem__(cls, key):  return key
    ǀ0ǀ = _tuplegetter(0, '0')
    ǀ1ǀ, ǀ2ǀ, ǀ3ǀ = [_tuplegetter(i, str(i)) for i in range(1,4)]
    ǁ = property(tuple)
    def __getitem__(self, key):
        if (type(key) is not tuple):
            key = (key,)
        return ǂ(chain(self, key)) if self else ǂ(key)
    def itemgetter(self):  return itemgetter(*self)
    def __or__(self, other):  return itemgetter(*self)(other)
    def __call__(self, other):  return other[*self]

'ʻꓼʼ'

@ꓸꓸregisteredꓸꓸ
@operator_hack
class infix(tuple):
    op_eval_priority: int = 20
    def __ror__(self, other):  return infix(self + (other,))
    def __or__(self, other):
        try:  return __call__(*self, other)
        except (ValueError, TypeError):  return infix(self + (other,))
    __sub__ = __or__


_itemget_ǀꓽꓽᐨ1ǀ = itemgetter(ǂ[::-1])
_itemget_ǀ1ꓽǀ = itemgetter(ǂ[1::])
_itemget_ǀ0ꓹ1ꓽǀ = ǂ(ǂ[0, 1::]).itemgetter
#_itemget_ǀ0ꓽᐨ1ꓹᐨ1ǀ = ǂ(ǂ[0:-1:, -1]).itemgetter
ǀꓽꓽǀ = ǂ[::]

ꓸꓸregisterꓸꓸ("_itemget_ǀꓽꓽᐨ1ǀ", "_itemget_ǀ1ꓽǀ", "_itemget_ǀ0ꓹ1ꓽǀ", "ǀꓽꓽǀ")

