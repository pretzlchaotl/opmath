
import sys
sys.path.append('/storage/emulated/0/Documents/Pydroid3/pythonstuff/distrib/')
import builtins, operator, math, cmath
from abcd._mathdomains_abcd_ import (
    ⲈOʙ, Ⲉƒx, 
    ⲈUɴ, ⲈCɴ, ⲈRɴ, ⲈQɴ, ⲈZɴ, ⲈNɴ, 
    ⲈLᴛ, Ⲉǃǃ, 
    ⲈCᴛ, ⲈSᴘ, 
    ⲈIᴛ, ⲈSવ, ⲈCʜ, ⲈVᴄ, 
    Hashable, 
    )


"  //  ____  //  DOMAIN OBJECTS  \\  ____  \\  "
ᴰᵾ = ⲈOʙ
ᴰꜰ = Ⲉƒx
ᴰꭥ = ⲈUɴ
ᴰc = ⲈCɴ
ᴰʀ = ⲈRɴ
ᴰવ = ⲈQɴ
ᴰz = ⲈZɴ
ᴰɴ = ⲈNɴ
ᴰᴌ = ⲈLᴛ
ᴰᴃ = Ⲉǃǃ
ᴰⲉ = ⲈCᴛ
ᴰᴘ = ⲈSᴘ
ᴰᵻ = ⲈIᴛ
ᴰꜱ = ⲈSવ
ᴰʨ = ⲈCʜ
ᴰᴠ = ⲈVᴄ

ᴰꟸ = Hashable

attrgetter = operator.attrgetter
methodcaller = operator.methodcaller

_floor, _ceil, _trunc = math.floor, math.ceil, math.trunc
_round, _abs, _len, _iter = builtins.round, builtins.abs, builtins.len, builtins.iter
_getattr, _delattr, _setattr = builtins.getattr, builtins.delattr, builtins.setattr
_ln, _exp, _log2, _exp2, _log = cmath.log, cmath.exp, math.log2, math.exp2, cmath.log
_divmod = builtins.divmod
_bool = builtins.bool
_int, _float, _complex = builtins.int, builtins.float, builtins.complex

_1j = 1j
_nan = math.nan


"  //  ____  //  ELEMENTARY FUNCTIONS  \\  ____  \\  "

#    PyCore
def call_(f: ᴰꜰ, *xyz: ᴰᵾ) -> ᴰᵾ:  return f(*xyz)
def call_nullary_(f: ᴰꜰ) -> ᴰᵾ:  return f()
def call_unary_(f: ᴰꜰ, x: ᴰᵾ) -> ᴰᵾ:  return f(x)
def call_binary_(f: ᴰꜰ, x: ᴰᵾ, y: ᴰᵾ) -> ᴰᵾ:  return f(x, y)
call_n_ary_ = call_

def getattr_(m: ᴰᵾ, n: ᴰʨ) -> ᴰᵾ:  return _getattr(m, n)
def delattr_(m: ᴰᵾ, n: ᴰʨ) -> ᴰᵾ:
    _delattr(m, n)
    return m
def setattr_(m: ᴰᵾ, n: ᴰʨ, o: ᴰᵾ) ->ᴰᵾ:
    _setattr(m, n, o)
    return m

def getitem_(m: ᴰⲉ, n: ᴰꟸ) -> ᴰᵾ:  return m[n]
def delitem_(m: ᴰⲉ, n: ᴰꟸ) -> ᴰⲉ:
    del m[n]
    return m
def setitem_(m: ᴰⲉ, n: ᴰꟸ, o: ᴰᵾ) ->ᴰⲉ:
    m[n] = o
    return m


#    Unary
def ident_(v: ᴰᵾ) -> ᴰᵾ:  return v

def invert_(x: ᴰᴌ) -> ᴰᴌ:  return (~x)
def pos_(x: ᴰꭥ) -> ᴰꭥ:  return (+x)
def neg_(x: ᴰꭥ) -> ᴰꭥ:  return (-x)
def mulinv_(x: ᴰꭥ) -> ᴰꭥ:  return (1/x)

