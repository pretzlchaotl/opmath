
import sys
from _typing import _idfunc
from _collections import _tuplegetter, defaultdict
from _operator import attrgetter as _attrgetter, itemgetter as _itemgetter
from functools import lru_cache as _lru_cache, partial, partialmethod
from itertools import filterfalse, chain, count
from more_itertools import unique_everseen
from math import floor, ceil, trunc, inf, nan, isinf as _isinf, isfinite as _isfinite
import builtins, operator, math

sys.path.append(__file__.rsplit("rhombus", 1)[0])
from futilities.aliases import *
from futilities.miscellaneous_debris import (
    sovereign, rename_function, 
    get_name, get_name_or_str, DefaultObject, singleton_registry, singleton_type, g_constfunc, 
    hashproperty, classproperty, 
    )
from futilities.syntax_tricks import infix
from rhombus import constants

__globals__ = (lambda:x).__globals__
__globals__.update(constants.__globals__|globals())

__all__ = [] + constants.__all__
modulefunc, modulefuncs = g_modulefunc(__all__)


ꓽFalse = constants._ꓽF[Ⲉǃǃ]#.value
ꓽTrue = constants._ꓽT[Ⲉǃǃ]#.value


{ ( (  (   (      ((("    ⲉ    ǂ    Ⲉ    ᑕ    ⵁ    ꕺ    ⵁ    ꕺ    ⵁ    ꕺ    ⵁ    ᑐ    Ⰵ    ǂ    ⰵ    ")))      )   )  ) ) }


_W = opvar("ꓽW", domain=ⲈOᴠ)
_X = opvar("ꓽX", domain=ⲈOᴠ)
_Y = opvar("ꓽY", domain=ⲈOᴠ)
_Z = opvar("ꓽZ", domain=ⲈOᴠ)


modulefuncs(
    "_W", "_X", "_Y", "_Z", 
    )




ꘌꘌ = infix([opfunc._instances[("==")]])
ǃꘌ = infix([opfunc._instances[("!=")]])

ͱ· = infix([opfunc._instances[("ͱ|")]])
ⲳ· = infix([opfunc._instances[("ⲳ|")]])

ꕺꓽ = infix([opfunc._instances[("|ꕺ|")]])
ꔷꓽ = infix([opfunc._instances[("|ꔷ|")]])

ͱ, ⲳ, ꕺ, ꔷ = ͱ·, ⲳ·, ꕺꓽ,  ꔷꓽ

modulefuncs('ͱ·',  'ⲳ·',  'ꕺꓽ', 'ꔷꓽ')
modulefuncs('ͱ',  'ⲳ',  'ꕺ', 'ꔷ')
modulefuncs(
    "ꘌꘌ", "ǃꘌ", 
    )

#    ·    ꙩꙭоꚙ    Ꞌᒾᶟ

#ɂᓒᣙ
#ꔧꕹꗬꘉ
#ͱⲳᐞⴰ
#ꕺꔷᛜⵙⴱⴲⵀꕕ

"""
ⲶⲷⲼⲽⲾⲿ ͰⲲ ͱⲳᐞ ꟷⲺⲻⳆⳇꤷ 
ⳘⳙⳞⳟ ϵⲈⲉⰅⰵ ᑐᑕᐳᐸᑌᑎⴸⴷᐁᐃ ⵠⴹⴺ 
ⵝⴻꖅⵜⵧ ⵃⵀⵁⵙⴱⴲ ⴲꚚꚛꕕ ⵙꖴꕺ ϴ ꝊꝋꝎꝏ ꙨꙩꙪꙫꙬꙭ    _·ººೲཿᐝᐤᐧᛜᣞᣟᯪⴰⴱⴲⵀⵁⵙꔮꔷꕕꕺꖴꗝꗞꞏ
 · ꞏ ꔷ ꔸ ⴰ ꔧ ꕹ ꗬ ꘉ ᛜ ⵙꖴꕺ
ᛜⴱⴲⵀⵁⵙꔮꔷꕕꕺꖴꗝꗞꞏ
 ᐡᐢᐣᒼᐞᘁᣔᑉᱼᐨᕀᐩᕁᕽᐠᐟᐥᐦᙾᑊᙿ ᐪᗮ  ᓒᣙ ᒃᒄᣖᓐ ᒡᒢᣗᓪ ᒻᒽᣘᔈ ᒾ ᕯ 
"""



