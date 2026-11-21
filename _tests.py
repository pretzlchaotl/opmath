
import sys, os
from _typing import _idfunc
from _collections import _tuplegetter, defaultdict
from _operator import attrgetter as _attrgetter, itemgetter as _itemgetter
from functools import lru_cache as _lru_cache, partial, partialmethod
from itertools import filterfalse, chain
from more_itertools import unique_everseen, nth
from math import floor, ceil, trunc, inf, nan, isinf as _isinf, isfinite as _isfinite
import builtins, operator, math, cmath

sys.path.append(__file__.rsplit("rhombus", 1)[0])
sys.path.append("/storage/emulated/0/Documents/Pydroid3/pythonstuff/distrib/")
from futilities.aliases import *
from futilities.miscellaneous_debris import (
    sovereign, rename_function, 
    get_name, get_name_or_str, DefaultObject, singleton_registry, singleton_type, g_constfunc, 
    hashproperty, classproperty, 
    )
from futilities.syntax_tricks import *
from abcd._collections_abcd_ import Hashable
from rhombus import rho as __ꕺ__
#from __ꕺ__.util.optimize import logfunc_print_logs, logfunc_compile_logs, logfunc


__globals__ = (lambda:x).__globals__
__globals__.update(__ꕺ__.__globals__|globals())

__all__ = [] + __ꕺ__.__all__
modulefunc, modulefuncs = g_modulefunc(__all__)


__call__ = operator.__call__

simplify_canonical = apply_rewrites_matchrewrite


def _refget_(ref: dict, key: Hashable, default: object=None):
    try:  return ref[key]
    except KeyError:  return default
def _refsetdflt_(ref: dict, key: Hashable, default: object):
    try:  return ref[key]
    except KeyError:
        ref[key] = default
        return ref[key]


_cmp_ops_commutative = frozenset({'==', '!='})
_cmp_ops_reversible = ({'<=':'>=',  '>=':'<=',  '<':'>', '>':'<',     '==':'==', '!=':'!=', })
_cmp_ops_negatable = ({'==':'!=',  '!=':'==', })


@modulefunc
@sovereign(base=frozenset)
class ςʈ(frozenset):
    #def __repr__(self):  return frozenset.__repr__(self)
    def __getitem__(self, index: int):  return nth(iter(self), index)


frozet = ςʈ
# ʆƪ
#çϵȶ


Ø = frozet({})


@modulefunc
@sovereign(base=dict)
class proxyref(dict):
    def __getitem__(self, key):
        value = dict.__getitem__(self, key)
        try:  return value()
        except (TypeError, ValueError):  return value
    def setdefault(self, key, default):
        try:
            value = dict.__getitem__(self, key)
        except KeyError:
            dict.__setitem__(self, key, default)
            value = default
        try:  return value()
        except (TypeError, ValueError):  return value


@modulefunc
@sovereign(base=dict)
class relset(dict):
    __slots__ = ("_cmp_map",)
    _cmp_map: dict[str, ⲈSᴘ]
    cmp_ops: ⲈCᴛ[opfunc] = property(attrgetter('_cmp_map.keys'))
    expressions: ⲈCᴛ[opterm] = dict.keys
#    def __new__(cls, *ops: opfunc, vars: ⲈCᴛ[opvar]=None):
    def __new__(cls, *, cmp_op_keys: tuple[str]=None):  return dict.__new__(cls)
    def __init__(self, *, cmp_op_keys: tuple[str]=None):
        if (cmp_op_keys is None):
            cmp_op_keys = ('==', '!=', '<=', '>=')
        self._cmp_map = {sym: {} for sym in cmp_op_keys}
        #self._cmp_map = {sym: (fetchset() if (sym in _cmp_ops_commutative) else dict())
    get = _refget_
    setdefault = _refsetdflt_
    def add(self, predicate: oprelation):
        _cmp_map = self._cmp_map
        cmp, leftterm, rightterm = predicate[None]
        if (cmp not in _cmp_ops_commutative):
            submap: dict = _cmp_map[cmp]
            _refsetdflt_(submap, leftterm, set()).add(rightterm)
            cmp_right: str = _cmp_ops_reversible[cmp]
            _refsetdflt_(_cmp_map[cmp_right], rightterm, set()).add(leftterm)
        else:
            submap: dict = _cmp_map[cmp]
            union_update = {leftterm, rightterm}
            subsubmap: set = _refsetdflt_(submap, leftterm, union_update)
            subsubmap_right: set = _refsetdflt_(submap, rightterm, union_update)
            if (subsubmap is not union_update):
                subsubmap.update(union_update)
            if (subsubmap_right is not union_update):
                subsubmap_right.update(union_update)
            if (cmp == '==') and (subsubmap is not subsubmap_right):
                union_update = subsubmap | subsubmap_right
                _union = _diff = frozenset(union_update)
                while True:
                    for item in _difF:
                        itemmap = submap[item]
                        if itemmap is union_update:  continue
                        union_update.update(itemmap)
                        submap[item] = union_update
                    if _diff := (union_update - _union):
                        _union |= _diff
                    else:  break
    
    def getterm(self, term: opterm):
        try:  return self[term]
        except KeyError:
            self[term] = ({opkey: (lambda: submap[term])() \
                                    for opkey, submap in self._cmp_map.items() \
                                    if (term in submap)})
            return self[term]


