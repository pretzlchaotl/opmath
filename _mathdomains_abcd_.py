
import sys, os
sys.path.append(__file__.rsplit("abcd", 2)[0])
from abcd import _abcd_, _collections_abcd_, _numbers_abcd_
from abcd._abcd_ import *
from abcd._numbers_abcd_ import *
from abcd._collections_abcd_ import *


__all__ = []
modulefunc, modulefuncs = _abcd_.g_modulefuncfuncs(__all__)



SequenceIndexTypage = (int | slice)

PredicateTypage = Callable[[object], bool]
RelationTypage = Callable[[object, object], bool]
NAryRelationTypage = Callable[[object, ...], bool]
DomainTypage = (ABCDMeta, _abcd_.GenericAlias)
FuncDomainsTypage = tuple[tuple[DomainTypage], DomainTypage]


modulefuncs("SequenceIndexTypage", "PredicateTypage", "RelationTypage", "NAryRelationTypage", "DomainTypage", "FuncDomainsTypage")

@modulefunc
class Natural(Integral, metaclass=ABCDMeta):
    "Natural numbers are positive whole numbers."
    __slots__ = ()
    
    @classmethod
    def __instancecheck__(cls, instance):
        if ABCDMeta.__instancecheck__(cls, instance):  return True
        return (isinstance(instance, Integral) and not (instance < 0))
    
    @classmethod
    def __subclasscheck__(cls, subclass):
        if ABCDMeta.__subclasscheck__(cls, subclass):  return True
        if issubclass(subclass, Integral):
            try:  return bool(subclass(-1) >= 0)
            except (TypeError, ValueError):  pass
        return False


@modulefunc
class Stringlike(Sequence, metaclass=ABCDMeta):
    "Stringlikes are mathematically-compatable String objects.  In python, they include:  (str, bytes, and numpy.str_)."
    __slots__ = ()
    
    @abstractmethod
    def split(self, /, sep=None, maxsplit=-1):  raise NotImplementedError
    @abstractmethod
    def join(self, iterable, /):  raise NotImplementedError
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Stringlike):  return _check_methods(C, "split", "join")
        #if (cls is Stringlike) and _check_methods(C, "__getitem__", ""):
        #    ( ¿ maybe check that type(C()[0][0][0][...) is C ? )    #
        return NotImplemented


@modulefunc
class Vector(Sequence, Number):
    "Vectors are arithmetic Sequences/matrices of numbers or other operands."
    __slots__ = ()
    
    @abstractmethod
    def __matmul__(self, other):
        raise NotImplementedError
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Vector):  return _check_methods(C, "__matmul__") #, "__buffer__"
        return NotImplemented


MathDomainTypes = (
        NonFinite, 
        Object, Oblivion, 
        Callable, 
        Iterable, Container, 
        Set, Mapping, 
        Sequence, Stringlike, Vector, 
        Number, Complex, Real, Rational, Integral, Natural, 
        Lattice, Bool, 
    )
#modulefuncs(Auto, *MathDomainTypes)
modulefunc("MathDomainTypes")



dXx = ⲈXx = NonFinite

dOb = ⲈOʙ = Object
dOv = ⲈOᴠ = Oblivion

dFc = ⲈFᴄ = Callable
#dHa = ⲈHᴀ = Hashable
dIt = ⲈIᴛ = Iterable

dCt = ⲈCᴛ = Container
dSp = ⲈSᴘ = Set
dMp = ⲈMᴘ = Mapping
dSq = ⲈSવ = Sequence

dCh = ⲈCʜ = Stringlike
dVc = ⲈVᴄ = Vector

dUn = ⲈUɴ = Number
dCn = ⲈCɴ = Complex
dRn = ⲈRɴ = Real
dQn = ⲈQɴ = Rational
dZn = ⲈZɴ = Integral
dNn = ⲈNɴ = Natural

dLt = ⲈLᴛ = Lattice
dBl = ⲈBʟ = Bool

_ⲈƒxGenericAlias = _CallableGenericAlias

Ⲉ_ = ⲈOᴠ
Ⲉƒx = ⲈFᴄ
Ⲉⲉⰵ = ⲈCᴛ
Ⲉⵁ = ⲈSᴘ
Ⲉǃǃ = ⲈBʟ