def sign_(x: ᴰʀ) -> ᴰʀ:  return x and (x/_abs(x))
def csign_(z: ᴰc) -> ᴰꭥ: return _exp(phase_(z) * _1j)
def abs_(x: ᴰꭥ) -> ᴰꭥ:  return _abs(x)
def phase_(z: ᴰc) -> ᴰʀ: return _phase(z) if _bool(z) else _nan

def ln_(x: ᴰꭥ) -> ᴰꭥ:  return _ln(x)
def exp_(x: ᴰꭥ) -> ᴰꭥ:  return _exp(x)

def real_(z: ᴰc) -> ᴰʀ:  return z.real
def imag_(z: ᴰc) -> ᴰʀ:  return z.imag
def numerator_(x: ᴰવ) -> ᴰz:  return x.numerator
def denominator_(x: ᴰવ) -> ᴰɴ:  return x.denominator
_get_real = attrgetter("real")
_get_imag = attrgetter("imag")
_get_numerator = attrgetter("numerator")
_get_denominator = attrgetter("denominator")

def conjugate_(z: ᴰc) -> ᴰc:  return z.conjugate()
_methodcall_conjugate = methodcaller("conjugate")

#    Repetitors
def incr_(x: ᴰꭥ) -> ᴰꭥ:  return x + 1
def decr_(x: ᴰꭥ) -> ᴰꭥ:  return x - 1
succ_ = incr_
precc_ = decr_
def double_(x: ᴰꭥ) -> ᴰꭥ:  return x * 2
def halve_(x: ᴰꭥ) -> ᴰꭥ:  return x / 2
def sqr_(x: ᴰꭥ) -> ᴰꭥ:  return x ** 2
def sqrt_(x: ᴰꭥ) -> ᴰꭥ:  return x ** mulinv_(2)
def log2_(x: ᴰꭥ) -> ᴰꭥ:  return _log2(x)
def exp2_(x: ᴰꭥ) -> ᴰꭥ:  return _exp2(x)

#    Adjusters
def floor_(x: ᴰꭥ) -> ᴰꭥ:
    try:  return _floor(x)
    except TypeError:  return _floor(x.real) + _floor(x.imag) * _1j
def ceil_(x: ᴰꭥ) -> ᴰꭥ:
    try:  return _ceil(x)
    except TypeError:  return _ceil(x.real) + _ceil(x.imag) * _1j
def trunc_(x: ᴰꭥ) -> ᴰꭥ:
    try:  return _trunc(x)
    except TypeError:  return _trunc(x.real) + _trunc(x.imag) * _1j

def nullround_(x: ᴰꭥ) -> ᴰꭥ:
    try:  return _round(x, 0)
    except TypeError:  return _round(x.real, 0) + _round(x.imag, 0) * _1j

def deciround_(x: ᴰꭥ, n: ᴰz=0) -> ᴰꭥ:
    try:  return _round(x, n)
    except TypeError:  return _round(x.real, n) + _round(x.imag, n) * _1j
def baseround_(x: ᴰꭥ, n: ᴰz=0, b: ᴰꭥ=2) -> ᴰꭥ:
    d = b**n
    try:  return _round(x * d) / d
    except TypeError:  return (_round(x.real * d) / d) + (_round(x.imag * d) / d) * _1j

round_ = nullround_


#    Binary Arithmetic (based on python dunders)
def or_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return a | b
def and_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return a & b
def xor_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return a ^ b
def nor_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return ~(a | b)
def nand_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return ~(a & b)
def xnor_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return ~(a ^ b)
def imply_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return (~a) | b
def nimply_(a: ᴰᴌ, b: ᴰᴌ) -> ᴰᴌ:  return a & (~b)