def isdisjoint(p: ⲈLᴛ, q: ⲈLᴛ,*args):
    print(vars())
    try:  return p.isdisjoint(q)
    except AttributeError:  return _ꓽʟⵁ==(p & q)
def intersects_disjoint(p: ⲈLᴛ, q: ⲈLᴛ):
    return (not ((p<=q) or (p>=q) or (_ꓽʟⵁ==(p & q))))
def isdisjoint_supreme(p: ⲈLᴛ, q: ⲈLᴛ):
    return (not ((p<=q) or (p>=q)) and (_ꓽʟU==(p | q)))


def _isdisjoint_(p: ⲈLᴛ, q: ⲈLᴛ,*args):
    print(vars())
    try:  return p.isdisjoint(q)
    except AttributeError:  return _ꓽʟⵁ==(p & q)
def intersects_disjoint(p: ⲈLᴛ, q: ⲈLᴛ):
    return (not ((p<=q) or (p>=q) or (_ꓽʟⵁ==(p & q))))
def isdisjoint_supreme(p: ⲈLᴛ, q: ⲈLᴛ):
    return (not ((p<=q) or (p>=q)) and (_ꓽʟU==(p | q)))

isdisjoint.op = opfunc._from_raw('^ꘉ|', 2, 11, "{0} ^ꘉ| {1}", Ⲉǃǃ, (ⲈOʙ, ⲈOʙ), func=isdisjoint)
intersects_disjoint.op = opfunc._from_raw('&ᥤ//', 2, 11, "{0} &ᥤ// {1}", Ⲉǃǃ, (ⲈOʙ, ⲈOʙ), func=intersects_disjoint)
isdisjoint_supreme.op = opfunc._from_raw('|ᥩ//', 2, 11, "{0} |ᥩ// {1}", Ⲉǃǃ, (ⲈOʙ, ⲈOʙ), func=isdisjoint_supreme)

ꘉT = quiktyp('ꘉT', infix, _op_eval_priority=4, 
                                            rand=infix.__ror__, 
                                            rxor=infix.__ror__, 
                                            floordiv=infix.__or__, 
                                            instantiate=0)
#    ꞌᵔꞋᴖ
#    ᴗꞋᵕꞌ7 
#infixᐩ ꗝ
ꘉ = infix((isdisjoint.op,))
ᥤ = infix((intersects_disjoint.op,))
ᥩ = infix((isdisjoint_supreme.op,))

#print(opvar('p') |ꘉ| opvar('q'))
#print(opvar('p') |ᥤ| opvar('q'))
#print(opvar('p') |ᥩ| opvar('q'))
ꘉ = ꘉT((isdisjoint.op,))
ᥤ = ꘉT((intersects_disjoint.op,))
ᥩ = ꘉT((isdisjoint_supreme.op,))
#print(opvar('p') |ꘉ| opvar('q'))
#print(opvar('p') &ᥤ// opvar('q'))
#print(opvar('p') |ᥩ// opvar('q'))