"    ( Ⲉ Ⲷ  Ⲷ Ⲷ  ᑕ  [( { Standard Python Arithmetic } )]  ᑐ  Ⲷ Ⲷ  Ⲷ Ⰵ  )"

ⲈꘌⰅ = ⲈOʙ

_W = _W[ⲈꘌⰅ]
_X = _X[ⲈꘌⰅ]
_Y = _Y[ⲈꘌⰅ]
_Z = _Z[ⲈꘌⰅ]

assert (_X.domain is ⲈOʙ)

propertiesref_py_ops = {
    (~~_X): (_X), 
    
    (+_X): (_X), 
    
    -(-_X): (_X),      -(+_X): (-_X),      (-_X)**-1: -(_X**-1), 
    
    (_X**-1)**-1: (_X), 
    
    (_X | _X): (_X), 
    (_X & _X): (_X), 
    
#    (_X ^ _X): (_ꓽ0), 
    
    (_ꓽ0 + _X): (_X),      (_X + _ꓽ0): (_X),  
    
#    (_X - _X): (_ꓽ0), 
    (_ꓽ0 - _X): (-_X),      (_X - _ꓽ0): (_X), 
    
    (_ꓽ0 * _X): (_ꓽ0),      (_X * _ꓽ0): (_ꓽ0),  
    (_ꓽ1 * _X): (_X),      (_X * _ꓽ1): (_X),  
    
#    (_X / _X): (_ꓽ1[_X.domain),  
#    (_ꓽ0[_ꓽⲉA] / _X[_ꓽⲉA]): (_ꓽ0[_ꓽⲉA]),      #(_X / _ꓽ0): (_ꓽꭒɲᶑꬲꝼ),  
    (_ꓽ1 / _X): (_X**-1),      (_X / _ꓽ1): (_X),  
    
#    (_X // _X): (_ꓽ1),  
#    (_ꓽ0 // _X): (_ꓽ0),      #(_X // _ꓽ0): (_ꓽꭒɲᶑꬲꝼ),  
#    
#    (_X % _X): (_ꓽ0), 
#    (_ꓽ0 % _X): (_ꓽ0),     #(_X % _ꓽ0): (_ꓽꭒɲᶑꬲꝼ), 
#    
#    (_ꓽ0 ** _X): (_ꓽ0),      (_X ** _ꓽ0): (_ꓽ1), #[_X.domain]),  
#    (_ꓽ1 ** _X): (_ꓽ1),      (_X ** _ꓽ1): (_X),  
    #(_ꓽ0 ** -_X): (_ꓽꭒɲᶑꬲꝼ), 
}


simplify_py_ops = apply_rewrites_matchrewrite(propertiesref_py_ops)

modulefuncs(
    "propertiesref_py_ops", "simplify_py_ops", 
    )


#canonref_Undefined_behavior = {
#    (+_ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),      (-_ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),      (_ꓽꭒɲᶑꬲꝼ**-1): (_ꓽꭒɲᶑꬲꝼ),      (~_ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),  
#    (_ꓽꭒɲᶑꬲꝼ + _X): (_ꓽꭒɲᶑꬲꝼ),      (_X + _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),  
#    (_ꓽꭒɲᶑꬲꝼ - _X): (_ꓽꭒɲᶑꬲꝼ),      (_X - _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ * _X): (_ꓽꭒɲᶑꬲꝼ),      (_X * _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ / _X): (_ꓽꭒɲᶑꬲꝼ),      (_X / _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ ** _X): (_ꓽꭒɲᶑꬲꝼ),      (_X ** _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ // _X): (_ꓽꭒɲᶑꬲꝼ),      (_X // _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ % _X): (_ꓽꭒɲᶑꬲꝼ),      (_X % _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ | _X): (_ꓽꭒɲᶑꬲꝼ),      (_X | _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ & _X): (_ꓽꭒɲᶑꬲꝼ),      (_X & _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#    (_ꓽꭒɲᶑꬲꝼ ^ _X): (_ꓽꭒɲᶑꬲꝼ),      (_X ^ _ꓽꭒɲᶑꬲꝼ): (_ꓽꭒɲᶑꬲꝼ),
#}
#modulefunc("canonref_Undefined_behavior")