def add_(a: ᴰᵾ, b: ᴰᵾ) -> ᴰᵾ:  return a + b
def sub_(c: ᴰꭥ, a: ᴰꭥ) -> ᴰꭥ:  return c - a
def mul_(a: ᴰᵾ, b: ᴰᵾ) -> ᴰᵾ:  return a * b
def truediv_(c: ᴰꭥ, a: ᴰꭥ) -> ᴰꭥ:  return c / a
def pow_(a: ᴰꭥ, b: ᴰꭥ) -> ᴰꭥ:  return a ** b
def root_(b: ᴰꭥ, c: ᴰꭥ) -> ᴰꭥ:  return c ** mulinv_(b)
def log_(c: ᴰꭥ, a: ᴰꭥ) -> ᴰꭥ:  return _log(c, a)

def lshift_(a: ᴰz, b: ᴰɴ) -> ᴰz:  return a << b
def rshift_(a: ᴰz, b: ᴰɴ) -> ᴰz:  return a >> b
def matmul_(m0: ᴰᴠ, m1: ᴰᴠ) -> ᴰᴠ:  return m0 @ m1

def floordiv_(a: ᴰꭥ, b: ᴰꭥ) -> ᴰꭥ:  return a // b
def mod_(a: ᴰꭥ, b: ᴰꭥ) -> ᴰꭥ:  return a % b
def divmod_(a: ᴰꭥ, b: ᴰꭥ) -> ᴰꜱ[ᴰꭥ,ᴰꭥ]:  return _divmod(a, b)


#    Binary Comparison
def eq_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return p == q
def ge_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return p >= q
def le_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return p <= q
def ne_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return p != q
def gt_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return p > q
def lt_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return p < q


#    BoolOps
def NOT_(p: ᴰᵾ) -> ᴰᴃ:  return (not p)
def TRU_(p: ᴰᵾ) -> ᴰᴃ:  return _bool(p)

def OR_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return p or q
def AND_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return p and q
def NOR_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return not (p or q)
def NAND_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return not (p and q)

def XOR_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return (not p) if q else p
def XNOR_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return p if q else (not p)
def IMPLY_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return (not p) or q
def NIMPLY_(p: ᴰᴃ, q: ᴰᴃ) -> ᴰᴃ:  return p and (not q)

def if_else_(p: ᴰᵾ, q: ᴰᵾ, r: ᴰᴃ) -> ᴰᵾ:  return (p if r else q)

def is_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return (p is q)
def isnt_(p: ᴰᵾ, q: ᴰᵾ) -> ᴰᴃ:  return (p is not q)

def in_(n: ᴰᵾ, m: ᴰⲉ) -> ᴰᴃ:  return (n in m)
def not_in_(n: ᴰᵾ, m: ᴰⲉ) -> ᴰᴃ:  return (n not in m)
def contains_(m: ᴰⲉ, n: ᴰᵾ) -> ᴰᴃ:  return (n in m)
def not_contains_(m: ᴰⲉ, n: ᴰᵾ) -> ᴰᴃ:  return (n not in m)


#    IterableOps & ContainerOps
def iter_(p: ᴰᵻ) -> ᴰᵻ:  return _iter(p)
def len_(p: ᴰᵻ) -> ᴰɴ:  return _len(p)

def indexof_(m: ᴰⲉ, n: ᴰᵾ) -> ᴰɴ:  return m.index(n)
def countof_(m: ᴰⲉ, n: ᴰᵾ) -> ᴰɴ:  return m.count(n)

def startuple_(*xyz: ᴰᵾ) -> ᴰꜱ:  return xyz

#    SetOps & SeqOps
def isdisjoint_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴃ:  return p.isdisjoint(q)
def issubset_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴃ:  return p.issubset(q)
def issuperset_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴃ:  return p.issuperset(q)
def issubset_strict_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴃ:  return (p!=q) and p.issubset(q)
def issuperset_strict_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴃ:  return (p!=q) and p.issuperset(q)

def union_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴘ:  return p.union(q)
def intersection_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴘ:  return p.intersection(q)
def symmetric_difference_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴘ:  return p.symmetric_difference(q)
def difference_(p: ᴰᴘ, q: ᴰᴘ) -> ᴰᴘ:  return p.difference(q)



functions_unary = (
    )
functions_binary = (
    )