_relmapꓸ_cmp2index = staticmethod(('!', '>', '=', '|', '<', '^', '&', ).index)
#_relmap_cmp_ops = ('??', '>=', '==', '|!', '<=', '^!', '&!')
_relmap_cmp_ops = ('!=', '>=', '==', isdisjoint_supreme.op, '<=', isdisjoint.op, intersects_disjoint.op)
_relmap_cmp_reverse_ops = ('!=', '<=', '==', isdisjoint_supreme.op, '>=', isdisjoint.op, intersects_disjoint.op)
@modulefunc
@sovereign(base=tuple)
class relation_map(tuple):
    #xⴺꘉⲶΣ:    xⴺꘌᑕΣ:    xⴺᑎꘌΣ:
    xⲶꘉ: ⲈCᴛ[opterm] = _tuplegetter(0b000, "Unsorted")              # 0
    xᑐꘌ: ⲈCᴛ[opterm] = _tuplegetter(0b001, "Subsets")                # 1
    xⲶꘌ: ⲈCᴛ[opterm] = _tuplegetter(0b010, "Identities")            # 2
    xᑕꘌ: ⲈCᴛ[opterm] = _tuplegetter(0b100, "Supersets")            # 4
    xꘌᑎ: ⲈCᴛ[opterm] = _tuplegetter(0b110, "Quasi Supersets") # 6
    xꘌꘉ: ⲈCᴛ[opterm] = _tuplegetter(0b101, "Disjoint sets")        # 5
    xꘌᑌ: ⲈCᴛ[opterm] = _tuplegetter(0b011, "Quasi Subsets")    # 3
    _termmap: dict[opterm] = _tuplegetter(7, "Terms Mapped")    # 7
    #    ⵌ ℘ ʗ ⵁ 〵 ⴱꕕ Ⲷꘉ ᑐⰅᑕⲈ  ᑌᑎ ⴹⴺ
    #    ᴱᴲᵉᵊᵋᵌᶟᴇⱻₑₔ
    _field_names: tuple[str] = ("xⲶꘉ", "xᑐꘌ", "xⲶꘌ", "xꘌᑌ", "xᑕꘌ", "xꘌꘉ", "xꘌᑎ", "_termmap")
    
    def _itemize(self):
        ǁ, ᑐ, Ⲷ, ᑌ, ᑕ, ꘉ, ᑎ = list(map(frozet, self[:7]))
        ⲷ = Ⲷ[0]
        yield ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ('==', Ⲷ, Ⲷ, domain=Ⲉǃǃ)
        yield ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ('>=', ⲷ, ᑐ, domain=Ⲉǃǃ)
        yield ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ('<=', ⲷ, ᑕ, domain=Ⲉǃǃ)
        yield ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(_relmap_cmp_ops[-2], ⲷ, ꘉ, domain=Ⲉǃǃ)
        yield ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(_relmap_cmp_ops[3], ⲷ, ᑌ, domain=Ⲉǃǃ)
        yield ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(_relmap_cmp_ops[-1], ⲷ, ᑎ, domain=Ⲉǃǃ)
#        for relop, sets in zip(_relmap_cmp_ops, self):
#            yield 
    
    def __new__(cls):
        self = ꓽtupleꓸ__new__(cls, (set(), set(), set(), set(), set(), set(), set(), dict()))
        return self
    
    def __repr__(self):
        ǁ, ᑐ, Ⲷ, ᑌ, ᑕ, ꘉ, ᑎ, _ = self
        return f"({Ⲷ=}, {ᑐ=}, {ᑕ=}, {ꘉ=}, {ᑎ=} {ᑌ=})"
    
    def add(self, predicate: oprelation):
        if not (isinstance(predicate, oprelation) or (opfunc(predicate.op).codomain is Ⲉǃǃ)):
            raise ValueError('predicate must be a binary relation')
        cmp, leftterm, rightterm = predicate[None]
        cmp = str(cmp)
        Ⲷ = self.xⲶꘌ
        if (not Ⲷ):
            Ⲷ.add(leftterm)
        elif (leftterm not in Ⲷ):  raise ValueError('left side must be an identity')
        if (leftterm not in self._termmap):
            self._termmap[leftterm] = self
        if (cmp == '!='):
            P = leftterm == (leftterm & rightterm)
            Q = leftterm == (leftterm | rightterm)
            cmp = ('!=' if P else '|') if Q else ('&' if P else '^')
        elif (cmp == '=='):
            if (rightterm not in self._termmap):
                self._termmap[rightterm] = self
        try:
            S = self[_relmapꓸ_cmp2index(cmp[0])]
        except ValueError as exc:  raise IndexError(vars())
        else:
            S.add(rightterm)
    
    def getterm(self, term: opterm):
        termmap = self._termmap
        try:  return termmap[term]
        except KeyError:
            termmap[term] = ()
            return termmap[term]







opsyms_list = [
    '.', '[]', '()', ', ', 
    '', ' ~', ' +', ' -', ' **-1', 
    '|', '&', '^', '+', '-', '*', '/', '**', '//', '%', '<<', '>>', '@', 
    '==', '!=', '<', '>', '<=', '>=', 
    ' in ', ' not in ', ' is ', ' is not ', 
    'not ', ' or ', ' and ', ' if else ', 
    ':=', '.=', '[]=', 
    '|=', '&=', '^=', '+=', '-=', '*=', '/=', '**=', '//=', '%=', '<<=', '>>=', '@=', 
    ]