#    ⲈⰅ    ⲉⰵ    #

_domainnicknames_0 = [
    'dXx','dOb', 'dOv', 
    'dFc', 'dIt', 'dCt', 'dSp', 'dMp', 'dSq', 'dCh', 'dVc', 'dUn', 'dCn', 'dRn', 'dQn', 'dZn', 'dLt', 'dBl',
    ]
_domainnicknames = [
    'ⲈXx', 
    'ⲈOʙ', 'ⲈOᴠ', 
    'ⲈFᴄ', #'ⲈHᴀ', 
    'ⲈIᴛ', 
    'ⲈCᴛ', 'ⲈSᴘ', 'ⲈMᴘ', 'ⲈSવ', 
    'ⲈCʜ', 'ⲈVᴄ', 
    'ⲈUɴ', 'ⲈCɴ', 'ⲈRɴ', 'ⲈQɴ', 'ⲈZɴ', 'ⲈNɴ', 
    'ⲈLᴛ', 'ⲈBʟ', 
    '_ⲈƒxGenericAlias', 
'Ⲉ_',    'Ⲉƒx',     'Ⲉⲉⰵ', 'Ⲉⵁ',     'Ⲉǃǃ',     ]
for _name in _domainnicknames[:-4]:
    eval(_name).__name__ = _name
modulefunc("_domainnicknames")
modulefuncs(_domainnicknames)
del _name, _domainnicknames_0



#print(f"{(_abcd_.__globals__ is _abcd_.__dict__) = }")

#_abcd_globals_ = (_abcd_.__dict__|_numbers_abcd_.__dict__|_collections_abcd_.__dict__) | globals()
_abcd_globals_ = dict(_abcd_.__dict__)
_abcd_globals_ |= (_numbers_abcd_.__dict__ | _collections_abcd_.__dict__)
tuple(map(_abcd_globals_.pop, ["__all__", "modulefunc", "modulefuncs"]))
_abcd_globals_ |= {"MathDomainTypes": MathDomainTypes} | {k: eval(k) for k in _domainnicknames}
_abcd_.__dict__.update(_abcd_globals_)
globals().update(_abcd_globals_)
del _abcd_globals_


#print("GLOBALS:", *_abcd_globals_.items(), sep=", \n    ")


NonFinite.register(type(None))
NonFinite.register(type(NotImplemented))
NonFinite.register(ArithmeticError)


Object.register(object)
Bool.register(bool)


Complex.register(complex)
Real.register(float)
Integral.register(int)
Lattice.register(Integral)


Coroutine.register(coroutine)
AsyncGenerator.register(async_generator)

Iterator.register(bytes_iterator)
Iterator.register(bytearray_iterator)
#Iterator.register(callable_iterator)
Iterator.register(dict_keyiterator)
Iterator.register(dict_valueiterator)
Iterator.register(dict_itemiterator)
Iterator.register(list_iterator)
Iterator.register(list_reverseiterator)
Iterator.register(range_iterator)
Iterator.register(longrange_iterator)
Iterator.register(set_iterator)
Iterator.register(str_iterator)
Iterator.register(tuple_iterator)
Iterator.register(zip_iterator)

Generator.register(generator)


Set.register(frozenset)
Set.register(ABCDMeta)
Lattice.register(Set)

MutableSet.register(set)

Mapping.register(mappingproxy)
Mapping.register(FrameLocalsProxy)

KeysView.register(dict_keys)
ItemsView.register(dict_items)
ValuesView.register(dict_values)

MutableMapping.register(dict)


Sequence.register(tuple)
Sequence.register(str)
Sequence.register(range)
Sequence.register(memoryview)

Stringlike.register(str)
Stringlike.register(bytes)
Stringlike.register(bytearray)

MutableSequence.register(list)
MutableSequence.register(bytearray)  # Multiply inheriting, see ByteString




try:
    import gmpy2 as _gmpy2
except ImportError:
    _gmpy2 = None
try:
    import mpmath as _mpm
except ImportError:
    _mpm = None
try:
    import numpy as _np
except ImportError:
    _np = None

if _gmpy2 is not None:
    Integral.register(_gmpy2.mpz)
    Rational.register(_gmpy2.mpq)
    Real.register(_gmpy2.mpfr)
    Complex.register(_gmpy2.mpc)