#functions_reversible = (
#    call_unary_, 
#    getattr_, delattr_, setattr_, 
#    add_, sub_, mul_, truediv_, pow_, mod_, floordiv_, matmul_, 
#    lshift_, rshift_, 
#    in_, not_in_, indexof_, countof_, getitem_, delitem_, setitem_, 
#    root_, log_, divmod_, 
#    difference_, concat_, repseq_, 
#    OR_, AND_, XOR_, XNOR_, IMPLY_, NIMPLY_, 
#    imply_, nimply_, 
#    )

functions_binary_cmp = (eq_, ge_, le_, ne_, gt_, lt_)
functions_arithmetic = (
#    ident_, pos_, neg_, invert_, abs_, nsign_, sign_, 
#    floor_, ceil_, trunc_, 
#    round_, 
#    real_, imag_, numerator_, denominator_, 
#    conjugate_, mulinv_, ln_, exp_, log2_, exp2_, 
#    add_, sub_, mul_, truediv_, pow_, mod_, floordiv_, matmul_, 
#    or_, and_, xor_, lshift_, rshift_, 
#    #iadd_, isub_, imul_, itruediv_, ipow_, imod_, ifloordiv_, imatmul_, 
#    #ior_, iand_, ixor_, ilshift_, irshift_, /
#    root_, log_, divmod_, 
#    incr_, decr_, double_, halve_, sqr_, sqrt_, 
#    nor_, nand_, xnor_, imply_, nimply_, 
    )
functions_bool_out = (
    )
functions_container = (
    )
functions_setops = (
    )
functions_latticeops = (
    )


functions_all = (
    call_nullary_, call_unary_, call_binary_, call_n_ary_, 
    
    getattr_, delattr_, setattr_, 
    getitem_, delitem_, setitem_, 
    
    ident_, 
    
    invert_, 
    pos_, neg_, mulinv_, 
    sign_, csign_, abs_, phase_, 
    ln_, exp_, 
    
    real_, imag_, numerator_, denominator_, 
    conjugate_, 
    
    incr_, decr_, double_, halve_, sqr_, sqrt_, log2_, exp2_, 
    
    floor_, ceil_, trunc_, 
    nullround_, deciround_, baseround_, 
    
    or_, and_, xor_, 
    nor_, nand_, xnor_, imply_, nimply_, 
    add_, sub_, mul_, truediv_, 
    pow_, root_, log_, 
    lshift_, rshift_, matmul_, 
    floordiv_, mod_, divmod_, 
    
    eq_, ge_, le_, ne_, gt_, lt_, 
    
    NOT_, TRU_, 
    OR_, AND_, 
    NOR_, NAND_, XOR_, XNOR_, IMPLY_, NIMPLY_, 
    if_else_, 
    
    is_, isnt_, in_, not_in_, 
    
    startuple_, 
    iter_, len_, 
    indexof_, countof_, contains_, not_contains_, 
    
    isdisjoint_, issubset_, issuperset_, issubset_strict_, issuperset_strict_, 
    #cardinality_, complement_, powerset_, 
    union_, intersection_, symmetric_difference_, difference_, 
    #cartesian_product_, cartesian_power_, 
    )

#print(list(globals()))