ǂⱶ = ǂ()
opsyms_list = [opfunc(op) for op in opsyms_list] #[:opsyms_list.index(":=")])]
opsyms_by_arity = {None:  ǂ(('()', ', ')) | opfunc._instances, 
                            1: ǂ(('', ' ~', ' +', ' -', ' **-1', 'not ')) | opfunc._instances, 
                            2: ǂ(('|', '&', '^', '+', '-', '*', '/', '**', '//', '%', '<<', '>>', '@', 
                                    '==', '!=', '<', '>', '<=', '>=', ' or ', ' and ', ' in ', ' not in ', 
                                    )) | opfunc._instances, 
                            3: ǂ(('[]=', ' if else ', )) | opfunc._instances, 
                            }
opsyms_by_codomain = {
        ⲈOʙ: ǂⱶ['.', '[]', '()', ', ', '', ] | opfunc._instances, 
        Ⲉǃǃ: ǂⱶ['==', '!=', '<', '>', '<=', '>=', 
                ' in ', ' not in ', #' is ', ' is not ', 
                'not ', ' or ', ' and ', ' if else ', ] | opfunc._instances, 
        ⲈLᴛ: ǂⱶ['', ' ~', '|', '&', '^', '-', ] | opfunc._instances, 
        ⲈUɴ: ǂⱶ[' +', ' -', ' **-1', '+', '-', '*', '/', '**', '//', '%', ] | opfunc._instances, 
        ⲈVᴄ: ǂⱶ['<<', '>>', '@', ] | opfunc._instances, 
    }


import random as ra
import numpy as np
ra.seed(os.urandom(*os.urandom(1)))
rng =np.random.default_rng(seed=tuple(os.urandom(*os.urandom(1))))

def random_expression(opfuncs_pool: tuple[opfunc], opvars_pool: tuple[opvar], size: int, 
domain: type=None):
    ls = []
    terms = list(range(size))
    joints_pool = list(opfuncs_pool)
    op = ra.choice(joints_pool)
    nin = op.nin
    ls.append((op, []))
    if (nin is not None):
        ls[0].extend([[]])



sys.path.append("/storage/emulated/0/Documents/Pydroid3/pythonstuff/Algevaric/")
from _abominable_types_.useless_metaclasses import subclasses_unravel


def _test():
    
    #_run_get_latticeop_permutations()
    
    _test_simplify_canonical()
    
    _test_relationrefset()
    
    print("\n\n")
#    
#    logfunc_print_logs(summarize_to_precision=2, summarize_with_paramspec_to_precision=-1, abbreviate_paramstr_threshold=120, display_name_count=24)
#    
#    logs_compiled = logfunc_compile_logs(get_mean=True)
#    for fname, fref in logs_compiled.items():
#        print(f"\n"\
#            f"Ⱶ ⲶⱵ ꘌⲶ ꘌⲶ ꘌⲈ  ____ {fname} ____  Ⰵꘌ Ⲷꘌ Ⲷꘌ ⱵⲶ Ⱶ >>> ꔷ")
#        for params, times in fref.items():
#            if params is not None:
#                params = ', '.join(f"{k}={v}" for k,v in params).join('()')
#                if (len(params) > 32):
#                    params = params[:26] + ' . . . )'
#            print(
#            f"        {params!s:>32} :  {times / 1_000_000_000 :>8.5f}, ")
#    
    exit()
    
    #_test_0()



def _test_relationrefset():
    relref = relset()
    relref = relation_map()
    
    p, q, o = list(map(opvar, "pqo"))
    pqꛌo = (p | q) & o
    
    relref.add(pqꛌo <= (p|q))
    relref.add(pqꛌo <= (o))
    relref.add(pqꛌo._eq_((p&o)|(q&o)))
    relref.add(pqꛌo >= (p&o))
    relref.add(pqꛌo >= (q&o))
    
    print(relref.getterm(pqꛌo))
    
    for item in relref._itemize():
        print('    ', (item.op, item))



#x = opvar(2)
#print(f"\n{x = }    {x.domain = }\n{x[ⲈRɴ] = }\n{x[ⲈCɴ] = }\n{x[ⲈLᴛ] = }\n")
#x = opvar(False)
#print(f"\n{x = }    {x.domain = }\n{x[ⲈSᴘ] = }\n{x[Ⲉǃǃ] = }\n{x[ⲈLᴛ] = }\n")