if _mpm is not None:
    Real.register(_mpm.mpf)
    Complex.register(_mpm.mpc)
if _np is not None:
    Bool.register(_np.bool_)
    Natural.register(_np.unsignedinteger)
    Integral.register(_np.integer)
    Real.register(_np.floating)
    Complex.register(_np.inexact)
    Number.register(_np.number)
    Stringlike.register(_np.str_)
    Vector.register(_np.ndarray)
    assert issubclass(_np.bool_, Bool)
    assert issubclass(_np.unsignedinteger, Natural)
    assert isinstance((_np.array([5]) != 7)[0], Bool)
    assert isinstance(_np.array([5], dtype='I')[0], Natural)

del _gmpy2, _mpm, _np


#def _get_mro(T):
#    try:  return ABCDMetaꓸmro(T)
#    except TypeError:
#        if isinstance(T, GenericAlias):  return ABCDMetaꓸmro(T.__origin__)
#        elif isinstance(T, TypeUnion):  return list(chain.from_iterable(map(_get_mro, T.__args__)))
#        raise
#@modulefunc
#def _mro_len(T):
#    return len(_get_mro(T))
#_mro_len=None


if __name__ == '__main__':
    
    print('\n\n\n')
    print(f"\n{issubclass(bool, Complex) = }")
    
    print()
    print(''.join(c*2 for c in "\n-=ᐨⲷˍᐨꘌᐨˍˉⲶˉˍᐨꘌ-ᐨⲷᐨˍⲷᐨꘌ-\n"))
    print(f"    {Ⲉƒx.__qualname__ = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] < ⲈFᴄ[[ⲈOʙ], Auto]) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] > ⲈFᴄ[[ⲈOʙ], Auto]) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] <= ⲈFᴄ[[ⲈOʙ], Auto]) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] >= ⲈFᴄ[[ⲈOʙ], Auto]) = }")
    print()
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] < ⲈFᴄ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] > ⲈFᴄ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] <= ⲈFᴄ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] >= ⲈFᴄ) = }")
    print()
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] < ⲈLᴛ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] > ⲈLᴛ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] <= ⲈLᴛ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] >= ⲈLᴛ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] >= ⲈFᴄ) = }")
    print()
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] < ⲈOʙ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] > ⲈOʙ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] <= ⲈOʙ) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] >= ⲈOʙ) = }")
    print()
    print()
    T = deduce_domain(5)
    print(f"    {(5 in ⲈCᴛ) = }    ")
    print(f"    {T = }    {type(T) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] < T) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] > T) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] <= T) = }")
    print(f"{(ⲈFᴄ[[ⲈOʙ], Ⲉǃǃ] >= T) = }")
    print()
    T = ⲈCᴛ
    S = T | Ⲉǃǃ
    assert isinstance(S, _ABCD_SetStructure_Base), (type(S), _ABCD_SetStructure_Base)
    T = deduce_domain(T)
    S = deduce_domain(S)
    print(f"    {T = }    ")
    print(f"    {S = }    ")
    print(f"{(S < T) = }")
    print(f"{(S > T) = }")
    print(f"{(S <= T) = }")
    print(f"{(S >= T) = }")
    print()
    T = ⲈCᴛ
    S = ⲈCᴛ - ⲈSવ
    T = Ⲉⵁ
    T = deduce_domain(T)
    S = deduce_domain(S)
    assert isinstance(S, _ABCD_SetStructure_Base), (type(S), _ABCD_SetStructure_Base)
    print(f"    {T = }    ")
    print(f"    {S = }    ")
    print(f"{(S < T) = }")
    print(f"{(S > T) = }")
    print(f"{(S <= T) = }")
    print(f"{(S >= T) = }")
    print(f"{({1} in S) = }")
    print(f"{((1,) in S) = }")
    print()
    
    T = ⲈCᴛ
    S = ⲈCᴛ | Auto[2]
    print(f"    {T = }    ")
    print(f"    {S = }    ")
    print(f"{(S < T) = }")
    print(f"{(S > T) = }")
    print(f"{(S <= T) = }")
    print(f"{(S >= T) = }")
    print(f"{({1} in S) = }")
    print(f"{((1,) in S) = }")
    print()
    
    
    print("\n\n")
    exit()