ⲈꘌⰅ = ⲈUɴ

_W = _W[ⲈꘌⰅ]
_X = _X[ⲈꘌⰅ]
_Y = _Y[ⲈꘌⰅ]
_Z = _Z[ⲈꘌⰅ]

assert (_X.domain is ⲈUɴ)



propertiesref_py_ops_numeric = {
    (+_X): (_X), 
    
    -(-_X): (_X),      -(+_X): (-_X),      (-_X)**-1: -(_X**-1), 
    (-_ꓽ0): (_ꓽ0), 
    
    (_X**-1)**-1: (_X), 
    
    
    (_ꓽ0 + _X): (_X),      (_X + _ꓽ0): (_X),  
    
    (_X - _X): (_ꓽ0), 
    (_ꓽ0 - _X): (-_X),      (_X - _ꓽ0): (_X), 
    
      
    (_ꓽ0 * _X): (_ꓽ0),      (_X * _ꓽ0): (_ꓽ0),  
    (_ꓽ1 * _X): (_X),      (_X * _ꓽ1): (_X),  
    
    (_X / _X): (_ꓽ1),  
    (_ꓽ0 / _X): (_ꓽ0),      #(_X / _ꓽ0): (_ꓽꭒɲᶑꬲꝼ),  
    (_ꓽ1 / _X): (_X**-1),      (_X / _ꓽ1): (_X),  
    
    
    (_X // _X): (_ꓽ1),  
    (_ꓽ0 // _X): (_ꓽ0),      #(_X // _ꓽ0): (_ꓽꭒɲᶑꬲꝼ),  
    
    (_X % _X): (_ꓽ0), 
    (_ꓽ0 % _X): (_ꓽ0),     #(_X % _ꓽ0): (_ꓽꭒɲᶑꬲꝼ), 
    
    
    (_ꓽ0 ** _X): (_ꓽ0),      (_X ** _ꓽ0): (_ꓽ1),  
    (_ꓽ1 ** _X): (_ꓽ1),      (_X ** _ꓽ1): (_X),  
    #(_ꓽ0 ** -_X): (_ꓽꭒɲᶑꬲꝼ), 
}


canonref_py_ops_numeric = propertiesref_py_ops_numeric | {
    (_X.__floor__()): (_X // _ꓽ1), 
    (_X.__ceil__()): -(_X // -_ꓽ1),  
#    (_X.__trunc__()): (_X // _ꓽ1), 
    
    (_X + _X): (_X*2),      #(_X + -_X): (_ꓽ0),  
    (_X + -_Y): (_X - _Y),      (-_X + _Y): (_Y - _X),  
    
    #(_ꓽ1 - _X)[(_ꓽ0 <= _X <= 1)]: (...
    (_X - -_Y): (_X + _Y),      (-_X - _Y): (_Y + _X),  
    
    (_X - _Y - _Z): (_X - (_Y + _Z)),  
    
    
    (_X * _X): (_X**2),  
    (_X * _Y**-1): (_X / _Y),      (_X**-1 * _Y): (_Y / _X),  
    
    (_X / _Y / _Z): (_X / (_Y * _Z)),  
    
    
#    (_X // _ꓽ1): (_X.__floor__()), 
#    -(_X // -_ꓽ1): (_X.__ceil__()),  
    
#    (_X % _ꓽ1): (_X - _X.__floor__()), 
#    (_X % _ꓽᐨ1): -(_X - _X.__ceil__()),  
    
    (_X ** _ꓽᐨ1): (_X**-1),      #(_X ** -_Y): ((_X**_Y)**-1), 
    
}



identities_ref_py_ops_numeric = [
   (_X + _Y) |ꘌꘌ| (_Y +_X),    ((_X + _Y) + _Z) |ꘌꘌ| (_X + (_Y + _Z)), 
   (_X - _Y) |ꘌꘌ| (_X +-_Y), 
   (_X * _Y) |ꘌꘌ| (_Y *_X),    ((_X * _Y) * _Z) |ꘌꘌ| (_X * (_Y * _Z)), 
   (_X / _Y) |ꘌꘌ| (_X * _Y**-1), 
]


simplify_pynumeric = apply_rewrites_matchrewrite(propertiesref_py_ops_numeric)
canonize_pynumeric = apply_rewrites_matchrewrite(canonref_py_ops_numeric)


modulefuncs(
    "propertiesref_py_ops_numeric", "canonref_py_ops_numeric", 
    "simplify_pynumeric", "canonize_pynumeric", 
    )

ⲈꘌⰅ = ⲈOʙ

_W = _W[ⲈꘌⰅ]
_X = _X[ⲈꘌⰅ]
_Y = _Y[ⲈꘌⰅ]
_Z = _Z[ⲈꘌⰅ]

assert (_X.domain is ⲈOʙ)





"    ( Ⲉ Ⲷ  Ⲷ Ⲷ  ᑕ  [( { Lattic/Setlike Structure } )]  ᑐ  Ⲷ Ⲷ  Ⲷ Ⰵ  )"


ⲈꘌⰅ = ⲈLᴛ

_W = _W[ⲈꘌⰅ]
_X = _X[ⲈꘌⰅ]
_Y = _Y[ⲈꘌⰅ]
_Z = _Z[ⲈꘌⰅ]

assert (_X.domain is ⲈLᴛ)



propertiesref_lattice_ops = {
    (~~_X): (_X), 
    (~_ꓽʟⵁ): (_ꓽʟU),             (~_ꓽʟU): (_ꓽʟⵁ), 
    
    
    (_X | _X): (_X), 
    (_X | _ꓽʟⵁ): (_X),         (_ꓽʟⵁ | _X): (_X), 
    (_X | _ꓽʟU): (_ꓽʟU),         (_ꓽʟU | _X): (_ꓽʟU), 
    (_X | ~_X): (_ꓽʟU),         (~_X | _X): (_ꓽʟU), 
    
    (_X & _X): (_X), 
    (_X & _ꓽʟⵁ): (_ꓽʟⵁ),         (_ꓽʟⵁ & _X): (_ꓽʟⵁ), 
    (_X & _ꓽʟU): (_X),         (_ꓽʟU & _X): (_X),
    (_X & ~_X): (_ꓽʟⵁ),         (~_X & _X): (_ꓽʟⵁ), 
    
    
    (_X ^ _X): (_ꓽʟⵁ), 
    (_X ^ _ꓽʟⵁ): (_X),         (_ꓽʟⵁ ^ _X): (_X), 
    (_X ^ _ꓽʟU): (~_X),         (_ꓽʟU ^ _X): (~_X),  
    
    
    (_Y[ⲈOʙ] - _Y[ⲈOʙ]): (_ꓽⵁ), 
#    (_Z[ⲈUɴ] - _Z[ⲈUɴ]): (_ꓽⵁ[ⲈUɴ]), 
#    (_X[ⲈLᴛ] - _X[ⲈLᴛ]): (_ꓽⵁ[ⲈLᴛ]), 
#    (_X[ⲈOʙ] - _X[ⲈOʙ]): (_ꓽⵁ), 
#    (_Y[ⲈLᴛ] - _Y[ⲈLᴛ]): (_ꓽʟⵁ), 
    (_Y - _Y): (_ꓽʟⵁ), 
#    (_X - _X): (_ꓽʟⵁ), 
    (_X - _ꓽʟⵁ): (_X),          (_ꓽʟⵁ - _X): (_ꓽʟⵁ), 
    (_X - _ꓽʟU): (_ꓽʟⵁ),         (_ꓽʟU - _X): (~_X), 
    (_X - ~_X): (_X),         (~_X - _X): (~_X), 
    
}

canonref_lattice_ops = {
    
    (~_X | ~_Y): ~(_X & _Y), 
    (~_X | _Y): (_Y | ~_X), 
    ~(_X | ~_Y): (_Y - _X),  
    
    
    (~_X & ~_Y): ~(_X | _Y), 
    (~_X & _Y): (_Y - _X),         (_X & ~_Y): (_X - _Y), 
    ~(~_X & _Y): (_X | ~_Y),          ~(_X & ~_Y): (_Y | ~_X), 
    
    
    (~_X - ~_Y): (_Y - _X), 
    (~_X - _Y): ~(_X |_Y),         #(_X - ~_Y): (_X & _Y), 
    ~(~_X - _Y): (_Y | _X), 
    ~(_X - _Y): (_Y | ~_X), 
    
    (_X | (_X | _Y)): (_X | _Y),     ((_X | _Y) | _X): (_X | _Y), 
    (_Y | (_X | _Y)): (_X | _Y),     ((_X | _Y) | _Y): (_X | _Y), 
    (_X & (_X & _Y)): (_X & _Y),     ((_X & _Y) & _X): (_X & _Y), 
    (_Y & (_X & _Y)): (_X & _Y),     ((_X & _Y) & _Y): (_X & _Y), 
    
#    ((_X | _Y) | _Z): (_X | (_Y | _Z)),
#    ((_X & _Y) & _Z): (_X & (_Y & _Z)), 
    
#    (_X | (_Y | _Z)): ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("|", _X, _Y,  _Z), 
#    ((_X | _Y) | _Z): ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("|", _X, _Y,  _Z), 
#    (_X & (_Y & _Z)): ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("&", _X, _Y,  _Z), 
#    ((_X & _Y) & _Z): ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("&", _X, _Y,  _Z), 
#    
#    (_X & (_Y | _Z)): ((_Y | _Z) & _X), 
    ((_X & _Y) | _X): (_X),     ((_X & _Y) | _Y): (_Y), 
    (_X | (_X & _Y)): (_X),     (_Y | (_X & _Y)): (_Y), 
    ((_X | _Y) & _X): (_X),     ((_X | _Y) & _Y): (_Y), 
    (_X & (_X | _Y)): (_X),     (_Y & (_X | _Y)): (_Y), 
    
    
#    (_X < (_X | _Y)):  AND_(_Y._ne_(_ꓽʟⵁ), _Y._ne_(_X)), 
#                                                              (_Y < (_X | _Y)):  AND_(_X._ne_(_ꓽʟⵁ), _X._ne_(_Y)), 
#                                                              (_Y < (_X | _Y)):  (_ꓽʟⵁ != _X != _Y), \
    _X <= _Y:  _X & _Y |ꘌꘌ| _X, 
    _X <= _Y:  _X | _Y |ꘌꘌ| _Y, 
    _X <= _Y:  ~_Y <= ~_X, 
    _X <= _Y:  _X - _Y |ꘌꘌ| _ꓽʟⵁ, 
    
    _X & _Y |ꘌꘌ| _ꓽʟⵁ:  _Y - _X |ꘌꘌ| _Y, 
        
    (_X <= (_X | _Y)):  ꓽTrue,         (_Y <= (_X | _Y)):  ꓽTrue, 
    (_X >= (_X | _Y)):  ꓽFalse,         (_Y >= (_X | _Y)):  ꓽFalse, 
    (_X <= (_X & _Y)):  ꓽFalse,         (_Y <= (_X & _Y)):  ꓽFalse, 
    (_X >= (_X & _Y)):  ꓽTrue,         (_Y >= (_X & _Y)):  ꓽTrue, 
    
    (_X < (_X | _Y)):  (_X |ǃꘌ| (_X | _Y)),         (_Y < (_X | _Y)):  (_Y |ǃꘌ| (_X | _Y)), 
    (_X > (_X | _Y)):  ꓽFalse,         (_Y > (_X | _Y)):  ꓽFalse, 
    (_X < (_X & _Y)):  ꓽFalse,         (_Y < (_X & _Y)):  ꓽFalse, 
    (_X > (_X & _Y)):  (_X |ǃꘌ| _Y),         (_Y > (_X & _Y)):  (_X |ǃꘌ| _Y), 
    
}
{
#    (_X & (_Y | _Z)) : ((_X & _Y) | (_X & _Z)), 
#    (_X | (_Y & _Z)) : ((_X | _Y) & (_X | _Z)), 
    ((_X & _Y) | (_X & _Z)) : (_X & (_Y | _Z)), 
#    ((_X | _Y) & (_X | _Z)) : (_X | (_Y & _Z)), 
}

#propertiesref_lattice_ops = canonref_lattice_ops = {
#    (_X - _X): (_ꓽᴘⵁ), }


"""

(a|b|c) - (b|d|e) |ꘌꘌ| (c)
(a,b,c) ^ (b,d,e) |ꘌꘌ| (c,e)
(a,b,c) & (b,d,e) |ꘌꘌ| (b)
(a,b,c) | (b,d,e) |ꘌꘌ| (a,b,c,d,e)
#z | (y - x) |ꘌꘌ| ((y | z) - (x - z))
~(a,b,c) | (b,d,e) |ꘌꘌ| (b,d,e) | (_ꓽʟU - (a,b,c)) |ꘌꘌ| (_ꓽʟU | (b,d,e)) - ((a,b,c) - (b,d,e)) |ꘌꘌ| _ꓽʟU - ((a,b,c) - (b,d,e)) |ꘌꘌ| ~(c)
#z & (x - y) |ꘌꘌ| (x & z) - y |ꘌꘌ| (z - y) & x
(a,b,c) & ~(b,d,e) |ꘌꘌ| (a,b,c) & (_ꓽʟU - (b,d,e)) |ꘌꘌ| _ꓽʟU & ((a,b,c) - (b,d,e)) |ꘌꘌ| (c)
~((a,b,c) - (b,d,e)) |ꘌꘌ| ~(c)
 |ꘌꘌ| (b,d,e) | ~(a,b,c) |ꘌꘌ| _ꓽʟU - (c)
"""

identities_ref_lattice_ops = [
    (_Z - (_X & _Y)) |ꘌꘌ| ((_Z - _X) | (_Z - _Y)), 
    (_Z - (_X | _Y)) |ꘌꘌ| ((_Z - _X) & (_Z - _Y)), 
    (_Z - (_Y - _X)) |ꘌꘌ| ((_X & _Z)|(_Z - _Y)), 
    
    ((_Y - _X) & _Z) |ꘌꘌ| ((_Y & _Z) - _X),  
                                        ((_Y & _Z) - _X) |ꘌꘌ| (_Y & (_Z - _X)), 
                                                                            (_Y & (_Z - _X)) |ꘌꘌ| ((_Y - _X) & _Z), 
    
#    (_Y - _X) | _Z |ꘌꘌ| (_Y | _Z) - (_X ??_Z), 
    ((_Y - _X) - _Z) |ꘌꘌ| (_Y - (_X | _Z)), 
    (_X - _X) |ꘌꘌ| ( _ꓽʟⵁ), 
    (_ꓽʟⵁ - _X) |ꘌꘌ| (_ꓽʟⵁ), 
    #_X - _ꓽʟⵁ |ꘌꘌ| _X), 
    #_Y - _X |ꘌꘌ| ~_X & _Y),  #|ꘌꘌ| _RNIMPLY_(_X, _Y) |ꘌꘌ| _NIMPLY_(_Y, _X), 
    (~(_Y - _X)) |ꘌꘌ| (_X | ~_Y), #|ꘌꘌ| _RIMPLY_(_X, _Y)) |ꘌꘌ| (_IMPLY_(_Y, _X), 
    (_ꓽʟU - _X) |ꘌꘌ| ( ~_X), 
    (_X - _ꓽʟU) |ꘌꘌ| ( _ꓽʟⵁ), 
    
    #_X & _Y |ꘌꘌ| _Y & _X, 
    #(_X | _Y |ꘌꘌ| _Y | _X), 
    #(_X | (_X & _Y) |ꘌꘌ| _X), 
    #(_X & (_X | _Y) |ꘌꘌ| _X), 
    #((_X | _Y) - _X |ꘌꘌ| (_Y - _X)), 
    #(~(~_X | _Y) | ~(~_X | ~_Y) |ꘌꘌ| (_X)), 
    ((_X & _Y) & _Z) |ꘌꘌ| (_X & (_Y & _Z)), 
    ((_X | _Y) | _Z) |ꘌꘌ| (_X | (_Y | _Z)), 
    (_Z - (_X & _Y)) |ꘌꘌ| ((_Z - _X) | (_Z - _Y)), 
    (_Z - (_X | _Y)) |ꘌꘌ| ((_Z - _X) & (_Z - _Y)), 
    (_Z - (_Y - _X)) |ꘌꘌ| ( (_Z - _Y) |(_Z & _X)), 
    ((_Y - _X) & _Z) |ꘌꘌ| ((_Y & _Z) - _X), 
    
    ((_Y & _Z) - _X) |ꘌꘌ| (_Y & (_Z - _X)), 
                                        (_Y & (_Z - _X))|ꘌꘌ|((_Y - _X) & _Z), 
                                                                           ((_Y - _X) | _Z) |ꘌꘌ| ((_Y | _Z) - (_X - _Z)), 
    
#    (_X & (_Y | _Z)) |ꘌꘌ| ((_X & _Y) | (_X & _Z)), 
#    (_X | (_Y & _Z)) |ꘌꘌ| ((_X | _Y) & (_X | _Z)), 
]

"""
~x  ==  -x − 1
~-x  ==  x + 1
-~x  ==  x − 1
(((('    BOOLEAN IDENTITIES    '))))
    'NOT ( ¬ \\ ~ ) invert
~x  ==  -x − 1
    ~-x  ==  x − 1
-~x  ==  x + 1
x  == ~(-x − 1)
~-x + 1 == x
-~x − 1 == x
~x  ==  -x − 1
~(~x)  ==  x
    'AND ( ∧ \\ & )
x & y  ==  y & x            # commutatative
x & (y & z)  ==  (x & y) & z    # 
x & 0xFFFF  ==  x     # congruency under modulo ?
x & 0  ==  0        # absorption
x & 1  ==  x        # identity
x & x  ==  x        # idempotence
    'OR ( ∨ \\ | )
x | y  ==  y | x            # commutatative
x | (y | z)  ==  (x | y) | z    # associative
x | 0xFFFF  ==  0xFFFF    # absorption under modulo ?
x | 1  ==  1    # absorption
x | 0  ==  x    # identity
x | x  ==  x    # idempotence
    'XOR ( ⊻ \\ ^ )
x ^ y ; ==  y ^ x        # commutatative
x ^ (y ^ z)  ==  (x ^ y) ^ z    # associative
x ^ 0xFFFF  ==  ~x % 0x10000    # congruency under modulo ?
x ^ 0  ==  x        # identity
x ^ y ^ y  ==  x    #  ↱ ↳ 
x ^ x  ==  0        #  non-idempotent ?
    '''Additionally, XOR can be composed using
     the 3 basic operations (AND, OR, NOT)'''
a ^ b  ==  (a | b) & (~a | ~b)  ==  (a | b) & ~(a & b)
a ^ b  ==  (a & ~b) | (~a & b)  ==  ()
    'NAND ( ⊼ \\ )
x ⊼ y  ==  y ⊼ x            # commutatative
x ⊼ (y ⊼ z)  ==  (x ⊼ y) ⊼ z    # associative
x ⊼ 0  ==  1        # inverse absorption
x ⊼ 1  ==  ¬x        # inverse identity
x ⊼ x  ==  ¬x        # inverse idempotence
    'NOR ( ⊽ \\ )
x ⊽ y  ==  y ⊻ x            # commutatative
x ⊽ (y ⊽ z)  ==  (x ⊽ y) ⊽ z    # associative
x ⊽ 1  ==  0    # inverse absorption
x ⊽ 0  ==  ¬x    # inverse identity
x ⊽ x  ==  ¬x    # inverse idempotence
    'XNOR ( ⊽᤻ \\ )
x ⊽᤻ y  ==  y ⊽᤻ x        # commutatative
x ⊽᤻ (y ⊽᤻ z)  ==  (x ⊽᤻ y) ⊽᤻ z    # associative
x ⊽᤻ 1  ==  x        # identity
x ⊽᤻ y ⊽᤻ y  ==   # 
x ⊽᤻ x  ==  1        #  non-idempotent ?

    'others
x | (x & y)  ==  x        # complement
x & (x | y)  ==  x        # complement
~(x | y)  ==  ~x & ~y        # complement
~(x & y)  ==  ~x | ~y        # complement
x | (y & z)  ==  (x | y) & (x | z)    # distributive
x & (y | z)  ==  (x & y) | (x & z)    # distributive
x & (y ^ z)  ==  (x & y) ^ (x & z)    # distributive
"Arithmetic"
x + y  ==  (x ^ y) + ((x & y) << 1)
x - y  ==  ~(~x + y)
x << y  ==  x * 2**y
x >> y  ==  x // 2**y
x << 1 = x * 2
x >> 2 = x // 2
1 << x == 2**x
[*] 1 >> x == 1 / 2**x == 2**-x
(1 >> x  ==  x>0 ? 0 : 1)
"""

rewriters_lattice_identities = identities_ref_lattice_ops \
    + list(filterfalse(identities_ref_lattice_ops.__contains__, \
    [pⲷq.commutate() for pⲷq in identities_ref_lattice_ops]))
rewriters_lattice_identities = \
    [pⲷq.get_rewriter(cmp_matchtransform) for pⲷq in rewriters_lattice_identities]


canonref_lattice_ops = propertiesref_lattice_ops | canonref_lattice_ops

simplify_lattice_ops = apply_rewrites_matchrewrite(propertiesref_lattice_ops)
canonize_lattice_ops = apply_rewrites_matchrewrite(canonref_lattice_ops)


modulefuncs(
    "canonref_lattice_ops", "propertiesref_lattice_ops", 
    "canonize_lattice_ops", "simplify_lattice_ops", 
    "identities_ref_lattice_ops", "rewriters_lattice_identities", 
    )


ⲈꘌⰅ = ⲈOʙ

_W = _W[ⲈꘌⰅ]
_X = _X[ⲈꘌⰅ]
_Y = _Y[ⲈꘌⰅ]
_Z = _Z[ⲈꘌⰅ]

assert (_X.domain is ⲈOʙ)



def _troubleshoot_typed_ref_expression_operands_domains():
    assert (_ꓽʟⵁ.domain is ⲈLᴛ)
    assert (_ꓽʟU.domain is ⲈLᴛ)
    assert (_ꓽⵁ.domain is ⲈOʙ), _ꓽⵁ.domain
    assert (_ꓽU.domain is ⲈOʙ)
    assert (_ꓽᴘⵁ.domain is ⲈSᴘ)
    assert (_ꓽᴘU.domain is ⲈSᴘ)
    assert (_ꓽⲉⵁ.domain is ⲈCᴛ)
    assert (_ꓽⲉU.domain is ⲈCᴛ)
    assert (_ꓽF.domain is Ⲉǃǃ)
    assert (_ꓽT.domain is Ⲉǃǃ)
    
    ref = propertiesref_lattice_ops | canonref_lattice_ops
    dom = ⲈLᴛ
    ref = propertiesref_py_ops | canonref_py_ops_numeric
    dom = ⲈUɴ
    for _patt, _rwrt in ref.items():
        print("    ╠╝╔╝⠀╔╝⠀⠀╔╝⠀⠀⠀║⠀⠀⠀⠀ⵌ⠀⠀⠀⠀║⠀⠀⠀╚╗⠀⠀╚╗⠀╚╗╚╣")
        print("    ╚═╩══╩═══╩════╝⠀⠀⠀╚═╝⠀⠀⠀╚════╩═══╩══╩═╝")
        allgood = True
        for p in _patt.operands:
            pdom = get_domain(p)
            if (pdom is not dom):
                allgood = False
                print(f"            {p=};    {pdom=};")
        print(f"{'❌✅'[allgood]}    {_patt = }")
        allgood = True
        for q in _rwrt.operands:
            qdom = get_domain(q)
            if (qdom is not dom):
                allgood = False
                print(f"            {q=};    {qdom=};")
        print(f"{'❌✅'[allgood]}    {_rwrt = }")
        print("    ╔═╦══╦═══╦════╗⠀⠀⠀╔═╗⠀⠀⠀╔════╦═══╦══╦═╗")
        print("    ╠╗╚╗⠀╚╗⠀⠀╚╗⠀⠀⠀║⠀⠀⠀⠀ⵌ⠀⠀⠀⠀║⠀⠀⠀╔╝⠀⠀╔╝⠀╔╝╔╣")
        
    exit()