#x = opvar("x", domain=ⲈZɴ)
#print(f"\n{(x, x.domain) = }")
#x = x[ⲈCɴ]
#print(f"\n{(x, x.domain) = }")
#print(f"\n{(x, type(x).__name__) = }")
#x = x - 3
#print(f"\n{(x, type(x).__name__) = }")
#x = x - 3
#ϱ

class Ranondom(tuple):#(metaclass=ABCDMeta):
    def __new__(cls, pool: tuple=MathDomainTypes):
        return tuple.__new__(cls, pool)
    def as_domain(self):  return ra.choice(self)
    def __contains__(self, other):  return True



def _test_simplify_canonical():
    import numpy as np
    import random as ra
    
    #opvar.__repr__ = opvar.__str__
    
    rng = np.random.default_rng()
    choices = rng.choice
    αβγδεζηθικλμνξοπρστυφχψω = np.array(list("αβγδεζηθικλμνξοπρστυφχψω"), dtype="O")
   
    #αβγδεζηθικλμνξοπρστυφχψω = tuple(map(opvar, "αβγδεζηθικλμνξοπρστυφχψω"))
    #[opvar(ch, domain=ⲈOᴠ) for ch in "αβγδεζηθικλμνξοπρστυφχψω"]
    
#    for ch in αβγδεζηθικλμνξοπρστυφχψω:
#        ch = opvar(ch, domain=ⲈOᴠ)
#        chlist = [ch[ⲈD] for ⲈD in MathDomainTypes]
#        #print(*map(repr, chlist), sep=', ')
        
    
    canonref = {}
    canonref |= canonref_lattice_ops
    canonref |= canonref_py_ops_numeric
    
#    canonref |= {
#    (_X + _Y) - _Z: (_X+_Y)-_Z,
#    (_X @ _Y) >> _Z: (_X @ (_Y>>_Z)), 
#    }
    
    #D = ⲈCᴛ
    
#    canonref = {k[D]: v[D] for k, v in canonref.items()}
#    print(*[(x, [(y, get_domain(y)) for y in x.operands]/) for x in chain.from_iterable(canonref.items())], sep="\n")
    
    #rewriters = _get_rewriters(cmp_matchtransform, canonref)
#    simplify = method(_apply_rewrites, rewriters)
    simplify = simplify_canonical(canonref, )
    
    #simplify = logfunc(simplify)
    
    canondom = Auto
    if (canonref == canonref_lattice_ops):
        opprops_ref = propertiesref_lattice_ops
        op_pool = ["|", "&", "^", " ~"] + ["<=", ">="]
        canondom = ⲈLᴛ
    elif (canonref == canonref_py_ops_numeric):
        opprops_ref = propertiesref_py_ops_numeric
        op_pool = ["+", "-", "*", "/", " **-1", " -"]
        op_pool = list(chain.from_iterable((ǂ(ǂ[:2,:4,:4,-2:,-1:])|op_pool)))
        canondom = ⲈUɴ
    elif (canonref.keys() == canonref_lattice_ops.keys() | canonref_py_ops_numeric.keys()):
        opprops_ref = propertiesref_lattice_ops | propertiesref_py_ops_numeric
        op_pool = ["|", "&", "^", " ~"] + ["<=", ">="] + ["+", "-", "*", "/", " **-1", " -"]
        canondom = ⲈOʙ
    else:
        op_pool = []
        opprops_ref = {}
        
    #canondom = Ranondom(type.__subclasses__(ⲈUɴ) + type.__subclasses__(ⲈLᴛ))
    #canondom = Ranondom(subclasses_unravel(ⲈUɴ))
    canondom = type("T", (ⲈUɴ, ⲈLᴛ), {})
    
    _αβn = "αβγδεζηθικλμνξοπρστυφχψω".index
    _ƍẟ = lambda ch: ((_αβn(ch) - 12) * 0.25) if pqr_get_vals else Unknown
    
    pqr_get_vals = False
    
    
    failures = []
    for pattern, canonical in canonref.items():
        _PQR= choices(αβγδεζηθικλμνξοπρστυφχψω, size=3, replace=False)
        _P, _Q, _R = _PQR \
            = [opvar(_V, value=_ƍẟ(_V), domain=canondom)#(ⲈBʟ if (_P in "αεηιουω") else ⲈLᴛ))
                                for _V in map(str, _PQR)]
        
        pqr_get_vals and print([(_V, _V.value) for _V in _PQR])
        
        assert (_P in canondom) and (_Q in canondom) or (canondom is Auto)
        
        expression = pattern
        #for V in (_ꓽ0, _ꓽ1, _ꓽᐨ1, _ꓽꭒɲᶑꬲꝼ):