__all__ = [
    #'ⲈOʙ', 'Ⲉƒx', 'ⲈUɴ', 'ⲈCɴ', 'ⲈRɴ', 'ⲈQɴ', 'ⲈZɴ', 'ⲈNɴ', 'ⲈLᴛ', 'Ⲉǃǃ', 'ⲈCᴛ', 'ⲈSᴘ', 'ⲈIᴛ', 'ⲈSવ', 'ⲈCʜ', 'ⲈVᴄ', 'Hashable', 
    #'Dᵾ', 'Dꜰ', 'Dꭥ', 'Dc', 'Dʀ', 'Dવ', 'Dz', 'Dɴ', 'Dᴌ', 'Dᴃ', 'Dⲉ', 'Dᴘ', 'Dᵻ', 'Dꜱ', 'Dʨ', 'Dᴠ', 'DĦ', 
    #'_floor', '_ceil', '_trunc', '_round', '_abs', '_len', '_iter', '_getattr', '_delattr', '_setattr', \
    #    '_ln', '_exp', '_log2', '_exp2', '_log', '_divmod', '_bool', '_int', '_float', '_complex', '_1j', '_nan', 
    'call_', 'call_nullary_', 'call_unary_', 'call_binary_', 'call_n_ary_', 
    'getattr_', 'delattr_', 'setattr_', 'getitem_', 'delitem_', 'setitem_', 
    
    'ident_', 'invert_', 'pos_', 'neg_', 'mulinv_', 'sign_', 'csign_', 'abs_', 'phase_', 'ln_', 'exp_', 
    'real_', 'imag_', 'numerator_', 'denominator_', 
    #'_get_real', '_get_imag', '_get_numerator', '_get_denominator', 
    'conjugate_', #'_methodcall_conjugate', 
    'incr_', 'decr_', 'succ_', 'precc_', 'double_', 'halve_', 'sqr_', 'sqrt_', 'log2_', 'exp2_', 
    'floor_', 'ceil_', 'trunc_', 'nullround_', 'deciround_', 'baseround_', 'round_', 
    'or_', 'and_', 'xor_', 'nor_', 'nand_', 'xnor_', 'imply_', 'nimply_', 
    'add_', 'sub_', 'mul_', 'truediv_', 'pow_', 'root_', 'log_', 
    'lshift_', 'rshift_', 'matmul_', 'floordiv_', 'mod_', 'divmod_', 
    
    'eq_', 'ge_', 'le_', 'ne_', 'gt_', 'lt_', 
    'NOT_', 'TRU_', 'OR_', 'AND_', 'NOR_', 'NAND_', 'XOR_', 'XNOR_', 'IMPLY_', 'NIMPLY_', 'if_else_', 
    'is_', 'isnt_', 'in_', 'not_in_', 
    
    'startuple_', 
    'iter_', 'len_', 'indexof_', 'countof_', 'contains_', 'not_contains_', 
    'isdisjoint_', 'issubset_', 'issuperset_', 'issubset_strict_', 'issuperset_strict_', 
    'union_', 'intersection_', 'symmetric_difference_', 'difference_', 
    
    'functions_unary', 'functions_binary', 'functions_binary_cmp', 'functions_arithmetic', 
    'functions_bool_out', 'functions_container', 'functions_setops', 'functions_latticeops', 
    'functions_all', 
    ]

#ref = list(map(attrgetter("__name__"), functions_all))
#print([k for k in globals() if k not in ref])


functions_unary = tuple(f for f in functions_all if (f.__code__.co_argcount==1))
functions_binary = tuple(f for f in functions_all if (f.__code__.co_argcount==2))


functions_arithmetic = tuple(f for f in functions_all \
                                                if all(((T <= ⲈUɴ or T <= ⲈLᴛ) \
                                                and not issubclass(T, (ⲈCᴛ, ⲈIᴛ))) for T in f.__annotations__.values()))
functions_bool_out = tuple(f for f in functions_all if (f.__annotations__["return"] == Ⲉǃǃ))
functions_container = tuple(f for f in functions_all \
                                                if (any(((ⲈCᴛ|ⲈIᴛ)>=T) for T in f.__annotations__.values())))
functions_setops = tuple(f for f in functions_all \
                                                if (any((ⲈSᴘ>=T) for T in f.__annotations__.values())))
functions_latticeops = tuple(f for f in functions_all \
                                                if (all((ⲈLᴛ>=T) and not (ⲈSᴘ>=T) for T in f.__annotations__.values())))

#print(list(map(attrgetter("__name__"), functions_all)), 
#list(map(attrgetter("__name__"), functions_arithmetic)), 
#(list(map(attrgetter("__name__"), functions_bool_out))), 
#(list(map(attrgetter("__name__"), functions_container))), 
#(list(map(attrgetter("__name__"), functions_setops))), 
#(list(map(attrgetter("__name__"), functions_latticeops))), 
#sep="\n\n")

