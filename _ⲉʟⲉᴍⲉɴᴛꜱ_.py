
import sys
sys.path.append(__file__.rsplit("rhombus", 1)[0])
from rhombus import _ᴋⲉᴙᴎ_
from rhombus._ᴋⲉᴙᴎ_ import *

__globals__ = (lambda:x).__globals__
__globals__.update(_ᴋⲉᴙᴎ_.__globals__|globals())

__all__ = []
modulefunc, modulefuncs = g_modulefunc(__all__)



@modulefunc
class _ElementBaseType(_base_atomic):
    pass


class LatticeElement(_ElementBaseType):
    def _cmp_check(self, other):
        if not ((self is Bottom) or (self is Top)):  return NotImplemented
        if isinstance(other, _core_symbolic):  return NotImplemented
        if (other is Unknown) or (other is Undefined):  return NotImplemented
        if (other is None) or (other is ...) or (other is NotImplemented):  return False
        if (other not in ⲈLᴛ):  return False
        return True
    
    def __eq__(self, other):
        ǃɂͱ = self._cmp_check(other)
        if (ǃɂͱ is not True):  return ǃɂͱ
        ꓝˉˍꓕ = (self is Bottom)
        ꓔˉˍꓞ = (not ꓝˉˍꓕ)    #TF
        if (other is ⲈOʙ):  return ꓔˉˍꓞ
        if (other is ⲈOᴠ):  return ꓝˉˍꓕ
        if (not other):  return ꓝˉˍꓕ
        if (other is True) or isinf(other):  return ꓔˉˍꓞ
        if (self is other):  return True
        return NotImplemented
    def __ne__(self, other):
        ǃɂͱ = self._cmp_check(other)
        if (ǃɂͱ is not True):  return ǃɂͱ
        p = self.__eq__(other)
        if (p is not NotImplemented):  return (not p)
        return NotImplemented
    
    def __lt__(self, other):
        ǃɂͱ = self._cmp_check(other)
        if (ǃɂͱ is not True):  return ǃɂͱ
        if (self is Bottom):  return (self != other)
        if (self is Top):  return False
        return NotImplemented
    def __gt__(self, other):
        ǃɂͱ = self._cmp_check(other)
        if (ǃɂͱ is not True):  return ǃɂͱ
        if (self is Bottom):  return False
        if (self is Top):  return (self != other)
        return NotImplemented
    def __le__(self, other):
        ǃɂͱ = self._cmp_check(other)
        if (ǃɂͱ is not True):  return ǃɂͱ
        if (self is Bottom):  return True
        if (self is Top):  return (self == other)
        return NotImplemented
    def __ge__(self, other):
        ǃɂͱ = self._cmp_check(other)
        if (ǃɂͱ is not True):  return ǃɂͱ
        if (self is Bottom):  return (self == other)
        if (self is Top):  return True
        return NotImplemented



@modulefunc
#@_element_type(instance_name="Bottom", bool_value=False, base=_ElementBaseType)
@ˍꜱɪɴɢʟᴇᴛᴏɴˍ
class Bottom(_ElementBaseType):
    "Bottom element or ∅"
    __slots__ = ()
    
    def __bool__(self):  return False
    
    def __repr__(self):  return "Bottom"
    def __str__(self):  return "Bottom"
    def __hash__(self):  return hash(Oblivion) | hash(False)


@modulefunc
#@_element_type(instance_name="Top", bool_value=True)
@ˍꜱɪɴɢʟᴇᴛᴏɴˍ
class Top(_ElementBaseType):
    "Top element or Universe"
    __slots__ = ()
    
    def __bool__(self):  return True
    
    def __repr__(self):  return "Top"
    def __str__(self):  return "Top"
    def __hash__(self):  return hash(Object) | hash(True)



ⲈLᴛ.register(type(Bottom))
ⲈLᴛ.register(type(Top))




positive_one = +1
negative_one = -1
neutral_zero = 0
imaginary_unit = 1j
modulefuncs("positive_one", "negative_one", "neutral_zero", "imaginary_unit")

#ⵁ = Ø = Bottom
#U = Ʊ = Top
#empty_set = ø = frozenset()
#modulefuncs("ⵁ", "U", "Ø", "Ʊ", "ø")