#            #print(f"[ⲷⲷⲷⲷⲷⲷⲷⲷ(    {V=}    {V.value=}    )ⲷⲷⲷⲷⲷⲷⲷⲷ]")
#            expression = expression.replace(V, V.value)
        expression = expression.replace(_X, _P).replace(_Y, _Q).replace(_Z, _R)
        
        _expression = expression
        _canonical = canonical
#        expression = (~expression >> (_P << _Q))
#        canonical = (canonical >> (_X << _Y))
#        canonical = (canonical >> pattern)[[0,2,1]]
        
        
        
        try:
            simplified = simplify(expression)
        except Exception as exc:
            print(f"({pattern!r}):  {expression!r}    ==>    {exc!r}\n")
            raise exc
        
        if not match(canonical, simplified):
#        if not match(canonical[canonical.index(_canonical)], simplified[expression.index(_expression)]):
            #print("✅❌"[0])
        #else:
            print("        (    ★        ❌        ★    )        ")
            indexes = cmp_get_matchindexes(pattern, expression)
            wrerite, wrindices = _cmp_get_rewrite_indices(pattern, canonical)
            
            rerighter = matchrewriter(pattern, canonical)
            
            if not (isinstance(simplified, opterm) and match(canonical, simplified[indexes])):
                
                failures.append((pattern, canonical, expression, simplified))
                if canonical in (ꓽTrue, ꓽFalse) or type(simplified) is opfunc: continue
                    
                print("        ★        ❌        ★        ❌        ★        ❌        ★        ")
                print(f"                    {pattern=}        ({type(pattern)})")
                print(f"                    {canonical=}        ({type(canonical)})")
                print(f"                    {simplified=}        ({type(simplified)})")
                print(f"                    {expression=}        ({type(expression)})")
                print(f"        {indexes=}")
                print(f"        {expression[indexes]=}        ({type(expression[indexes])})")
                print(f"        {wrindices=}")
                print(f"        {wrerite=}")
                if not indexes:
                    indexes = [indexes or None]
                expritem = expression[indexes[0]]
                print(f"        {expritem=}")
                print(f"        {(expritem + wrerite)=}")
                print(f"        {ꓽtupleꓸ__new__ǁoptermǁ((ʻʻᐩˮ, expritem, wrerite))=}")
                print(f"        {(expritem + wrerite)[wrindices]=}")
                print(f"        {ꓽtupleꓸ__new__ǁoptermǁ((ʻʻᐩˮ, expritem, wrerite))[wrindices]=}")
                print(f"        {rerighter(expression)=}")
                print(f"        {rerighter(pattern)=}")
                #        ({len(expression[indexes])=})")
                print(f"                           {canonical=}")
                _cache = {}
                #gtm.getem_print(simplify)l
                rewriters = simplify.__self__
                _expr = _apply_rewrites(rewriters, expression, _cache=_cache)
                print(*_cache[expression], sep="\n")
                
        w = 12
        #simplified = opvar(simplified)
        #canonical = opvar(canonical)
#        print(
#   f"⠀⠀{(pattern):s!⠀>{w})}⠀║⠀⠀{expression:s!⠀^{w})}⠀╠═>║⠀{(simplified):⠀^{w}}⠀⠀║⠀{(canonical):⠀<{w}}")
#    
        print(f"⠀⠀{(pattern):⠀>{w})}⠀⠀"\
                f"║⠀{expression:r!⠀^{w})}⠀╠═>"\
                f"║⠀{(simplified):⠀^{w}}⠀⠀"\
                f"║⠀⠀{(canonical):⠀<{w}}")
        if (not pqr_get_vals):
            continue
        print(f"ⲶⱵ~⠀⠀({evaluate(pattern)})⠀"\
                f"ǁ⠀⠀({evaluate(expression)})⠀⠀⠀ǁ>>>"\
                f"ǁ⠀⠀({evaluate(simplified)})⠀⠀"\
                f"ǁ⠀⠀({evaluate(canonical)})⠀")
#        def ƒ(xyz):
#            if not isinstance(xyz, _core_symbolic):  return xyz
#            for x in xyz.operands:
#                if isinstance(x, opvar):
#                    print("[    ]", x, x.value)
#                    xyz = replace(xyz, x, x.value)
#            return xyz
#        print(f"ⲶⱵ~⠀⠀({ƒ(pattern)})⠀"\
#                f"ǁ⠀⠀({ƒ(expression)})⠀⠀⠀ǁ>>>"\
#                f"ǁ⠀⠀({ƒ(simplified)})⠀⠀"\
#                f"ǁ⠀⠀({ƒ(canonical)})⠀")
        print()
#        simplified.variables.sort()
#        print(f"            {simplified.parametrize(2, 3) = }")
#        print(f"            {simplified.evaluate(2, 3) = }")
    
    print(f"═{'═':═>{w}}═╩═{'═':═>{w}}═╝⠀⠀╚═{'═':═>{w}}╩═{'═':═>{w}}═╝")
    exit()
    for pattern, canonical, expression, simplified in failures:
        
        print("        ★        ❌        ★        ❌        ★        ❌        ★        ")
        #print(
#   f"⠀⠀{(pattern):s!⠀>{w})}⠀║⠀⠀{expression:⠀^{w})}⠀╠═>║⠀{(simplified):s!⠀^{w})}⠀⠀║⠀{(canonical):s!⠀<{w})}")
    print(
   f"⠀⠀{(pattern):⠀>{w}}⠀║⠀⠀{expression:⠀^{w}}⠀╠═>║⠀{(simplified):⠀^{w}}⠀⠀║⠀{(canonical):⠀<{w}}")
    
    print(f"═{'═':═>{w}}═══{'═':═>{w}}══════{'═':═>{w}}══{'═':═>{w}}══")
    print(" - -  -:-   -:–:-     -:–:—:–:-        -:–:–:—:—:–:–:-        -:–:—:–:-      -:–:-   -:-  - - ")
    
    ref = {v:k for k,v in (canonref.items() - opprops_ref.items()) \
                                                    if (isinstance(v, opterm) \
                                                and (len(k) > 1 < len(v)) \
                                                and (k[[0, ǂ[1::-1] ]] != v[[0, ǂ[1::+1] ]]) \
                                                        )\
                                                        } | opprops_ref
    if canondom is ⲈLᴛ:
        ref = dict(map(attrgetter('left','right'), identities_ref_lattice_ops))
    
    rerewriters = get_rewriters_matchrewrite(ref)
    unsimplify = method(_apply_rewrites, rerewriters)
    
    op_pool = list(map(opfunc, op_pool))
    
    var_pool = [opvar(ch, domain=canondom) for ch in ǂ(ǂ[0,1,2,-3,-2,-1])|"ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘવʀꜱᴛᴜᴠᴡxʏᴢ"]
    
    
    for op in unique_everseen(op_pool):
        if (op.nin != 1):  continue
        var_pool.extend([op(x) for x in var_pool])
    #var_pool.extend([+x for x in var_pool]+[-x for x in var_pool]+[x**-1 for x in var_pool])
    
    
    for i in range(8):
        while True:
            oplist = list(ra.choices(op_pool, k=ra.randrange(3, 8)))
            varlist = list(ra.choices(var_pool, k=ra.randrange(3, 8)))
            
            while (oplist and varlist[1:]):
                s = (1,2) if ra.randrange(2) else (2,1)
                varlist[:2] = [oplist[ra.randrange(len(oplist))](*varlist[:2])[[0, *s]]]
         #       if ra.randrange(2):
#                    varlist[0] = varlist[0][[0,2,1]]
            expression = varlist[0]
            #_apply_rewrites.__kwdefaults__["recursion_limit"] = 5
            noisserpxe = unsimplify(expression, recursion_limit=8)
            if (expression != noisserpxe):
                break
        
        #print(f"\n{oplist = }\n{varlist = }")
        
        print(f"\n{expression:)}  ==>  {simplify(expression):)}  <==  {noisserpxe:)}")
        print()
        #print(" - -  -:-   -:–:-     -:–:—:–:-        -:–:–:—:—:–:–:-        -:–:—:–:-      -:–:-   -:-  - - ")



def _test_0():
    print(" - -  -:-   -:–:-     -:–:—:–:-        -:–:–:—:—:–:–:-        -:–:—:–:-      -:–:-   -:-  - - ")
    
    a, b, c = varlist = [opvar(ch, domain=Real) for ch in "abc"]
    f, g, h = varlist = [opvar(ch, domain=Ⲉƒx) for ch in "fgh"]
    x, y, z = varlist = [opvar(ch, domain=Number) for ch in "xyz"]
    
    patt: opterm = (~x | ~y)
    canon: opterm = ~(x & y)
    expr: opterm = (~a | ~(b ^ 2))
    
    print(f"{a, b, c = }")
    print(f"{x, y, z = }")
    
    print(f"\n{patt = }\n{canon = }\n{expr = }")
    ref = {}
    print(f"{match(patt, expr, _matched=ref) = }\n    {ref = }")
    _expr: opterm = cmp_matchtransform(patt, canon, expr)
    print(f"{expr = }\n{_expr = }\n")
    
    patt: opterm = (~x | ~(y ^ z))
    canon: opterm = f(x, y, z)
    
    print(f"\n{patt = }\n{canon = }\n")
    _expr: opterm = cmp_matchtransform(patt, canon, expr)
    print(f"{expr = }\n{_expr = }\n")
    
    patt: opterm = (~x | ~y)
    canon: opterm = ~(x & y)
    expr: opterm = (~a |ꔷ| ~(b ^ 2)) ^ c
    
    expr: opterm = (~a | ~(b ^ 2)) % c
    
    print(f"\n{patt = }\n{canon = }\n")
    _expr: opterm = cmp_matchtransform(patt, canon, expr)
    print(f"{expr = }\n{_expr = }")
    print(f"{expr.replacements({patt:canon}) = }")
    print(f"{expr.matchrewrite({patt:canon}) = }")
    print(f"{apply_rewrites_matchrewrite({patt:canon})(expr) = }\n")
    
    dct = {a: (b ^ 2), c: ~a}
    dct = {(b^2): 3, "|": ʻʻƒⵙ}
    dct = {a: (b^2), "|": ʻʻƒꔷ, (x|ꔷ|y)[0]: (x|ꕺ|y)[0]}
    assert (type(ʻʻƒꔷ) is opfunc)
    #dct.pop("|")
    print(f"\n{dct = }")
    print(f"\n{patt = }\n{canon = }\n")
    print(f"{expr = }\n{expr[dct] = }")
    print(f"{expr = }\n{apply_rewrites_replacements(dct)(expr) = }\n")
    
    print(" - -  -:-   -:–:-     -:–:—:–:-        -:–:–:—:—:–:–:-        -:–:—:–:-      -:–:-   -:-  - - ")
    
    print(f"\n{patt = }\n{canon = }\n\n{expr = }")
    print(f"{expr.replacements(dct) = }")
    print(f"{expr.matchrewrite(dct) = }")
    def g(p, q):
        return (tuple(ucs.ucd_categories(p)) == tuple(ucs.ucd_categories(q)))
    ᴄᴍᴘ = (lambda p: (lambda q: g(str(p), str(q))))
    print(f"ᴄᴍᴘ = (lambda p: (lambda q: ucd_category_match(p, q)))")
    print(f"{expr.rewrites(dct, cmp_method=ᴄᴍᴘ) = }\n")
    
    ᴄᴍᴘ = (lambda p: (lambda q: ((p) == (q))))
    print(f"ᴄᴍᴘ = (lambda p: (lambda q: (p == q)))")
    print(f"{expr.rewrites(dct, cmp_method=ᴄᴍᴘ) = }\n")
    
    ᴄᴍᴘ = (lambda p: (lambda q: match(p, q)))
    print(f"ᴄᴍᴘ = (lambda p: (lambda q: match(p, q)))")
    print(f"{expr.rewrites(dct, cmp_method=ᴄᴍᴘ) = }\n")
    
    ᴄᴍᴘ = (lambda p: (lambda q: match(p, q) or (p == q)))
    print(f"ᴄᴍᴘ = (lambda p: (lambda q: match(p, q) or (p == q)))")
    print(f"{expr.rewrites(dct, cmp_method=ᴄᴍᴘ) = }\n")
    
    ᴄᴍᴘ = (lambda p: (lambda q: (get_domain(p) >= get_domain(q)) and \
                                                        (type(p) is type(q) is opfunc)
        ))
    print(f"ᴄᴍᴘ = (lambda p: (lambda q: (get_domain(p) >= get_domain(q))))")
    print(f"{expr.rewrites(dct, cmp_method=ᴄᴍᴘ) = }\n")
    
    print(" - -  -:-   -:–:-     -:–:—:–:-        -:–:–:—:—:–:–:-        -:–:—:–:-      -:–:-   -:-  - - ")


if __name__ == "__main__":
    
    print("\n\n\n")
    
    _test()
    
    print("\n\n")
    exit()
