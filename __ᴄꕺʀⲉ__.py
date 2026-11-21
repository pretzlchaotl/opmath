
import sys, os
from _typing import _idfunc
from _collections import _tuplegetter, defaultdict
from _operator import is_ as __is__
from itertools import filterfalse, chain
from more_itertools import unique_everseen
from math import floor, ceil, trunc, inf, nan, isinf as _isinf, isfinite as _isfinite
import builtins, operator, math
import regex as rex

sys.path.append(__file__.rsplit("rhombus", 1)[0])
from futilities.aliases import function, method, generator, mappingproxy
from futilities.miscellaneous_debris import (
    DefaultObject, 
    get_name, get_name_or_str, 
    rename_function, copy_function, 
    hashproperty, classproperty, 
    g_constfunc, const_False, const_True, 
    singleton_registry, singleton_type, 
    sovereign, _ꜱᴛʀ, 
    )
from futilities import syntax_tricks
from futilities.syntax_tricks import operator_hack
from futilities import nestindextensions
from futilities.nestindextensions import (
    nested_iterable, nested_indices, 
    _get_nested_utils_typed, 
    tuplify, 
    )
from abcd.domains import (
    ABCDMeta, DomainType, DomainTypage, FuncDomainsTypage, 
    PredicateTypage, 
    MathDomainTypes, 
    Auto, Object, Oblivion, 
    Iterator, 
    ⲈXx, ⲈOʙ, ⲈOᴠ, 
    ⲈFᴄ, ⲈIᴛ, ⲈCᴛ, ⲈSᴘ, ⲈMᴘ, ⲈSવ, ⲈCʜ, ⲈVᴄ, 
    ⲈUɴ, ⲈCɴ, ⲈRɴ, ⲈQɴ, ⲈZɴ, ⲈNɴ, ⲈLᴛ, ⲈBʟ, 
    _ⲈƒxGenericAlias, Ⲉƒx, Ⲉǃǃ, 
    deduce_domain, typecheck_isinstance, typecheck_issubclass, 
    )
from futilities.functions import (
    startuple_, mulinv_, 
    not_contains_, OR_, AND_, if_else_, 
    )
from rhombus import _ᴋⲉᴙᴎ_
from rhombus._ᴋⲉᴙᴎ_ import *


__doc__ = """
Rhombus: A Flexible Symbolic Rewriting System
=============================================

Rhombus is a general-purpose symbolic expression and rewriting system
designed to represent, manipulate, and transform mathematical
expressions. It provides a flexible foundation for symbolic computation,
with an emphasis on structural generality, extensibility, and
customizable algebraic behavior, as well as string representation and 
parenthesization congruent with python syntax.

Rather than prescribing a fixed set of mathematical laws, Rhombus
separates the representation of expressions from the properties and
transformations that may be applied to them. This allows it to
accommodate a wide variety of mathematical domains, including
conventional algebraic systems, lattices, symbolic sets, and
structures with unconventional or user-defined operations.

Core components include, but are not limited to:

	class opvar:
		Represents symbolic operands, variables, parameters, and 
        constants. Supports arbitrary symbol tagging, known/unknown 
        value, domains, referents, and matching.
	
	class opfunc (opvar):
		Represents symbolic operators and functions, including 
        access to arity, input/output domains, implementations, and 
        other metadata [see opdata below].

	class opterm:
		Represents symbolic expressions as trees formed by operators 
        with their operands. Provides expression construction, structural 
        indexing, traversal, matching, replacement, parameterization, 
        evaluation, and formatting.

	class oprelation (opterm):
		Specialized `opterm` for relational expressions, with support for 
        comparisons and logical operations.

	class opdata & namespace opdata_canonical:
		Define and organize operator metadata, including formatting, 
        precedence, arity, domains, and implementations. Canonical 
        definitions provide operator information for Python syntax and 
        other operations.

Other features:

	Domain sytem (ABCDMeta & co.):
		Integrates the ABCD typing system to tag operands as belonging to a 
        given domain.  [See the peripheral abcd module for more info.]  The 
        system assists with pattern matching, and also allows for constants 
        to be cleanly 'cast' from one domain to another, translating 
        properties from one space to another without overlapping definitions 
        [see the opvar type & the rhombus.constants submodule for more]. 

	Nested Indexing:
		The opterm class is a type of nested tuple which supports nested 
        indexing, search, and traversal features.  [See the peripheral submodule, 
        futilities.nestedindextensions, for more info.]  The rewrite system 
        relies entirely on nested indexing to produce transformed expressions.
 
	Matching and Rewriting:
		Provides structural matching, equality-based matching, index discovery, 
        transformation, and replacement mechanisms. Rewrite rules can be compiled 
        into reusable rewriters and repeatedly applied until an expression 
        stabilizes or a recursion limit is reached.

    Optimization:
        In generalized tests, rhombus has consistently outperformed Sympy in 
        constructing expressions, making rewrites/replacements, and similar 
        areas by 5-10x in terms of process time.

Design Philosophy
-----------------

Rhombus prioritizes structural flexibility over assumptions about
conventional mathematical behavior. Expressions are not required to
satisfy familiar algebraic identities simply because they resemble
familiar mathematical operations.

Instead, mathematical properties and simplification rules are
introduced explicitly through the appropriate domains and rewriting
contexts. This distinction allows the system to represent any arbitrary
symbolic construction, and transform those expressions according to whatever 
identities or rules the user is able to express as {pattern: replacement} 
expression pairs.

The result is a modular symbolic framework intended to support both
traditional symbolic algebra and the exploration of more general
mathematical structures.
"""


_Dflt = DefaultObject
ꓽtupleꓸ__new__ = tuple.__new__
ꓽtupleꓸ__getitem__ = tuple.__getitem__

_wordsplit = method(rex.split, rex.compile(r"\b"))

const_NotImplemented = g_constfunc(NotImplemented)


__all__ = [] + _ᴋⲉᴙᴎ_.__all__
modulefunc, modulefuncs = g_modulefunc(__all__)

modulefuncs("DefaultObject", "_Dflt", "tuplify", 
                        "nested_iterable", "nested_indices", 
                        "ꓽtupleꓸ__new__", "ꓽtupleꓸ__getitem__", 
                        "const_NotImplemented", 
                         )

attrgetter = attrgetterᐩᐩ
itemgetter = itemgetterᐩᐩ



"⠀⠀╻┏━┛╶╼━━━━━━┓┃┣━━━━╾╴╶╼━━┓╻⠀⠀"
"⠀┃┃┃⠀     DEFINE  OP-DATA  TUPLES     ⠀┃┃┃⠀"
"⠀┃┃┃⠀            & CANONICAL  OPS           ⠀┃┃┃⠀"
"⠀⠀╹┗━━╾╴╶╼━━━━┫┃┗━━━━━━╾╴┏━┛╹⠀⠀"

@modulefunc
class opdata(tuple):
    "Data storage class for arithmetic operations."
    op: str = _tuplegetter(0, "operator symbol")
    nin: int = _tuplegetter(1, "number of inputs")
    precidence: int = _tuplegetter(2, "evaluation order")
    
    _formatter_ref: dict[tuple, Ⲉƒx] = {}
    _func_ref: dict[tuple, Ⲉƒx] = defaultdict(lambda: Undefined)
    format: Ⲉƒx = hashproperty(_formatter_ref, setter=True, deleter=False)
    func: Ⲉƒx = hashproperty(_func_ref, setter=True, deleter=False)
    
    _instances: dict[str, tuple] = {}
    def __new__(cls, symbol: str, /, nin: int=None, precidence: int=0, formatter: (Ⲉƒx | str)=None, func: Ⲉƒx=Undefined, *, _cache: bool=True):
        
        key = str(symbol)
        if _cache:
            try:  return cls._instances[key]
            except KeyError:  pass
        
        if (type(formatter) is function):
            formatter.format = formatter
            formatter.__self__ = formatter({0}, {1}, {2}, '...')
        elif isinstance(formatter, str):
            if symbol in cls._flattenable_ops:
                ǁꔷꓸᴊᴏɪɴǁ = formatter.format('', '').join
                formatter = (lambda *xyz: ǁꔷꓸᴊᴏɪɴǁ(map(str, xyz)))
            else:
                formatter = formatter.format
        else:
            if (not isinstance(formatter, type("".format))):
                raise ValueError("invalid formatter: %r" % formatter)
        
        self = ꓽtupleꓸ__new__(cls, (symbol, nin, precidence))
        cls._formatter_ref[self] = formatter
        if (func is not Undefined):
            cls._func_ref[self] = func
        
        if _cache:
            cls._instances[key] = self
        return self
    
    _flattenable_ops = ('|', '&', '^', '+', '-', '*', '/', '@', '==', '!=', '<', '>', '<=', '>=', ' is ', ' is not ', ' or ', ' and ',)
    
    def __hash__(self):  return hash(self.op)
    
    def __delete__(self):
        data = self._instances.pop(self.op)
        if (data is not self):
            self._instances[data.op] = data


@modulefunc
class opdata_canonical:
    "False class hosting a reference namespace to be left alone.  The opdata objects stored as attributes here under trailing sunder names ('invert_', 'truediv_', 'if_else_', etc.) define which ops are considered canonical.  All opdata objects are stored in the op_data_ref dictionary for general access; this is just the core set used by the system to best integrate with python syntax."
    
    def _opdata(sym: str, *args, **kwargs):
        op_data = opdata(sym, *args, **kwargs)
        def get_data(cls):  return opdata._instances[sym]
        return classproperty(get_data)
    
    getattr_ = _opdata(".", 2, 2, "{0}.{1!s}", func=builtins.getattr)
    getitem_ = _opdata("[]", 2, 2, "{0}[{1!r}]", func=operator.__getitem__)
    
    call_ = _opdata("()", None, 2, (lambda f, *xyz: f"{f}({', '.join(map(str, xyz))})"), func=operator.__call__)
    startuple_ = _opdata(", ", None, 18, (lambda *xyz: f"({', '.join(map(str, xyz))})"), func=startuple_)
    
    ident_ = _opdata("", 1, 0, "{0!s}", func=_idfunc)
    invert_ = _opdata(" ~", 1, 5, "~{0}", func=operator.__invert__)
    pos_ = _opdata(" +", 1, 5, "+{0}", func=operator.__pos__)
    neg_ = _opdata(" -", 1, 5, "-{0}", func=operator.__neg__)
    mulinv_ = _opdata(" **-1", 1, 4, "{0}**-1", func=mulinv_)
    
    bool_ = _opdata("bool", 1, 2, "bool({0!s})", func=builtins.bool)
    len_ = _opdata("len", 1, 2, "len({0!s})", func=builtins.len)
    iter_ = _opdata("iter", 1, 2, "iter({0!s})", func=builtins.iter)
    abs_ = _opdata("abs", 1, 2, "abs({0!s})", func=builtins.abs)
    floor_ = _opdata("floor", 1, 2, "floor({0!s})", func=math.floor)
    ceil_ = _opdata("ceil", 1, 2, "ceil({0!s})", func=math.ceil)
    trunc_ = _opdata("trunc", 1, 2, "trunc({0!s})", func=math.trunc)
    round_ = _opdata("round", 2, 2, "round({0!s}, {1!s})", func=builtins.round)
    divmod_ = _opdata("divmod", 2, 2, "divmod({0!s}, {1!s})", func=builtins.divmod)
    
    or_ = _opdata("|", 2, 11, "{0}|{1}", func=operator.__or__)
    and_ = _opdata("&", 2, 9, "{0}&{1}", func=operator.__and__)
    xor_ = _opdata("^", 2, 10, "{0}^{1}", func=operator.__xor__)
    add_ = _opdata("+", 2, 7, "{0} + {1}", func=operator.__add__)
    sub_ = _opdata("-", 2, 7, "{0} - {1}", func=operator.__sub__)
    mul_ = _opdata("*", 2, 6, "{0}*{1}", func=operator.__mul__)
    truediv_ = _opdata("/", 2, 6, "{0}/{1}", func=operator.__truediv__)
    pow_ = _opdata("**", 2, 4, "{0}**{1}", func=operator.__pow__)
    floordiv_ = _opdata("//", 2, 6, "{0} // {1}", func=operator.__floordiv__)
    mod_ = _opdata("%", 2, 6, "{0} % {1}", func=operator.__mod__)
    lshift_ = _opdata("<<", 2, 8, "{0} << {1}", func=operator.__lshift__)
    rshift_ = _opdata(">>", 2, 8, "{0} >> {1}", func=operator.__rshift__)
    matmul_ = _opdata("@", 2, 6, "{0} @ {1}", func=operator.__matmul__)
    
    eq_ = _opdata("==", 2, 12, "{0} == {1}", func=operator.__eq__)
    ne_ = _opdata("!=", 2, 12, "{0} != {1}", func=operator.__ne__)
    lt_ = _opdata("<", 2, 12, "{0} < {1}", func=operator.__lt__)
    gt_ = _opdata(">", 2, 12, "{0} > {1}", func=operator.__gt__)
    le_ = _opdata("<=", 2, 12, "{0} <= {1}", func=operator.__le__)
    ge_ = _opdata(">=", 2, 12, "{0} >= {1}", func=operator.__ge__)
    
    contains_ = _opdata(" in ", 2, 12, "{1} in {0}", func=operator.__contains__)
    not_contains_ = _opdata(" not in ", 2, 12, "{1} not in {0}", func=not_contains_)
    is_ = _opdata(" is ", 2, 12, "{0} is {1}", func=operator.is_)
    is_not_ = _opdata(" is ", 2, 12, "{0} is not {1}", func=operator.is_not)
    NOT_ = _opdata("not ", 1, 13, "not {0}", func=operator.__not__)
    OR_ = _opdata(" or ", 2, 15, "{0} or {1}", func=OR_)
    AND_ = _opdata(" and ", 2, 14, "{0} and {1}", func=AND_)
    if_else_ = _opdata(" if else ", 3, 16, "{0} if {2} else {1}", func=if_else_)
    
    assign_ = _opdata(":=", 2, 20, "{0!s} = {1}", func=(lambda k, v: globals().__setitem__(k, v)))
    setattr_ = _opdata(".=", 3, 20, "{0}.{1!s} = {2}", func=builtins.setattr)
    setitem_ = _opdata("[]=", 3, 20, "{0}[{1!r}] = {2}", func=operator.__setitem__)
    
    ior_ = _opdata("|=", 2, 20, "{0} |= {1}", func=operator.__ior__)
    iand_ = _opdata("&=", 2, 20, "{0} &= {1}", func=operator.__iand__)
    ixor_ = _opdata("^=", 2, 20, "{0} ^= {1}", func=operator.__ixor__)
    iadd_ = _opdata("+=", 2, 20, "{0} += {1}", func=operator.__iadd__)
    isub_ = _opdata("-=", 2, 20, "{0} -= {1}", func=operator.__isub__)
    imul_ = _opdata("*=", 2, 20, "{0} *= {1}", func=operator.__imul__)
    itruediv_ = _opdata("/=", 2, 20, "{0} /= {1}", func=operator.__itruediv__)
    ipow_ = _opdata("**=", 2, 20, "{0} **= {1}", func=operator.__ipow__)
    ifloordiv_ = _opdata("//=", 2, 20, "{0} //= {1}", func=operator.__ifloordiv__)
    imod_ = _opdata("%=", 2, 20, "{0} %= {1}", func=operator.__imod__)
    ilshift_ = _opdata("<<=", 2, 20, "{0} <<= {1}", func=operator.__ilshift__)
    irshift_ = _opdata(">>=", 2, 20, "{0} >>= {1}", func=operator.__irshift__)
    imatmul_ = _opdata("@=", 2, 20, "{0} @= {1}", func=operator.__imatmul__)
    
    ꓽͱǀ_ = _opdata("ͱ|", 1, 11, "ͱ|{0}", func=(lambda x: opfunc("ͱ")(x)))
    ꓽⲳǀ_ = _opdata("ⲳ|", 1, 11, "ⲳ|{0}", func=(lambda x: opfunc("ⲳ")(x)))
    
    ǀꕺǀ_ = _opdata("|ꕺ|", 2, 11, "{0}|ꕺ|{1}", func=(lambda p,q: opfunc("ꕺ")(p, q)))
    ǀꔷǀ_ = _opdata("|ꔷ|", 2, 11, "{0}|ꔷ|{1}", func=(lambda p,q: opfunc("ꔷ")(p, q)))
    
    del _opdata
    
    opsyms: tuple[str] = tuple(opdata._instances)
    ops_map: dict[str, opdata] = {}

opdata_canonical.ops_map = mappingproxy(
    {k: v for k,v in opdata_canonical.__dict__.items() if (type(v) is opdata)})


#print('", "'.join(opdata_canonical.__dict__))
("getattr_", "getitem_", "call_", "comma_", "ident_", "invert_", "pos_", "neg_", "mulinv_", "len_", "iter_", "abs_", "floor_", "ceil_", "trunc_", "round_", "divmod_", "or_", "and_", "xor_", "add_", "sub_", "mul_", "truediv_", "pow_", "floordiv_", "mod_", "lshift_", "rshift_", "matmul_", "eq_", "ne_", "lt_", "gt_", "le_", "ge_", "in_", "not_in_", "is_", "is_not_", "NOT_", "OR_", "AND_", "if_else_", "assign_", "setattr_", "setitem_", "ior_", "iand_", "ixor_", "iadd_", "isub_", "imul_", "itruediv_", "ipow_", "ifloordiv_", "imod_", "ilshift_", "irshift_", "imatmul_", )


op_data_ref = opdata._instances
modulefunc("op_data_ref")




"⠀⠀╻┏━┛╶╼━━━━━━┓┃┣━━━━╾╴╶╼━━┓╻⠀⠀"
"⠀┃┃┃⠀          DEFINE  FACTORIES,           ⠀┃┃┃⠀"
"⠀┃┃┃⠀       TEMPLATES, & PROXIES        ⠀┃┃┃⠀"
"⠀┃┃┃⠀     for  SYMBOLIC  METHODS      ⠀┃┃┃⠀"
"⠀⠀╹┗━━╾╴╶╼━━━━┫┃┗━━━━━━╾╴┏━┛╹⠀⠀"

ᐝꭘꔷɂ = DefaultObject


def _define_symbolic_opmethod(cls, name: str, op: str, nin: int=_Dflt, codomain: type=Auto, include_reverse: bool=False, rname: str=None, doc: str=_Dflt, assign_to_class: bool=False) -> (function|tuple[function, function]):
    "Define and return a new opmethod."
    if assign_to_class and (cls is ᐝꭘꔷɂ):
        cls = assign_to_class
    if (nin is _Dflt):
        nin = opdata_get(op).nin
    ǁᴏᴘǁ = op
    ǁᴅᴏᴍᴀɪɴǁ = deduce_domain(codomain)
    if (nin == 1):
        def __ᴏᴘ__(self):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(ǁᴏᴘǁ, self, domain=ǁᴅᴏᴍᴀɪɴǁ)
        include_reverse = False
    elif (nin == 2):
        if (ǁᴅᴏᴍᴀɪɴǁ is Auto):
            def __ᴏᴘ__(self, other):
                if (not self._op_eval_check(other)):  return NotImplemented
                return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(ǁᴏᴘǁ, self, other)
        else:
            def __ᴏᴘ__(self, other):
                if (not self._op_eval_check(other)):  return NotImplemented
                return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(ǁᴏᴘǁ, self, other, domain=ǁᴅᴏᴍᴀɪɴǁ)
    else:
        def __ᴏᴘ__(self, *args):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(ǁᴏᴘǁ, self, *args, domain=ǁᴅᴏᴍᴀɪɴǁ)
    rename_function(__ᴏᴘ__, name, alter_localnames=True, doc=doc, ǁᴏᴘǁ=ǁᴏᴘǁ)
    if assign_to_class:
        type.__setattr__(cls, name, __ᴏᴘ__)
    if include_reverse:
        if (ǁᴅᴏᴍᴀɪɴǁ is Auto):
            def __rᴏᴘ__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(ǁᴏᴘǁ, other, self)
        else:
            def __rᴏᴘ__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(ǁᴏᴘǁ, other, self, domain=ǁᴅᴏᴍᴀɪɴǁ)
        if (rname is None):
            rname = "{0}r{1}{2}".format(name.partition(name.strip("_")))
        rename_function(__rᴏᴘ__, rname, alter_localnames=True, doc=doc, ǁᴏᴘǁ=ǁᴏᴘǁ)
                                                                                #ǁᴅᴏᴍᴀɪɴǁ=get_name(ǁᴅᴏᴍᴀɪɴǁ))
        if assign_to_class:
            type.__setattr__(cls, rname, __rᴏᴘ__)
        return __ᴏᴘ__, __rᴏᴘ__
    return __ᴏᴘ__

def _generate_defined_symbolic_opmethods(cls, names_and_ops: list[str], nin: int=_Dflt, codomain: type=Auto, include_reverses: bool=False, assign_to_class: bool|type=False) -> generator:
    if assign_to_class and (cls is ᐝꭘꔷɂ):
        cls = assign_to_class
    _def = define_symbolic_opmethod.__func__
    definer = (lambda name, op: _def(cls, name, op, nin, codomain, include_reverses, assign_to_class))
    return (definer(name, op) for name, op in names_and_ops)


def _define_symbolic_proxied(cls, proxymethod: str, name: str, joiner: str|Ⲉƒx=None, codomain: type=Auto, doc: str=None, as_property=False, assign_to_class: bool|type=False) -> function:
    "Proxymethods include:  ._getattr_(),  ._methodcall_(),  and  ._functioncall_()\n"\
    "The ʻjoinerʼ is either the str attribute name or presumedly callable object which "\
    "the new method is defined by.  For _getattr_ and _methodcall_, it can be left None "\
    "and will default to the same as the name of the method, ʻnameʼ."
    if (proxymethod not in ("_getattr_", "_methodcall_", "_functioncall_")):
        raise ValueError('proxymethod must be one of ("_getattr_", "_methodcall_", "_functioncall_")')
    if assign_to_class and (cls is ᐝꭘꔷɂ):
        cls = assign_to_class
    if (joiner is None):
        joiner = name
    ǁᴘʀᴏxʏǁ, ǁᴊᴏɪɴᴇʀǁ, ǁᴅᴏᴍᴀɪɴǁ = proxymethod, joiner, codomain
    ǂᴄʟꜱǂ = cls
    if (doc is None):
        doc = getattr(ǁᴊᴏɪɴᴇʀǁ, "__doc__", None) if (ǁᴘʀᴏxʏǁ == "_functioncall_") else None
    def __ᴏᴘ__(self, *args, domain: type=ǁᴅᴏᴍᴀɪɴǁ, **kwargs):
        return self.ǁᴘʀᴏxʏǁ(ǁᴊᴏɪɴᴇʀǁ, *args, domain=domain, **kwargs)
    #('', ["ǁᴊᴏɪɴᴇʀǁ:=", ("ǁᴊᴏɪɴᴇʀǁ" if (ǁᴘʀᴏxʏǁ == "_functioncall_") else ǁᴊᴏɪɴᴇʀǁ)], *vars().items(), '', sep="\n    ")
    rename_function(__ᴏᴘ__, name, alter_localnames=True, doc=doc, 
                                    ǁᴘʀᴏxʏǁ=ǁᴘʀᴏxʏǁ, 
                                    ǁᴊᴏɪɴᴇʀǁ=("ǁᴊᴏɪɴᴇʀǁ" if (ǁᴘʀᴏxʏǁ == "_functioncall_") else ǁᴊᴏɪɴᴇʀǁ))
                                    #ǁᴅᴏᴍᴀɪɴǁ=("None" if (ǁᴅᴏᴍᴀɪɴǁ is None) else ǁᴅᴏᴍᴀɪɴǁ.__name__))
    if as_property: #and (ǁᴘʀᴏxʏǁ == "_getattr_"):
        __ᴏᴘ__ = property(__ᴏᴘ__)
    if assign_to_class:
        type.__setattr__(cls, name, __ᴏᴘ__)
    return __ᴏᴘ__


def _defsym_getattr_(cls, name: str, *, codomain: type=Auto, **kwargs):
    return _define_symbolic_proxied(cls, "_getattr_", name, codomain=codomain, **kwargs)
def _defsym_methodcall_(cls, name: str, *, codomain: type=Auto, **kwargs):
    return _define_symbolic_proxied(cls, "_methodcall_", name, codomain=codomain, **kwargs)
def _defsym_functioncall_(cls, name: str, func: Ⲉƒₓ, *, codomain: type=Auto, **kwargs):
    return _define_symbolic_proxied(cls, "_functioncall_", name, func, codomain=codomain)


define_symbolic_opmethod = method(_define_symbolic_opmethod, ᐝꭘꔷɂ)
generate_defined_symbolic_opmethods = method(_generate_defined_symbolic_opmethods, ᐝꭘꔷɂ)
define_symbolic_proxied = method(_define_symbolic_proxied, ᐝꭘꔷɂ)
defsym_getattr_ = method(_defsym_getattr_, ᐝꭘꔷɂ)
defsym_methodcall_ = method(_defsym_methodcall_, ᐝꭘꔷɂ)
defsym_functioncall_ = method(_defsym_functioncall_, ᐝꭘꔷɂ)

modulefuncs("define_symbolic_opmethod", "generate_defined_symbolic_opmethods", 
                         "define_symbolic_proxied", 
                         "defsym_getattr_", "defsym_methodcall_", "defsym_functioncall_")





"⠀⠀╻┏┛╶╼━━━━━━━┓┃┣━━━━╾╴╶╼━━┓╻⠀⠀"
"⠀┃┃┃⠀      DEFINE  CORE-SYMBOLIC      ⠀┃┃┃⠀"
"⠀⠀╹┗━━╾╴╶╼━━━━┫┃┗━━━━━━━╾╴┏┛╹⠀⠀"

@modulefunc
class _core_symbolic(_base_atomic):
    """
    Base class for symbolic objects.  Where enclosing algebraic methods are defined.
    """
    
    op_eval_priority: int = 0
    
    def _op_eval_check(self, other):
        "Returns True unless (self ꕺ other) should defer to othsr.__rꕺ__ methods."
        try:  return (other.op_eval_priority <= self.op_eval_priority)
        except AttributeError:  return True
    
    
    def __format__(self, fspec: str=""):
        if (fspec.endswith(')')):  return get_nameᐩ(self).__format__(fspec.removesuffix(')'))
        return super().__format__(fspec)
    
    def __format__(self, fspec: str=""):
        strf = str
        if fspec.startswith('!'):
            strf = {'r':repr, 's':str, 'n':get_name, 'm':get_name_or_str}[fspec[1]]
            fspec = fspec[2:]
        string = strf(self)
        if fspec.endswith(')'):
            fspec = fspec.removesuffix(')')
            if not (string.isidentifier() and self.depth):
                string = f"({string})"
                if (' ' in string) and (self.depth >= 1) \
                and (not {'not', ' or', 'and', 'is', 'in', 'if', 'else'}.intersection(_wordsplit(string))):
                    string = string.replace(' ', '')
        return string.__format__(fspec)
    
    
    _define_symbolic_opmethod = classmethod(_define_symbolic_opmethod)
    _generate_defined_symbolic_opmethods = classmethod(_generate_defined_symbolic_opmethods)
    _define_symbolic_proxied = classmethod(_define_symbolic_proxied)
    
    _defsym_getattr_ = classmethod(_defsym_getattr_)
    _defsym_methodcall_ = classmethod(_defsym_methodcall_)
    _defsym_functioncall_ = classmethod(_defsym_functioncall_)
    
    def _as_op_(self, *args, **kwargs):
        "Return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ expression with self as the joining operation.  May raise errors if self is not an opfunc."
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(self, *args, **kwargs)
    
    def _functioncall_(self, func: Ⲉƒx, *args, **kwargs):
        "Return a call expression with self as the first argument:  func(self, *args)"
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("()", func, self, *args, **kwargs)
    def _methodcall_(self, name: str, *args, **kwargs):
        "Return a call expression on a method bound to self:  self.<name>(*args)"
        return self._getattr_(name)(*args, **kwargs)
    
    def _getattr_(self, name: str, **kwargs):
        "Symbolic version of .__getattribute__(), or more accurately, the dot '.' operator.  Of the Big 3 visceral ops ('.', '()', '[]'), <getattr> is the most sensitive.  When defining a .__getattribute__() method, using this as a fallback is not forbidden like ._eq_() is for .__eq__(), but should only be done within strict bounds.  Preferrably, self.__getattribute__(name) should never return a symbolic if (type(name) is str), because a lot of this module relies on AttributeError propogating normally.  For things like x.denominator, z.real, etc., they should be defined explicitely and call on the bisunder directly, like:"'''
        >>>     @property
        >>>     def numerator(self):  return self._getattr_('numerator', domain=ⲈZɴ)
        '''
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(".", self, name, **kwargs)
    
    def _getitem_(self, key, **kwargs):
        "The most dynamic of the Big 3, <getitem> serves many roles in both symbolic & literal contexts.  The expression class, opterm, is a kind of nested tuple, and implements indexing as such, with nested indexing behaving similarly to that of numpy ndarrays, which the raw _cmp_transform() function uses to quickly and efficiently grab and restructure subterms into rewritten expressions (the types accepted are (list|slice|tuple|int) & nested permutations thereupon (though generally list[tuple[int|slice]]), plus allowance for (None|...|NotImplemented)).  Indexing is also used to apply domain specifiers to a symbolic unknown or generalized const value.  "
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("[]", self, key, **kwargs)
    
    def _call_(self, *args, **kwargs):
        "Of the Big 3, <call> is the most stable, and can usually be assigned directly to the .__call__() dunder like any of the more common arithmetics.  The only hard-coded special symbolic use for this operation is for the set of canonically recognized opfunc instances to construct expressions directly with themself as the joining operator."
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("()", self, args, **kwargs)
    
    @property
    def numerator(self):
        return self._getattr_("numerator", domain=ⲈZɴ)
    @property
    def denominator(self):
        return self._getattr_("denominator", domain=ⲈZɴ)
    @property
    def real(self):
        return self._getattr_("real", domain=ⲈRɴ)
    @property
    def imag(self):
        return self._getattr_("imag", domain=ⲈRɴ)
    
    conjugate = defsym_methodcall_("conjugate", codomain=ⲈCɴ)
    
    _len_ = defsym_functioncall_("__len__", len, codomain=ⲈNɴ)
    _iter_ = defsym_functioncall_("__iter__", iter, codomain=Iterator)
    
    index = defsym_methodcall_("index", codomain=ⲈNɴ)
    count = defsym_methodcall_("count", codomain=ⲈNɴ)
    
    isdisjoint = defsym_methodcall_("isdisjoint", codomain=Ⲉǃǃ)
    issuperset = defsym_methodcall_("issuperset", codomain=Ⲉǃǃ)
    issubset = defsym_methodcall_("issubset", codomain=Ⲉǃǃ)
    issuperset_strict = defsym_methodcall_("issuperset_strict", codomain=Ⲉǃǃ)
    issubset_strict = defsym_methodcall_("issubset_strict", codomain=Ⲉǃǃ)
    
    union = defsym_methodcall_("union", codomain=ⲈSᴘ)
    intersection = defsym_methodcall_("intersection", codomain=ⲈSᴘ)
    symmetric_difference = defsym_methodcall_("symmetric_difference", codomain=ⲈSᴘ)
    difference = defsym_methodcall_("difference", codomain=ⲈSᴘ)
    
    def __abs__(self):
        return self._functioncall_(_ꓽƒ(abs))
    def __floor__(self):
        return self._functioncall_(_ꓽƒ(floor))
    def __ceil__(self):
        return self._functioncall_(_ꓽƒ(ceil))
    def __trunc__(self):
        return self._functioncall_(_ꓽƒ(trunc))
    
    def __round__(self, ndigits: int=0):
        return self._functioncall_(_ꓽƒ(round), ndigits)
    
    def __invert__(self):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" ~", self)
    def __pos__(self):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" +", self)
    def __neg__(self):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" -", self)
    def _mulinv_(self):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" **-1", self)
    
    def __or__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("|", self, other)
    def __and__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("&", self, other)
    def __xor__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("^", self, other)
    def __lshift__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("<<", self, other)
    def __rshift__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(">>", self, other)
    def __matmul__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("@", self, other)
    def __add__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("+", self, other)
    def __sub__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("-", self, other)
    def __mul__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("*", self, other)
    def __truediv__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        if __is__(self.value, +1):  return _core_symbolic._mulinv_(other)
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("/", self, other)
    def __pow__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        if __is__(other, -1):  return self._mulinv_()
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("**", self, other)
    def __floordiv__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("//", self, other)
    def __mod__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("%", self, other)
    
    def __divmod__(self, other):
        dom = min(domain, self.domain, get_domain(other))
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(", ", self.__floordiv__(other, domain=dom), 
                                              self.__mod__(other, domain=dom), 
                                              domain=ⲈSવ[dom])
    
    def __ror__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("|", other, self)
    def __rand__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("&", other, self)
    def __rxor__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("^", other, self)
    def __rlshift__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("<<", other, self)
    def __rrshift__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(">>", other, self)
    def __rmatmul__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("@", other, self)
    def __radd__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("+", other, self)
    def __rsub__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("-", other, self)
    def __rmul__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("*", other, self)
    def __rtruediv__(self, other):
        if __is__(other, +1):  return self._mulinv_()
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("/", other, self)
    def __rpow__(self, other):
        if __is__(self.value, -1):  return _core_symbolic._mulinv_(other)
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("**", other, self)
    def __rfloordiv__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("//", other, self)
    def __rmod__(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("%", other, self)
    
    def __rdivmod__(self, other):
        dom = min(self.domain, get_domain(other))
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(", ", self.__rfloordiv__(other, domain=dom), 
                                              self.__rmod__(other, domain=dom), 
                                              domain=ⲈSવ[dom])
    
    def _startuple_(self, *xyz):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(", ", self, *xyz, domain=ⲈSવ[Auto])
    @classmethod
    def _itertup_(cls, xyz: ⲈSવ=()):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(", ", *xyz, domain=ⲈSવ[Auto])
    
    
    def _bool_(self):  return self._functioncall_(_ꓽƒ(bool), domain=Ⲉǃǃ)
    
    def _eq_(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("==", self, other, domain=Ⲉǃǃ)
    def _ne_(self, other):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("!=", self, other, domain=Ⲉǃǃ)
    def __lt__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("<", self, other, domain=Ⲉǃǃ)
    def __gt__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(">", self, other, domain=Ⲉǃǃ)
    def __le__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("<=", self, other, domain=Ⲉǃǃ)
    def __ge__(self, other):
        if (not self._op_eval_check(other)):  return NotImplemented
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(">=", self, other, domain=Ⲉǃǃ)
    
    def _contains_(self, other):
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" in ", self, other, domain=Ⲉǃǃ)
    
    def _getattribute_(self, name: str):
        "If you want a class to return a call to symbolic _getattr_(self, name) instead of raising AttributeError, you_can replace its .__getattribute__() method with this temporarily, but it is strongly suggested that you only do so under limited contexts.  A safer, more permanent version might implement a simple <contains> predicate to allow only a subset of possible names to return symbolic instances, and could easily be made from scratch."
        try:  return object.__getattribute__(self, name)
        except AttributeError: return self._getattr_(name)
    
    def __getitem__(self, key):
        if isinstance(key, ABCDMeta):  return type(self)(self, value=self, domain=key)
        return self._getitem_(key)
    
    def __call__(self, *args, **kwargs):  return self._call_(*args, **kwargs)





"⠀⠀╶╼━━━━━╾╴╶╼━━╾╴⠀⠀"
"⠀╶╼┳━━━╾╴╶╼━━━━┳╾╴⠀"
"⠀⠀⠀┃      Try-Getters    ┃⠀⠀⠀"
"⠀╶╼┻━━━━╾╴╶╼━━━┻╾╴⠀"
"⠀⠀╶╼━━╾╴╶╼━━━━━╾╴⠀⠀"

@modulefunc
def get_value(ob):
    "Tries to retrieve  ob.value,  defaulting to  ob  if no such name exists."
    try:  return ob.value
    except AttributeError:  return ob
@modulefunc
def get_domain(ob, /, allow_auto: bool=False):
    "Tries to retrieve  ob.domain,  defaulting to  deduce_domain(ob)  if no such name exists."
    try:
        domain = ob.domain
    except AttributeError:  pass
    else:
        if (domain is not Auto) or allow_auto:  return domain
        val = get_referent(ob, True)
        if (val is Unknown) and (val is not ob):  return Object
    return deduce_domain(ob)

@modulefunc
def get_referent(ob, /, allow_unfinites: bool|int=False, *, _ob: object=None):
    "Returns get_value(get_value(...(ob)) recursively.  Unless ʻallow_unfinitesʼ == +1 (default:=False|0), if get_value(ob) is Unknown or Undefined, ʻobʼ is returned instead.  If allow_unfinites == -1 and the value is unfinite, ob is only returned if it is not the original input."
    if (_ob is None):
        _ob = ob
    try:
        val = ob.value
    except AttributeError:  return ob
    else:
        if isunfinite(val):
            if (not allow_unfinites):  return ob
            if (allow_unfinites < 0):  return (val if (ob is _ob) else ob)
            return val
        return get_referent(val, allow_unfinites=allow_unfinites, _ob=_ob)
@modulefunc
def get_referent_symbolic(ob, *, _ob: object=None):
    "Returns the 2nd-to-bottommost referent of a symbolic object.  If ʻobʼ is not a symbolic, returns None."
    try:  return get_referent_symbolic(ob.value, _ob=ob)
    except AttributeError:  return _ob


@modulefunc
def get_op(ob):
    "Retrieves  ob.op  for arbitrary ob (default ==> '')."
    try:  return ob.op
    except AttributeError:  return opdata._instances[""].op
@modulefunc
def get_op_data_ob(ob):
    "Retrieves  ob.op.op_data  for arbitrary ob (default ==> opdata(''))."
    try:  return ob.op.op_data
    except AttributeError:  return opdata._instances[""]
@modulefunc
def get_op_nin(ob):
    "Retrieves  ob.op.nin  for arbitrary ob (default ==> 1)."
    try:  return ob.nin
    except AttributeError:  pass
    try:  return ob.op.nin
    except AttributeError:  return 1
@modulefunc
def get_op_precidence(ob):
    "Retrieves  ob.op.precidence  for arbitrary ob (default ==> 0)."
    try:  return ob.precidence
    except AttributeError:  pass
    try:  return ob.op.precidence
    except AttributeError:  return 0





"⠀╶╼━━━━━━╾╴╶╼━━╾╴⠀"
"⠀    Indices/Items Getters  ⠀"
"⠀╶╼━━╾╴╶╼━━━━━━╾╴⠀"

_itemget_ǀꓽꓽᐨ1ǀ = itemgetter(slice(None, None, -1))
_itemget_ǀ1ꓽǀ = itemgetter(slice(1, None))
_itemget_ǀ0ꓹ1ꓽǀ = itemgetter(0, slice(1, None))
#_itemget_ǀ0ꓽᐨ1ꓹᐨ1ǀ = itemgetter(slice(0, -1), -1)
ǀꓽꓽǀ = slice(None)
NoneType, EllipsisType = type(None), type(...)

_nested_utils_vars = _get_nested_utils_typed(tuple)

get_indicesꓹitems, get_indices, get_items = itemgetter(\
"get_indicesꓹitems_b", "get_indices_b", "get_items_b"\
)(_nested_utils_vars)



"⠀╶╼━━━━━━╾╴╶╼━━╾╴⠀"
"⠀        Property Getters ⠀⠀⠀"
"⠀╶╼━━╾╴╶╼━━━━━━╾╴⠀"

get_depth = _nested_utils_vars["get_depth"]
get_size = _nested_utils_vars["get_size"]

modulefuncs('get_indices', 'get_items', 'get_indicesꓹitems', 'get_depth', 'get_size')


KVǀKǀV_PredicateTypage = \
        ( Ⲉƒx[[ (ⲈSવ[ⲈSવ[ ...], ⲈOʙ]) ], ⲈOʙ] \
                      | Ⲉƒx[[ (ⲈSવ[ⲈZɴ, ...]) ], ⲈOʙ] \
                                    | Ⲉƒx[[ (ⲈOʙ) ], ⲈOʙ] )

ǀKV_PredicateTypage, ǀK_PredicateTypage, ǀV_PredicateTypage = KVǀKǀV_PredicateTypage.__args__

@modulefunc
@lru_cacheᐩᐩ
def get_operand_elements(tup: nested_iterable, *, unique: bool=True, include_ops: bool=False, include_operands: bool=True, item_predicate: PredicateTypage=None):
    gen = _get_operand_elements(tup, include_ops, include_operands, item_predicate)
    if unique:
        gen = unique_everseen(gen)
    return tuple(gen)
def _get_operand_elements(tup: nested_iterable, include_ops: bool, include_operands: bool, item_predicate: PredicateTypage=None):
    for index, item in enumerate(tup):
        if (not index):
            if include_ops and ((item_predicate is None) or item_predicate(item)):  yield item
            continue
        if (not isinstance(item, tuple)):
            if include_operands and ((item_predicate is None) or item_predicate(item)):  yield item
        else:  yield from _get_operand_elements(item, include_ops, include_operands, item_predicate)


@modulefunc
def itempredicateꓽob_is_var(ob: _math_ob):
    "Quick predicate to check if ob is a symbol whose referent is Unknown."
    return isinstance(ob, opvar) and (ob.referent_value is Unknown)
@modulefunc
def itempredicateꓽob_is_const(ob: _math_ob):
    "Quick predicate to check if ob is a non-symbol, or one whose referent is not Unknown."
    return (get_referent(ob, allow_unfinites=True) is not Unknown)

@modulefunc
@lru_cacheᐩᐩ
def get_vars(tup: nested_iterable, *, unique: bool=True, include_ops: bool=False, include_operands: bool=True):
    gen = _get_operand_elements(tup, include_ops, include_operands, itempredicateꓽob_is_var)
    if unique:  return tuple(unique_everseen(gen))
    return tuple(gen)
@modulefunc
@lru_cacheᐩᐩ
def get_consts(tup: nested_iterable, *, unique: bool=True, include_ops: bool=False, include_operands: bool=True):
    gen = _get_operand_elements(tup, include_ops, include_operands, itempredicateꓽob_is_const)
    if unique:  return tuple(unique_everseen(gen))
    return tuple(gen)

@modulefunc
@lru_cacheᐩᐩ
def get_operands(tup: nested_iterable, *, unique: bool=False, include_operators: bool=False):
    gen = _get_operand_elements(tup, include_operators, True, None)
    if unique:  return tuple(unique_everseen(gen))
    return tuple(gen)
def _get_operands_true(tup: nested_iterable):
    for item in _itemget_ǀ1ꓽǀ(tup):
        if (not isinstance(item, tuple)):  yield item
        else:  yield from _get_operands_true(item)

@modulefunc
@lru_cacheᐩᐩ
def get_operators(tup: nested_iterable, *, unique: bool=False, include_operands: bool=False):
    gen = _get_operators(tup, include_operands)
    if unique:  return tuple(unique_everseen(gen))
    return tuple(gen)
def _get_operators(tup: nested_iterable, include_operands: bool):
    yield tup[0]
    for item in _itemget_ǀ1ꓽǀ(tup):
        if isinstance(item, tuple):  yield from _get_operators(item, include_operands)
        elif include_operands:  yield item


@sovereign(base=list, nullify_methods=True, nullify_mutable_methods=True, ignore=['sort', 'reverse'])
class _static_list(list):
    def reorder(self, new_order: list|tuple):
        try:
            list.sort(self, key=new_order.index)
        except ValueError:
            new_order = tuple(map(self.__getitem__, new_order))
            try:
                list.sort(self, key=new_order.index)
            except ValueError:
                raise ValueError("new order must match either the contents or the indices of the target list")
        return self

#l = _static_list('abcba')
#print(f"\n{l = }\n{l.reorder([2,3,0,1,4]) = }\n{l = }")
#print(f"\n{l = }\n{l.reorder(range(5)) = }\n{l = }")
#l = _static_list('abcde')
#print(f"\n{l = }\n{l.reorder([2,3,0,1,4]) = }\n{l = }")
#print(f"\n{l = }\n{l.reorder([2,3,0,1,0]) = }\n{l = }")





"⠀⠀╶╼━┳━━━━━╾╶╼━┳━╾╴⠀⠀"
"⠀╶╼┳━┛┏━━╾╴╶╼━┓┗━┳╾╴⠀"
"⠀⠀⠀┃          OPTERM          ┃⠀⠀⠀"
"⠀╶╼┻━┓┗━╾╴╶╼━━┛┏━┻╾╴⠀"
"⠀⠀╶╼━┻━╾╴╶╼━━━━┻━╾╴⠀⠀"

@modulefunc
class opterm(_core_symbolic, tuple):
    "Basic expression object.  As a tuple, opterm supports nested getitem, indexing, contains and replace functionality, as well as access to depth, size, and indexing layout via properties.  As an expression, each opterm is structured as (op, *args), representing op(*args), or an n-ary function call."
    
    depth: int = property(get_depth, \
                            doc="The depth of the most nested subtuple.")
    indices: list[bytes] = property(get_indices, \
                            doc="Standard nested indices such that  self[indices] would reconstruct self.")
    items: list = property(get_items, \
                            doc="Nested items as a list, not including subnests.")
    indicesꓹitems: list = property(get_indicesꓹitems, \
                            doc="Nested (index, item) pairs like enumerate.")
    size: int = property(get_size, \
                            doc="Number of all non-iterable objects within.")
    
    _kwdefs = {'flat':True,'skip_nests':False}
    get_indices: function = copy_function(get_indices, kwdefaults=_kwdefs)
    get_items: function = copy_function(get_items, kwdefaults=_kwdefs)
    get_indicesꓹitems: function = copy_function(get_indicesꓹitems, kwdefaults=_kwdefs)
    del _kwdefs
    
    op: str = _tuplegetter(0, "operator or function")
    args: tuple = property(_itemget_ǀ1ꓽǀ, "operands or subterms")
    
    x: _math_ob = _tuplegetter(1, "unary arg, or n-ary 1st operand")
    ʟ: _math_ob = _tuplegetter(1, "binary left side, or n-ary leftmost operand")
    ʀ: _math_ob = _tuplegetter(2, "binary right side, or n-ary 2nd operand")
    
    
    _value_ref: dict[tuple, object] = defaultdict(lambda: Unknown)
    _domain_ref: dict[tuple, DomainType] = defaultdict(lambda: Auto)
    
    value: object = hashproperty(_value_ref, False, False)
    domain: DomainType = hashproperty(_domain_ref, False, False)
    
    @value.setter
    def value(self, value: object):
        self._value_ref[self] = value
        if (not isunfinite(value)):
            self._domain_ref[self] = deduce_domain(value)
    @domain.setter
    def domain(self, domain: DomainType):
        if (not typecheck_isinstance(domain, DomainType)):
            domain = deduce_domain(domain)
        value = self.value
        if isunfinite(value) or (value in domain) or (get_domain(value) < domain):
            self._domain_ref[self] = domain
        else:  raise ValueError("value not in domain: ({value!r} ∉ {domain})")
         #⊗ⅅⅆⅇⅈⅉ∈∉∋∌⊇⊉⊆⊈⊃⊅⊂⊄∪∩⊖△ᒾ
    
    
    _variables_ref = {}
    _varorder: list = hashproperty(_variables_ref, setter=True, deleter=False)
    def get_variables(self):
        "(<opterm>.variables is mutable to facilitate the .parametrize method)"
        try:  return self._varorder
        except KeyError:  pass
        self._varorder = variables = _static_list(get_vars(self))
        return variables
    def set_variables(self, new_order: list[str]):
        existing_order = self.get_variables()
        #if (len(new_order) < len(existing_order)):  raise ValueError("number of variables must ")
        #elif (set(new_order) != set(existing_order)):  raise ValueError("set of symbols must match")
        self._varorder.sort(key=new_order.index)
    
    operands: tuple[ⲈOʙ] = property(get_operands)
    variables: tuple[_core_symbolic] = property(get_variables, set_variables, doc="The expression’s named unknown variables or parameters in-order as a mutable list.  Can be sorted or updated using the assignment (=) operator.")
    constants: tuple[ⲈOʙ] = property(get_consts)
    operators: tuple[Ⲉƒx] = property(get_operators)
    
    
    @classmethod
    def from_iterable(cls, iterable: ⲈIᴛ):  return cls(*iterable)
    
    _instances: dict = {}
    def __new__(cls, op: str, *args, value: object=Unknown, domain: DomainType=Auto):
        #if (not args) and (op not in opfunc._instances):  return opvar(op, value=value, domain=domain)
        if (op == ""):  return opvar(*args, value=value, domain=domain)
        if op_ok := (op == "()"):
            f, xyz = _itemget_ǀ0ꓹ1ꓽǀ(args)
            if op_ok := (type(f) is opfunc) and str.isidentifier(f):
                op = f
                args = xyz
        
#        key = (op, tuplify(args, item_wrapper=lambda x: (x, get_domain(x)))) ❌ makes all 30x slower
        key = (op, args, tuple(map(get_domain, args)))
        try:  return cls._instances[key]
        except KeyError:  pass
        
        if (not op_ok):
            try:
                op = opfunc._instances[op]
            except KeyError:
                if type(op) is not opvar:  raise
        
        if (cls is opterm) and (op in ("== != >= <=")):
            return oprelation(op, *args, value=value)
        
        self = ꓽtupleꓸ__new__(cls, (op, *args))
        
        if (domain is not Auto):
            self.domain = domain or Object
        if (value is not Unknown):
            self.value = value
        
        cls._instances[key] = self
        return self
    
    def __format__(self, fspec: str=''):
        op = self.op
        strf = repr
        if ('!' in fspec):
            strfcode, fspec = fspec.split('!', 1)
            if (strfcode == "s"):
                strf = str
            elif (strfcode == "r"):
                strf = repr
            elif (strfcode == "a"):
                strf = ascii
        if fspec.endswith(')'):
            fspec = fspec.removesuffix(')')
            string = op.get_string(*self.args, strf=strf, outer_op=(op not in (2, 20)))
        else:
            string = op.get_string(*self.args, strf=strf)
        return format(string, fspec)
    
    def _reprcheck(self):
        argsdomains = {x._reprcheck() for x in self.args if isinstance(x, (opterm, opvar))} - {False}
        if (not argsdomains):  return False
        if (len(argsdomains) == 1):  return argsdomains.pop()
        return argsdomains
    
    def __repr__(self):
        op = self.op
        return op.get_string(*self.args, strf=repr)
#        args = self.args
#        argsdomains = self._reprcheck()
#        if argsdomains and (type(argsdomains) is not set):
#            string = op.get_string(*args, strf=str, outer_op="[]")
#            string = f"{string}[{argsdomains}]"
#        else:
#            string = op.get_string(*self.args, strf=repr)
#        print(argsdomains, string)
#        return string
    
    def __str__(self):
        op = self.op
        return op.get_string(*self.args, strf=str)
    
    __hash__ = tuple.__hash__
    
    def __contains__(self, other):
        return (self == other) or nested_iterable.__contains__(self, other)
    
    def __getitem__(self, indices):
        #print(f">>> opterm.__getitem__(..., {indices})")
        T = type(indices)
        if T in (slice, int):
            item = ꓽtupleꓸ__getitem__(self, indices)
        elif (T is bytes):
            if (not indices):  return ()
            item = self
            for index in (indices):
                #print(f"({item=})    [{index=}]    [{indices=}]")
                item = item[index]
            return item
        elif (T is tuple):
            if (not indices):  return ()
            item = self
            for index in (indices):
                if (type(index) is slice):# and isinstance(item, (tuple)):
                    indices_remaining = tuple(indices_iter)
                    item = tuple(item[l][indices_remaining] for l in range(*index.indices(len(item))))
                    break
                #print(f"({item=})    [{index=}]    [{indices=}]")
                item = item[index]
            return item
        elif (T is list) or (T is nested_indices):
            if (not indices):  return ()
            if (indices[-1] is None):
                if ni := indices.index(None):
                    indices = indices[:ni]
            item = tuple(map(self.__getitem__, indices))
#        elif (indices is ...):  return ꓽtupleꓸ__new__ǁoptermǁ((", ", self,))
        elif (indices is None) or (indices == ǀꓽꓽǀ):  return self
        elif issubclass(T, _core_symbolic):  return self._getitem_(indices)
        elif (indices is NotImplemented):  return NotImplemented
        elif typecheck_issubclass(T, DomainTypage):
            return tuplify(self, item_wrapper=lambda x: (x[indices] if (type(x) is opvar) else x), 
                                    tuplify_as=opterm.from_iterable)
        elif (T is dict):  return self.replacements(indices)
        else:  raise IndexError(vars())
        if (type(item) is tuple):
            try:  return opterm._instances[*item]
            except KeyError:  pass
            if item and (type(item[0]) is opfunc):
                nin = item[0].nin
                if (nin is None) or ((len(item) - 1) >= nin):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(*item) 
        return item
    
    
    def index(self, other, count: int=0):
        gen = (i for i, x in get_indicesꓹitems(self, flat=True, skip_nests=False) if (other==x))
        index = next(gen, NotImplemented)
        for _ in range(count):
            index = next(gen, NotImplemented)
        return index
        return indexes[count] if indexes else NotImplemented
    
    def indexes(self, value, /, eq_func: Ⲉƒx=None, **kwargs):
        "Generates all nested indices where ‘value’ can be found."
        eq_method = value.match if (eq_func is None) else memmethod(eq_func, value)
        return list(self._indexes(eq_method, **kwargs))
    def _indexes(self, eq_method: method, flat=True, skip_nests=False, **kwargs):
        if eq_method(self):  yield None
        gen = get_indicesꓹitems(self, flat=flat, skip_nests=skip_nests, **kwargs)
        for index, item in gen:
            if eq_method(item):  yield index
    
    def match(self, other, *, _matched: dict=None):
        #print(f">>> {self[...]}\n>>> ({self}).size = {self.size})")
        if (not isinstance(other, opterm)):  return False
        if (len(self) != len(other)):  return False
        if (_matched is None):
            _matched = {}
        else:
            try:  return (_matched[self] == other)
            except KeyError:  pass
        for x, y in zip(self, other):
            matches = match(x, y, _matched=_matched)
            #print(f"\n>>> .match({x=}, {y=})  ==>  {matches}")
            if (not matches):  return False
        return True
    
    def replace(self, old, new):
        if (not isinstance(new, _math_ob)):
            new = opvar(new)
        if (old == self):  return new
        _op = op = self.op
        _args = args = self.args
        if (old == op):
            op = new
        args = tuple(replace(x, old, new) for x in args)
        if (_op==op) and (_args == args):  return self
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(op, *args, domain=self.domain)
    
    def replacements(self, mapping: dict=None, **kwargs):
        if (mapping is None):
            mapping = {}
        if kwargs:
            mapping = (mapping | kwargs)
        return apply_rewrites_replacements(mapping)(self)
    
    def parametrize(self, *args, **kwargs):
        "Replace variables with inputs"
        if args:
            kwargs.update(zip(self.variables, args))
        if kwargs:  return apply_rewrites_replacements(kwargs)(self)
        return self
    
    def evaluate(self, *args, **kwargs):
        return _evaluate(self.parametrize(*args, **kwargs))
    def _evaluate(self):
        op = self.op
        args = tuple(map(_evaluate, self.args))
        try:  return op.func(*args)
        except (TypeError, ArithmeticError):
            #print('❗', op, args)
            return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(op, *args, domain=self.domain)
    
    _functions_ref: dict[tuple, function] = {}
    f: function = hashproperty(_functions_ref, False, False, doc="expression as callable")
    def as_function(self):
        try:  return self.f
        except KeyError:  pass
        except AttributeError:  return self
        variables = self.variables
        argstr = ", ".join(map(str, variables))
        execstr = str(self)
        fstr = f"lambda {argstr}: ({execstr})"
        f = exec(fstr)
        self._functions_ref[self] = f
        return f
    
    

nested_iterable.register(opterm)



"⠀⠀╶╼━┳━━━━━╾╶╼━┳━╾╴⠀⠀"
"⠀╶╼┳━┛┏━━╾╴╶╼━┓┗━┳╾╴⠀"
"⠀⠀⠀┃           OPVAR            ┃⠀⠀⠀"
"⠀╶╼┻━┓┗━╾╴╶╼━━┛┏━┻╾╴⠀"
"⠀⠀╶╼━┻━╾╴╶╼━━━━┻━╾╴⠀⠀"

@modulefunc
class opvar(_core_symbolic, _ꜱᴛʀ):
    "    Basic symbolic operand class in the form of a symbol (str) with an associated value (any object) and domain (DomainType).  By default, the value is set to Unknown, marking the operand as a variable or parameter, but it can be any object.  A constant can created from a value, like opvar(3.14), and the symbol will derive from str(value).  Named constants can be created by using the constructorʼs keyword-arguments, like opvar('π', value=3.14, domain=ⲈRɴ), and any opvar can be cast into a different domain using subscript ([]), as in:"'''
        >>> x = opvar("x", domain=Integral)
        >>> x, x.domain
        x, ⲈZɴ
        >>> x = x[Complex]
        >>> x, x.domain
        x[ⲈCɴ], ⲈCɴ
        >>> x = x[Integral]
    Opvars can be used to form opterm expressions by applying an operator or common function:
        >>> x, type(x).__name__
        (x, 'opvar')
        >>> x = x - 3
        >>> x, type(x).__name__
        (x - 3, 'opterm')
        
    '''
    
    __slots__ = ("_value", "_domain")
    _value: object
    _domain: DomainType
    
    value: object = property(attrgetter("_value"))
    domain: DomainType = property(attrgetter("_domain"))
    referent: object = property(lambda x: get_referent(x, allow_unfinites=-1), 
                doc="Bottommost referent value, or its symbolic if unfinite and not self.")
    referent_value: object = property(lambda x: get_referent(x, allow_unfinites=True), 
                doc="Bottommost referent value.")
    
    depth: int = 0
    indices: list[tuple[int]] = ()
    items: list = ()
    size: int = 1
    
    op: str = None
    
    x: _math_ob = property(_idfunc, "symbolic operand or named constant")
    
    operands: tuple[ⲈOʙ] = property(lambda x: (x,))
    variables: tuple[_core_symbolic] = property(lambda x: list((x,) if (x.value is Unknown) else ()))
    constants: tuple[ⲈOʙ] = property(lambda x: (x,) if (x.value is not Unknown) else ())
    operators: tuple[Ⲉƒx] = property(lambda x: (x,) if (x.value in Ⲉƒx) else ())
    
    _instances: dict = {}
    def __new__(cls, symbol: str, value: object=Unknown, domain: DomainType=Auto):
        key = (symbol, domain)
        try:  return cls._instances[key]
        except KeyError:  pass
        
        S = type(symbol)
        if (S is not str):
            if (value is Unknown):
                if (S is cls) and (domain is Auto):  return symbol
                value = symbol
            symbol = get_name(symbol)
        if (domain is None) or (domain is Auto):
            domain = Object
            if (value is not Unknown):
                domain = get_domain(value)
        elif not isinstance(domain, DomainType):
            domain = deduce_domain(domain)
        
        ǀk0ǀ = cls._get_base_key(value, symbol)
        key = (ǀk0ǀ, domain)
        try:  return cls._instances[key]
        except KeyError:  pass
        try:
            existing = cls._instances[ǀk0ǀ]
        except KeyError:
            existing = None
        else:
            if (domain is Auto):  return existing
            value = existing.value
        
        self = str.__new__(cls, symbol)
        self._value = value
        self._domain = domain
        
        cls._instances[key] = self
        if (existing is None):
            cls._instances[ǀk0ǀ] = self
        return self
    
    "    ⲈǂⲶⲶǂⲶⲶǂⲶⲶǂⲶⲶǂ(    vvv    messy; should refactor    vvv   )ǂⲶⲶǂⲶⲶǂⲶⲶǂⲶⲶǂⰅ    "
    def ǀget_reftypeǀ():
        ǁꜱᴘᴇᴄɪᴀʟᴄᴀꜱᴇꜱǁ = (False, True)
        ǁꜱᴘᴇᴄɪᴀʟᴄᴀꜱᴇꜱǁ = dict(zip(ǁꜱᴘᴇᴄɪᴀʟᴄᴀꜱᴇꜱǁ, ǁꜱᴘᴇᴄɪᴀʟᴄᴀꜱᴇꜱǁ))
        def ǁǂ_ɢᴇᴛᴋᴇʏǂǁ(key):
            try:  return (ǁꜱᴘᴇᴄɪᴀʟᴄᴀꜱᴇꜱǁ[key] is key, key)
            except KeyError:  return key
        class ǀʀᴇꜰǀ(dict):
            def __getitem__(self, key):  return dict.__getitem__(self, ǁǂ_ɢᴇᴛᴋᴇʏǂǁ(key))
            def __setitem__(self, key, value):  return dict.__setitem__(self, ǁǂ_ɢᴇᴛᴋᴇʏǂǁ(key), value)
        return ǀʀᴇꜰǀ
    _ǀk0ǀ_ref: dict[object, str] = ǀget_reftypeǀ()()
    del ǀget_reftypeǀ
    @classmethod
    def _get_base_key(cls, value: object, symbol: str=None):
        subkey = (symbol if ((cls is opfunc) or isunfinite(value) \
                                                                           or isinstance(value, str)) else value)
        try:  return cls._ǀk0ǀ_ref[subkey]
        except KeyError:  return get_name(subkey)
    @classmethod
    def _set_base_key(cls, instance: _core_symbolic, newkey: str):
        value = instance.value
        subkey = (str(instance) if ((cls is opfunc) or isunfinite(value) \
                                                                           or isinstance(value, str)) else value)
        cls._ǀk0ǀ_ref[subkey] = newkey
    def set_base_key(self, base: _core_symbolic):
        "Assigns self.ǀk0ǀ := base.ǀk0ǀ, and ._instances[(ǀk0ǀ, self.domain)] := self.  This makes it so that self[<domspec>] returns the same instance as base[<domspec>] for any&all domain specifiers."
        cls = type(self)
        try:
            ǀk0ǀ = base.ǀk0ǀ
        except AttributeError:
            ǀk0ǀ = cls._get_base_key(base)
        try:
            existing = cls._instances[ǀk0ǀ]
        except KeyError:
            existing = cls._instances[ǀk0ǀ] = self
        cls._instances[(ǀk0ǀ, self.domain)] = self
        cls._set_base_key(self, ǀk0ǀ)
    def get_base_key(self):
        "The first instance of an unknown symbol or known value is cached twice:  once with the standard cache key (<str varname or value>, <domain>), then saved again without the domain.  This allows successive instances or versions created under different domains/specifications to reference the original, keeping naming schemas consistent, concrete fallbacks for cmp&matching, etc.."
        return self._get_base_key(self.value, str(self))
    ǀk0ǀ = property(get_base_key)
    "    ⲈǂⲶⲶǂⲶⲶǂⲶⲶǂⲶⲶǂ(    ^^^    messy; should refactor    ^^^    )ǂⲶⲶǂⲶⲶǂⲶⲶǂⲶⲶǂⰅ    "
    
    def _reprcheck(self):
        var0 = self._instances[self.ǀk0ǀ]
        return False if ((var0 is self) or (var0.domain is Oblivion)) else self.domain
    def __repr__(self):
        var0 = self._instances[self.ǀk0ǀ]
        if (var0 is self) or (var0.domain is Oblivion):  return str(self)
        return f"{var0}[{self.domain}]"
    __str__ = str.__str__
    __hash__ = str.__hash__
    
    def __iter__(self):  yield str(self)
    def __len__(self):  return 1
    
    def __contains__(self, other):  return (self == other)
    
    def __bool__(self):
        try:  return bool(self.value)
        except TypeError:  return True
    
    def __getitem__(self, key):
        if isinstance(key, DomainType):
            current = self.domain
            if (key is current) or (current == key):  return self
            new = type(self)(f'{self}', value=self.value, domain=key)
            #print(f">>> {self!r}[{key}] ==> {new!r}")
            return new
        return self._getitem_(key)
    
    def __call__(self, *args):
        if (self in op_data_ref):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(self, *args)
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("()", self, *args)
    
    def __eq__(self, other):
        v0 = self.value
        if (v0 is not Unknown) and (v0 == get_value(other)):  return True
        if isinstance(other, str):  return str.__eq__(self, other)
        if isinstance(other, tuple):
            if (len(other) == 2) and (other[0] == ""):  return (self == other[1])
            return False
        return (self.value == get_value(other)) or (str(self) == str(other))
    def __ne__(self, other):  return (not self.__eq__(other))
    
    __lt__ = _core_symbolic.__lt__
    __gt__ = _core_symbolic.__gt__
    __le__ = _core_symbolic.__le__
    __ge__ = _core_symbolic.__ge__
    
    def match(self, other, *, _matched: dict=None):
        if (_matched is None):
            _matched = {}
        else:
            try:  return (_matched[self] == other)
            except KeyError:  pass
        v0 = self.referent_value
        v1 = get_referent(other, 1)
        d0 = self.domain
        d1 = get_domain(other)
        if (d0 is Auto):
            d0 = d1
        elif (d1 is Auto):
            d1 = d0
        matches = None
        if (v0 is Unknown):
            #if (d0 is not Object):
            #    print(f"    {self=};    {other=};\n    {v0=};    {v1=};")
            #    print(f"{d0=};    {d1=};    {d0>=d1 = }")
            matches = ((d0 >= d1) or ((not isunfinite(v1)) and (v1 in d0))) \
                       and ((not (d1 <= Ⲉƒx)) or (d0 <= Ⲉƒx))
        else:
            matches = (v0 is v1) or (v0 ==  v1)
        if (matches is True):
            _matched[self] = other
        return matches
    
    def replace(self, old, new):
        if (not isinstance(new, _math_ob)):
            new = opvar(new)
        if (self == old):  return new
        return self
    
    def replacements(self, mapping: dict=None, **kwargs):
        if (mapping is None):
            mapping = {}
        if kwargs:
            mapping = (mapping | kwargs)
        try:  return mapping[self]
        except KeyError:  return self
    
    def parametrize(self, *args, **kwargs):
        val = self.value
        if (val is Unknown):
            if args:  return args[0]
            if kwargs:
                try:  return kwargs[self]
                except KeyError:  pass
            return self
        else:  return val
    
    def evaluate(self, *args, **kwargs):
        return _evaluate(self.parametrize(*args, **kwargs))
    def _evaluate(self):
        val = self.value
        return self if (val is Unknown) else val
        




"⠀⠀╶╼━┳━━━━━╾╶╼━┳━╾╴⠀⠀"
"⠀╶╼┳━┛┏━━╾╴╶╼━┓┗━┳╾╴⠀"
"⠀⠀⠀┃          OPFUNC           ┃⠀⠀⠀"
"⠀╶╼┻━┓┗━╾╴╶╼━━┛┏━┻╾╴⠀"
"⠀⠀╶╼━┻━╾╴╶╼━━━━┻━╾╴⠀⠀"

@modulefunc
class opfunc(opvar):
    __slots__ = ()
    
    op_data: opdata = hashproperty(op_data_ref, setter=False, deleter=False)
    
    opdomains: tuple[tuple, DomainType] = property(attrgetter("_domain.__args__"))
    codomain: DomainType = property(lambda self: self.opdomains[-1])
    argdomains: DomainType = property(lambda self: self.opdomains[0])
    
    op: str = property(_idfunc)
    nin: int = property(attrgetter("op_data.nin"))
    precidence: int = property(attrgetter("op_data.precidence"))
    format: Ⲉƒx = property(attrgetter("op_data.format"))
    func: Ⲉƒx = property(attrgetter("op_data.func"))
    
    _instances: dict = {}
    def __new__(cls, symbol: str, codomain: DomainType=Auto, argdomains: tuple[DomainType]=None, 
    *, value: object=Unknown, overwrite_opdata: bool=True):
        T = type(symbol)
        if (codomain is Auto) and (argdomains is None) and (value is Unknown):
            if (T is cls):  return symbol
            try:  return cls._instances[symbol]
            except KeyError:  pass
        
        symbol = str(symbol)
        
        try:
            op_data = op_data_ref[symbol]
        except KeyError:
            nin = None if ((argdomains is None) or (... in argdomains)) else len(argdomains)
            if (nin is None):
                fmt = (lambda *xyz: f"{symbol}{xyz}") if symbol.isidentifier() else \
                          (lambda *xyz: symbol.join(map(str, xyz)))
            else:
                fmt = f"{symbol}{{0}}" if (nin==1) else symbol.join(map(str, ({i} for i in range(nin))))
            op_data = op_data_ref[symbol] = opdata(symbol, nin, 18, fmt, func=Undefined, _cache=False)
            func = None
        else:
            nin = op_data.nin
            func = op_data.func
        
        if (value is Unknown) and (func is not None):
            value = func
        
        codomain, argdomains = cls._fix_opdomains(nin, codomain, argdomains)
        domain = _ⲈƒxGenericAlias(Ⲉƒx, (list(argdomains), codomain))
        
        self = opvar.__new__(cls, symbol, value=value, domain=domain)
        
        if overwrite_opdata:
            op_data = op_data_ref[symbol] = opdata(self, *op_data[1:], formatter=op_data.format, _cache=False)
            if (func is None):
                op_data.func = self.__call__
        
        cls._instances[symbol] = self
        return self
    @classmethod
    def _from_raw(cls, symbol: str, /, nin: int=None, precidence: int=0, formatter: (Ⲉƒx | str)=None, codomain: DomainType=Auto, argdomains: tuple[DomainType]=None, func: Ⲉƒx=Undefined, *, value: object=None, overwrite_opdata: bool=True):
        op_data = opdata(symbol, nin, precidence, formatter, func=func)
        self = cls(symbol, codomain, argdomains, value=value, overwrite_opdata=overwrite_opdata)
        return self
    
    @classmethod
    def _fix_opdomains(cls, nin: int, codomain: DomainType=Auto, argdomains: tuple[DomainType]=None):
        if (argdomains is not None) and (len(argdomains) == 1) and (type(argdomains[0]) is (list)):
            argdomains = argdomains[0]
        #print(f">>> {nin, (codomain, argdomains) = }")
        if isinstance(argdomains, DomainType):
            argdomains = (argdomains, ...) if (nin is None) else ((argdomains,) * nin)
        if (codomain is not Auto):
            codomain = deduce_domain(codomain)
        if (argdomains is None):
            if (codomain is Auto):
                domain = Object
            else:
                domain = codomain
                codomain = Auto
            argdomains = (domain, ...) if (nin is None) else ((domain,) * nin)
        else:
            #print(f">>>     {nin, (codomain, argdomains) = }")
            argdomains = tuple(argdomains)
            if (nin is None):
                if (argdomains[0] in (..., Auto)):
                    argdomains = (Object,) + argdomains[1:]
                if (argdomains[-1] is not ...):
                    argdomains = argdomains + (...,)
                argdomains = tuple(deduce_domain(d, Auto, ...) for d in argdomains)
            elif (len(argdomains) != nin):
                #print(f">>>     {nin, (codomain, argdomains) = }")
                raise ValueError(f"(len(argdomains) != nin):  ({len(argdomains)} != {nin})")
            else:
                argdomains = (deduce_domain(argdomains[0]),) \
                                         + tuple(deduce_domain(d, Auto) for d in argdomains[1:])
        
        #print(f">>>         {nin, (codomain, argdomains) = }")
        return codomain, argdomains
    
    def get_string(self, *args, strf: Ⲉƒx=get_name, outer_op: opdata=None):
        "(((Redefined & replaced down below.)))"
        raise NotImplementedError
    
    def __repr__(self):
        string = str(self)
        if (self._instances[string] is self):  return string
        return f"{string}[{self.argdomains}, {self.codomain}]"
    __str__ = str.__str__
    __hash__ = str.__hash__
    __eq__ = str.__eq__
    
    def __iter__(self):  yield str(self)
    def __len__(self):  return 1
    
    def __contains__(self, other):  return (self == other)
    
    def __bool__(self):
        try:  return bool(self.value)
        except TypeError:  return True
    
    def __getitem__(self, key):
        if (type(key) is list) or (key in (None, ..., NotImplemented)):
            return opterm.__getitem__(self, key)
        if isinstance(key, dict):  return self.replacements(key)
        domain = None
        if isinstance(key, ABCDMeta):
            codomain, argdomains = opdata._fix_opdomains(self.nin, key, self.argdomains)
            domain = Ⲉƒx[list(argdomains), codomain]
        elif (type(key) is tuple) and (len(key) == 2) \
        and (type(key[0]) is list) and isinstance(key[1], ABCDMeta):
            codomain, argdomains = opdata._fix_opdomains(self.nin, key[-1], key[:-1])
            domain = Ⲉƒx[list(argdomains), codomain]
        if (domain is not None):
            #print(f">>> {(codomain, argdomains) = }")
            return opvar.__new__(type(self), self, value=self, domain=domain)
        return self._getitem_(key)
    
    def __call__(self, *args):
        if (str(self) in op_data_ref):  return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(self, *args)
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("()", self, *args)
    
    def match(self, other, *, _matched: dict=None):
        if (_matched is None):
            _matched = {}
        else:
            try:  return (_matched[self] == other)
            except KeyError:  pass
        v0 = self.value
        v1 = get_value(other)
        d0 = self.domain
        d1 = get_domain(other)
        matches = None
        matches = (type(other) is opfunc)
        if matches and (v0 is Unknown):
            if matches := (self.nin == other.nin):
                og0 = d0.__origin__
                og1 = d1.__origin__
                ag0 = d0.__args__
                ag1 = d1.__args__
                opdoms_match = (og0 >= og1) \
                        and all((p is ...) or (... is q) or (p >= q) for p,q in zip(ag0, ag1))
                matches = (opdoms_match) #and (v0 is Unknown) or (str(self) == str(other))
                
            #(v0 == str(self)) or print(f"\n>>> .match({self=}, {other=})\n>>>     {(d0,d1) = }\n>>>     {opdoms_match = }\n>>>     {matches = }\n")
        elif matches:
            matches = (self == other)
        else:
            matches = (v0 ==  v1)
        #(v0 == str(self)) or print(f"\n>>> .match({self=}, {other=})\n>>>     {(d0,d1) = }\n>>>     {(v0,v1) = }\n>>>     {matches = }\n")
        
        if (matches is True):
            _matched[self] = other
        return matches


@modulefunc
def _ꓽƒ(func: function):
    fname = get_name(func)
    try:  return opfunc._instances[fname]
    except KeyError:  pass
    return opfunc(fname, value=func)



#    ᐨꞋ = property(_mulinv_)
#    ꤶ = _root_
#    ꓹ = _startuple_

_op_data_ref = ({k: opdata(v, *v.op_data[1:]) for k,v in \
({
    ".": opfunc(".", ⲈOʙ, (ⲈOʙ, ⲈCʜ)),
    "[]": opfunc("[]", ⲈOʙ, (ⲈCᴛ, ⲈOʙ)),
    "()": opfunc("()", ⲈOʙ, (ⲈFᴄ, ⲈOʙ, ...)),
    
    ", ": opfunc(", ", ⲈSવ, (ⲈOʙ, ...)),
    "": opfunc("", ⲈOʙ, (ⲈOʙ,)),
    " ~": opfunc(" ~", Auto, (ⲈLᴛ,)),
    " +": opfunc(" +", Auto, (ⲈUɴ,)),
    " -": opfunc(" -", Auto, (ⲈUɴ,)),
    " **-1": opfunc(" **-1", Auto, (ⲈUɴ,)),
    
    "bool": opfunc("bool", Ⲉǃǃ, (ⲈOʙ,)), 
    "len": opfunc("len", ⲈNɴ, (ⲈCᴛ,)), 
    "iter": opfunc("iter", Iterator, (ⲈIᴛ,)), 
    "abs": opfunc("abs", ⲈRɴ, (ⲈUɴ,)), 
    "floor": opfunc("floor", Auto, (ⲈUɴ,)), 
    "ceil": opfunc("ceil", Auto, (ⲈUɴ,)), 
    "trunc": opfunc("trunc", Auto, (ⲈUɴ,)), 
    "round": opfunc("round", Auto, (ⲈUɴ, ⲈZɴ)), 
    "divmod": opfunc("divmod", ⲈSવ[ⲈUɴ, ⲈUɴ], (ⲈUɴ, ⲈUɴ)), 
    
    "|": opfunc("|", Auto, (ⲈLᴛ, ⲈLᴛ)),
    "&": opfunc("&", Auto, (ⲈLᴛ, ⲈLᴛ)),
    "^": opfunc("^", Auto, (ⲈLᴛ, ⲈLᴛ)),
    "+": opfunc("+", Auto, (ⲈUɴ|ⲈSવ, ⲈUɴ|ⲈSવ)),
    "-": opfunc("-", Auto, (ⲈUɴ|ⲈLᴛ, ⲈUɴ|ⲈLᴛ)),
    "*": opfunc("*", Auto, (ⲈUɴ|ⲈCᴛ, ⲈUɴ|ⲈCᴛ)),
    "/": opfunc("/", Auto, (ⲈUɴ, ⲈUɴ)),
    "**": opfunc("**", Auto, (ⲈUɴ, ⲈUɴ)),
    "//": opfunc("//", Auto, (ⲈUɴ, ⲈUɴ)),
    "%": opfunc("%", Auto, (ⲈUɴ, ⲈUɴ)),
    "<<": opfunc("<<", Auto, (ⲈOʙ, ⲈOʙ)),
    ">>": opfunc(">>", Auto, (ⲈOʙ, ⲈOʙ)),
    "@": opfunc("@", Auto, (ⲈOʙ, ⲈOʙ)),
    "==": opfunc("==", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    "!=": opfunc("!=", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    "<": opfunc("<", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    ">": opfunc(">", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    "<=": opfunc("<=", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    ">=": opfunc(">=", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    
    " in ": opfunc(" in ", ⲈBʟ, (ⲈCᴛ, ⲈOʙ)),
    " not in ": opfunc(" not in ", ⲈBʟ, (ⲈCᴛ, ⲈOʙ)),
    " is ": opfunc(" is ", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    " is not ": opfunc(" is not ", ⲈBʟ, (ⲈOʙ, ⲈOʙ)),
    "not ": opfunc("not ", ⲈBʟ, (ⲈOʙ,)),
    " or ": opfunc(" or ", ⲈBʟ|ⲈOʙ, (ⲈOʙ, ⲈOʙ)),
    " and ": opfunc(" and ", ⲈBʟ|ⲈOʙ, (ⲈOʙ, ⲈOʙ)),
    " if else ": opfunc(" if else ", Auto, (ⲈOʙ, Auto, ⲈBʟ)),
    
    ":=": opfunc(":=", Auto, (ⲈOʙ, ⲈOʙ)),
    ".=": opfunc(".=", Auto, (ⲈOʙ, ⲈCʜ, ⲈOʙ)),
    "[]=": opfunc("[]=", Auto, (ⲈCᴛ, ⲈOʙ, ⲈOʙ)),
    "|=": opfunc("|=", Auto, (ⲈOʙ, ⲈOʙ)),
    
    "&=": opfunc("&=", Auto, (ⲈOʙ, ⲈOʙ)),
    "^=": opfunc("^=", Auto, (ⲈOʙ, ⲈOʙ)),
    "+=": opfunc("+=", Auto, (ⲈOʙ, ⲈOʙ)),
    "-=": opfunc("-=", Auto, (ⲈOʙ, ⲈOʙ)),
    "*=": opfunc("*=", Auto, (ⲈOʙ, ⲈOʙ)),
    "/=": opfunc("/=", Auto, (ⲈOʙ, ⲈOʙ)),
    "**=": opfunc("**=", Auto, (ⲈOʙ, ⲈOʙ)),
    "//=": opfunc("//=", Auto, (ⲈOʙ, ⲈOʙ)),
    "%=": opfunc("%=", Auto, (ⲈOʙ, ⲈOʙ)),
    "<<=": opfunc("<<=", Auto, (ⲈOʙ, ⲈOʙ)),
    ">>=": opfunc(">>=", Auto, (ⲈOʙ, ⲈOʙ)),
    "@=": opfunc("@=", Auto, (ⲈOʙ, ⲈOʙ)),
    
    
    
    "ͱ|": opfunc("ͱ|", Auto, (ⲈOʙ,)), 
    "ⲳ|": opfunc("ⲳ|", Auto, (ⲈOʙ,)), 
    
    "|ꕺ|": opfunc("|ꕺ|", Auto, (ⲈOʙ, ⲈOʙ)), 
    "|ꔷ|": opfunc("|ꔷ|", Auto, (ⲈOʙ, ⲈOʙ)), 
    
}).items()})
op_data_ref.clear()
op_data_ref.update(_op_data_ref)
del _op_data_ref

opdata_canonical.ꓽͱǀ_.func = opfunc("ͱ|")
opdata_canonical.ꓽⲳǀ_.func = opfunc("ⲳ|")
opdata_canonical.ǀꕺǀ_.func = opfunc("|ꕺ|")
opdata_canonical.ǀꔷǀ_.func = opfunc("|ꔷ|")

#assert opdata_canonical.imod_ is op_data_ref["%="]


_ops_precedences = {
    0: ("",),     1: ("(, )", "[, ]", "{:,}", "{,}", ),     2: ("[]", "()", ".",),     3: ("await ",), 
    4: ("**", " **-1"),     5: (" +", " -", " ~", ),     6: ("*", "@", "/", "//", "%",),     7: ("+", "-", ), 
    8: ("<<", ">>",),     9: ("&", ),     10: ("^", ),     11: ("|", ), 
    12: ("<", "<=", ">", ">=", "!=", "==", " in ", "not in", " is ", "is not",), 
    13: ("not ",),     14: (" and ",),     15: (" or ",),     16: (" if else ",), 
    17: ("lambda : ",),     18: (", ",),     19: ("yield ", ), 
    20: ("=", ":=", "[]=", ".=", "**=", "*=", "@=", "/=", "//=", "%=", "+=", "-=", "<<=", ">>=", "&=", "^=", "|="), 
}
ops_precidences = {}
_k = _w = _v = None
for _k, _v in _ops_precedences.items():
    for _w in _v:
        ops_precidences[_w] = _k
del _k, _v, _w


opfref = {str(op): opfunc(op) for op,data in op_data_ref.items()}

for methodname in ("_getattr_", "_getitem_", "_call_", 
"__invert__", "__pos__", "__neg__", "_mulinv_", 
"__or__", "__and__", "__xor__", "__lshift__", "__rshift__", "__matmul__", 
"__add__", "__sub__", "__mul__", "__truediv__", "__pow__", "__floordiv__", "__mod__", "__divmod__", 
"_eq_", "_ne_", "__lt__", "__gt__", "__le__", "__ge__", "_contains_", ):
    func: function = getattr(_core_symbolic, methodname)
    fco = func.__code__   
    func.__code__ = fco.replace(co_consts=tuple((opfref.get(k,k) for k in fco.co_consts)))



"⠀⠀╶╼━┳━━━━━━━╾╶╼━━┳━╾╴⠀⠀"
"⠀╶╼┳━┛┏━━━━╾╴╶╼━━┓┗━┳╾╴⠀"
"⠀⠀⠀┃          OPRELATION          ┃⠀⠀⠀"
"⠀╶╼┻━┓┗━━╾╴╶╼━━━━┛┏━┻╾╴⠀"
"⠀⠀╶╼━┻━━╾╴╶╼━━━━━━┻━╾╴⠀⠀"

@modulefunc
class oprelation(opterm):
    
    op_eval_priority: int = 1
    
    left: opterm = _tuplegetter(1, "left side")
    right: opterm = _tuplegetter(2, "right side")
    
    _instances: dict = {}
    def __new__(cls, op: opfunc, left: opterm, right: opterm|opvar, *, value: bool=Unknown):
        if (not isinstance(op, _core_symbolic)):
            op = opfunc(str(op))
        if not (op.codomain <= Ⲉǃǃ):
            raise ValueError("oprelation requires (op.codomain <= Ⲉǃǃ);\n    ({op=};    {op.codomain=})")
        
        key = op, left, right
        try:  return cls._instances[key]
        except KeyError:  pass
        
        self = opterm.__new__(cls, op, left, right, value=value, domain=Ⲉǃǃ)
        
        cls._instances[key] = self
        return self
    
    _rewriters_ref: dict[tuple, function] = {}
    _rewriters: dict[function] = hashproperty(_rewriters_ref, setter=True, deleter=True)
    def get_rewriter(self, transformfunc: function=None):
        key = transformfunc
        try:  return self._rewriters[key]
        except KeyError:  pass
        if (transformfunc is None):
            op = self.op
            cmp = method(memmethod, op.func)
            transformfunc = memmethod(_cmp_transform, cmp)
        rewriter = _rewriter(transformfunc, self.left, self.right)
        self._rewriters_ref.setdefault(self, {})[key] = rewriter
        return rewriter
    
    _reverse_ops_ref: dict[str, str] = {"==": '==', "!=": '!=', ">=": "<=", "<=": ">=", ">": "<", "<": ">"}
    def commutate(self):
        op = self.op
        try:
            rop = self._reverse_ops_ref[op]
        except KeyError:  raise ValueError('unrecognized relop: %r' % op)
        else:  return self[[0, 2, 1]] if (rop is ...) else oprelation(rop, self.right, self.left)
    
    def _NOT_(self, *, domain: type=...):
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ("not ", self, domain=Ⲉǃǃ)
    
    def _OR_(self, other, *, domain: type=...):
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" or ", self, other, domain=(Ⲉǃǃ|Auto[:2]))
    def _AND_(self, other, *, domain: type=...):
        return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ(" and ", self, other, domain=(Ⲉǃǃ|Auto[:2]))
    
    __invert__ = _NOT_
    
    __or__ = _OR_
    __and__ = _AND_




"⠀⠀⠀╶╼━━━╾╴╶╼━╾╴⠀⠀⠀"
"⠀╶╼━━━╾╴╶╼━━━━━╾╴⠀"
"⠀        Method Helpers    ⠀⠀"
"⠀╶╼━━━━━╾╴╶╼━━━╾╴⠀"
"⠀⠀⠀╶╼━╾╴╶╼━━━╾╴⠀⠀⠀"

@modulefunc
def replace(ob, old, new):
    try:  return ob.replace(old, new)
    except (AttributeError, TypeError):  pass
    if (old == ob):  return new
    return ob


@modulefunc
def match(p, q, *, _matched: dict=None):
    if (_matched is None):
        _matched = {}
    try:  return p.match(q, _matched=_matched)
    except AttributeError:  return _match(p, q, _matched)
def _match(p, q, _matched: dict):
    if (p == q): #or ((p!=p) and (q!=q)):
        try:  return (_matched[p] == q)
        except KeyError:
            _matched[p] = q
            return True
    return False


@modulefunc
def evaluate(ob, *args, **kwargs):
    try:  return ob.evaluate(*args, **kwargs)
    except AttributeError:  return _evaluate(ob)
def _evaluate(ob):
    try:  return ob._evaluate()
    except AttributeError:  pass
    try:
        val = ob.value
    except AttributeError:  return ob
    else:  return (ob if isunfinite(val) else _evaluate(val))



"⠀╶╼━━━━━━╾╴╶╼━━╾╴⠀"
"⠀     Expression Strings   ⠀⠀"
"⠀╶╼━━╾╴╶╼━━━━━━╾╴⠀"

def get_string(op: opfunc, *args, strf: Ⲉƒx=get_name, outer_op: opdata=None):
    if str.isidentifier(op):
        return f"{op}({', '.join(map(strf, args))})"
    op_data = op.op_data
    prec = op_data.precidence
    string = op_data.format(*[f"({strf(x)})" if (prec <= get_op_precidence(x) > 3) else strf(x) for x in args])
    if (outer_op is not None) and (outer_op is not False):
        if (outer_op is True) or (get_op_precidence(outer_op) <= prec):  return string.join('()')
    return string

opfunc.get_string = get_string
del get_string

@lru_cacheᐩᐩ
def _get_string_get_parenthesizer(outer_op: opdata=None, strf: Ⲉƒx=get_name_or_str):
    if (outer_op is None) or (outer_op is False):  return strf
    elif (outer_op is True):  return (lambda x: f"({strf(x)})")
    prec_check = _get_string_get_prec_check(outer_op)
    def parenthesizer(x):
        x_opd = get_op_data_ob(x)
        if prec_check(x_opd) or (x_opd.op.value is Unknown):  return f"({strf(x)})"
        return strf(x)
    return parenthesizer
@lru_cacheᐩᐩ
def _get_string_get_prec_check(outer_op: opdata=None):
    if (outer_op is None) or (outer_op is False):  return (const_False)
    elif (outer_op is True):  return (const_True)
    prec = outer_op.precidence
    if (prec == 18) or (prec == 12):  return (lambda x: (3 < get_op_precidence(x)))
    '↑↑↑    (", ", ) || ("<", "<=", ">", ">=", "!=", "==", " in ", "not in", " is ", "is not",)'
    if (prec in (13, 14, 15, 16)):  return (lambda x: (2 == get_op_nin(x)))
    "↑↑↑    ('not ', ' or ʻ, ' and ', ' if else ')"
    if (prec == 4):  return (lambda x: (prec <= get_op_precidence(x)))
    '↑↑↑    ("**", )'
    return (lambda x: (prec < get_op_precidence(x)))


"⠀╶╼━━━╾╴╶╼━━━━━━━╾╴╶╼━╾╴⠀"
"⠀     Assign 'ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ' Globalvar  ⠀⠀"
@modulefunc
def assign_globalǁʽᴏᴘᴊᴏɪɴˮǀ(cls: type):
    global ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ
    if 1 or issubclass(cls, _core_symbolic):
        ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ = cls
    else:  raise TypeError("expected a subclass of _core_symbolic")
    return ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ

ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ = assign_globalǁʽᴏᴘᴊᴏɪɴˮǀ(opterm)
modulefunc("ꓸꓽᴏᴘᴊᴏɪɴꓽꓸ")




#        ★        #        ★        #        ★        #        ★        #        ★        #
"⠀⠀╻┏━┛╶╼━━━━━━━┓┃┣━━━━━╾╴╶╼━━┓╻⠀⠀"
"⠀┃┃┃⠀              DEFINE & COMPILE              ⠀┃┃┃⠀"
"⠀┃┃┃      MODULAR  COMPONENT  FUNCS    ┃┃┃⠀"
"⠀┃┃┃⠀          for  MATCH-&-REWRITE          ⠀┃┃┃⠀"
"⠀┃┃┃⠀⠀               ARCHITECTURE                 ⠀┃┃┃⠀"
"⠀⠀╹┗━━╾╴╶╼━━━━━┫┃┗━━━━━━━╾╴┏━┛╹⠀⠀"
#        ★        #        ★        #        ★        #        ★        #        ★        #


@modulefunc
@lru_cacheᐩᐩ
def _cmp_transform(cmp_method: Ⲉƒx[[object], PredicateTypage], pattern: opterm, rewrite: opterm, expression: opterm):
    "Returns a new expression with all subterms matching ‘pattern’ (according to ʻcmp_methodʼ(pattern)(subterm)) transformed to match ‘rewriteʼ."'''
        >>> pattern = (a/b)
        >>> rewrite = (a*b**-1)
        >>> expression = (a/b - 3/c)
        >>> _cmp_transform(attrgetter("match"), pattern, rewrite, expression)
        (a*b**-1) - (3*c**-1)
        >>> _cmp_transform(method(memmethod, operator.__eq__), pattern, rewrite, expression)
        (a*b**-1) - (3/c)
    ____________________
    Predefined globals:
    |    cmp_matchtransform := memmethod(_cmp_transform, attrgetter("match"))
    |    cmp_eqtransform := memmethod(_cmp_transform, method(memmethod, operator.__eq__))
    ____________________
    '''
    patt2rerite_indices = DefaultObject
    if (not isinstance(pattern, opterm)):
        pattern = ꓽtupleꓸ__new__ǁoptermǁ((ʻʻˮ, pattern,))
    pattern_cmp = cmp_method(pattern)
    expr = expression
    try:
        match_indexes = list(expr._indexes(pattern_cmp))#, maxdepth=(pattern.depth + 1)))
    except AttributeError:
        if (not pattern_cmp(expr)):  return expr
        match_indexes = [None]
    if match_indexes:
        if (patt2rerite_indices is DefaultObject):
            rewrite, patt2rerite_indices = _cmp_get_rewrite_indices(pattern, rewrite)
        for item in expr[match_indexes]:
            source = ꓽtupleꓸ__new__ǁoptermǁ((ʻʻᐩˮ, item, rewrite))
            repl = source[patt2rerite_indices]
            expr = expr.replace(item, repl)
    return expr


#@modulefunc
#def _transform_indextransform(rewrite_indices: list, rewrite: opterm, match_indexes: list, expr: opterm):
#    """
#    [assumes match_indexes refer to expr before replacement;
#    each index is resolved against the original corresponding
#    matched subterm.]
#    """
#    for item in expr[match_indexes]:
#        source = ꓽtupleꓸ__new__ǁoptermǁ((ʻʻᐩˮ, item, rewrite))
#        repl = source[rewrite_indices]
#        expr = expr.replace(item, repl)
#    return expr


@modulefunc
def _cmp_get_indexes_where(cmp_method: Ⲉƒx[[object], PredicateTypage], pattern: opterm, expression: opterm):
    '''
    Returns the indices where ʻexpressionʼ contains ʻpatternʼ according to ʻcmp_methodʼ, which should be a comparison-getter of the form ℊ(p):→ƒᴘ, where ƒᴘ(q):→ƒ(p,q), and ƒ is a boolean relation.  When bound to a cmp_method, the function takes on the form Ƒ(pattern, expression):→indices, where (all([cmp_method(expression[idx])(pattern) for idx in indices]) == True).
    ____________________
    Predefined globals:
    |    cmp_get_matchindexes := memmethod(_cmp_get_indexes_where, attrgetter("match"))
    |    cmp_get_eqindexes := memmethod(_cmp_get_indexes_where, method(memmethod, operator.__eq__))
    ____________________
    '''
    if (not isinstance(pattern, opterm)):
        pattern = ꓽtupleꓸ__new__ǁoptermǁ((ʻʻˮ, pattern,))
    pattern_cmp = cmp_method(pattern)
    try:  return list(expression._indexes(pattern_cmp))#, maxdepth=(pattern.depth + 1)))
    except AttributeError:  return [None] if pattern_cmp(expression) else []

ʻʻˮ = op_data_ref[""].op
ʻʻᐩˮ = op_data_ref["+"].op
ʻʻᐩˣˮ = op_data_ref[" +"].op
assert type(ʻʻᐩˮ) is opfunc, type(ʻʻᐩˮ)
ꓽtupleꓸ__new__ǁoptermǁ = memmethod(ꓽtupleꓸ__new__, opterm)
modulefunc("ꓽtupleꓸ__new__ǁoptermǁ")

@lru_cacheᐩᐩ
def _cmp_get_rewrite_indices(pattern: opterm, rewrite: opterm):
    "Retrieves the indices for which ‘rewrite’ can be constructed from the concatenation of ‘pattern’+‘rewrite’.  This will be mapped onto similarly-shaped concatenations of the rewrite with matched subterms in the matched expression."'''
    ____________________
    Predefined globals:
    |    cmp_get_matchindexes := memmethod(_cmp_get_indexes_where, attrgetter("match"))
    |    cmp_get_eqindexes := memmethod(_cmp_get_indexes_where, method(memmethod, operator.__eq__))
    ____________________
    '''
    if nontuple := (not isinstance(rewrite, tuple)):
        rewrite = ꓽtupleꓸ__new__ǁoptermǁ((ʻʻᐩˣˮ, rewrite))
    source = ꓽtupleꓸ__new__ǁoptermǁ((ʻʻᐩˮ, pattern, rewrite))
    patt2rerite_indices = tuplify(rewrite, iterable_types=tuple, \
                            tuplify_as=list, item_wrapper=source.index)
    if nontuple:
        patt2rerite_indices = (patt2rerite_indices, 1)
    return rewrite, patt2rerite_indices




@modulefunc
def _get_cmp_transform(cmp_method: Ⲉƒx[[object], PredicateTypage]):
    '''
    Returns ʻtransformfuncʼ, a method of the function _cmp_transform() bound to ʻcmp_methodʼ, which should be a comparison-getter of the form ℊ(p):→ƒᴘ, where ƒᴘ(q):→ƒ(p,q), and ƒ is a boolean relation.  The predefined transformfuncs below should suffice for most contexts, and can easily be reverse-engineered if needed.  The returned callable will be of the form TƑ(pattern, rewrite, expression), which rewrites expression according to pattern:==>rewrite.  So:
        >>> cmp_matchtransform = _get_cmp_transform(attrgetter("match"))
        >>> pattern = (X/Y)
        >>> rewrite = (X*Y**-1)
        >>> expression = (a/2 - 3/b)
        >>> cmp_matchtransform(pattern, rewrite, expression)
        (a*0.5 - (3*b**-1))
    ____________________
    Predefined globals:
    |    cmp_matchtransform := memmethod(_cmp_transform, attrgetter("match"))
    |    cmp_eqtransform := memmethod(_cmp_transform, method(memmethod, operator.__eq__))
    ____________________
    '''
    return memmethod(_cmp_transform, cmp_method)


cmp_matchtransform = memmethod(_cmp_transform, attrgetter("match"))
cmp_eqtransform = memmethod(_cmp_transform, method(memmethod, operator.__eq__))


cmp_get_matchindexes = memmethod(_cmp_get_indexes_where, \
                                                    attrgetter("match"))
cmp_get_eqindexes = memmethod(_cmp_get_indexes_where, \
                                                    method(memmethod, operator.__eq__))

modulefuncs(["cmp_matchtransform", "cmp_eqtransform", 
                          "cmp_get_matchindexes", "cmp_get_eqindexes", 
                          ])


def _get_rewritersꓸdefault_sortkey(kv):
    k, v = kv
    w = get_referent(v, allow_unfinites=True)
    if (w is Unknown):
        w = v
    return (~get_size(k) - len(get_consts(k)), get_size(v), (not isunfinite(w)))

@modulefunc
def _get_rewriters(transformfunc: Ⲉƒx[[opterm, opterm, opterm], opterm], canon_ref: dict, *, sort_dict_inplace: bool=False):
    '''
    Binds ʻtransformfuncʼ (cmp_matchtransform, cmp_eqtransform, or other method(_cmp_transform, <cmp-func>)) to a dictionary of {ʻpatternʼ: ʻrewriteʼ} pairs.  Returns a tuple of rewriters to be used in the _apply_rewrites() function.
        >>> get_rewriters_matchrewrite = memmethod(_get_rewriters, cmp_matchtransform)
        >>> canonref = {(X/Y): (X*Y**-1),  (X-Y): (X+-Y)}
        >>> rewriters = get_rewriters_matchrewrite(cmp_matchtransform, canonref)
        >>> len(rewriters)
        2
        >>> apply_rewrites = memmethod(_apply_rewrites, rewriters)
        >>> apply_rewrites((a/2 - 3/b))
        (a*0.5 + -(3*b**-1))
    ____________________
    Predefined globals:
    |    get_rewriters_matchrewrite := memmethod(_get_rewriters, cmp_matchtransform)
    |    get_rewriters_replacements := memmethod(_get_rewriters, cmp_eqtransform)
    ____________________
    '''
    if (type(canon_ref) is tuple):
        return canon_ref
    
    key = transformfunc, frozenset(canon_ref.items())
    try:  return _get_rewriters.__dict__[key]
    except KeyError:  pass
    
    items = sorted(canon_ref.items(), key=_get_rewritersꓸdefault_sortkey)
    if sort_dict_inplace:
        canon_ref.clear()
        canon_ref.update(items)
    
    rewriters = tuple(memmethod(memmethod(transformfunc, pattern), rewrite) \
                                                                                for pattern, rewrite in items)
    _get_rewriters.__dict__[key] = rewriters
    return rewriters



@modulefunc
def _apply_rewrites(rewriters: list[method], expression: opterm, *, recursion_limit: int=16, _cache: dict=None):
    "Apply rewriters to an expression object until it remains unchanged, or the recursion_limit is reached.  The full conversion path goes like this:\n"'''
        >>> a, b, c, x, y, z = [opvar(ch) for ch in "abcxyz"]
        >>> canonref = {(x/y): (x*(y**-1)),  (x-y): (x+(-y))}
      [(>>> rewriters = _get_rewriters(cmp_matchtransform, canonref)
        >>> simplify = memmethod(_apply_rewrites, rewriters)    <<<)\
 ] | [(>>> simplify = _get_apply_rewrites(cmp_matchtransform, canonref)    <<<)\
 ] | [(>>> simplify = apply_rewrites_matchrewrite(canonref)    <<<)\
 ]      >>> expr = (a + 3/(b-c))
        >>> simplify(expr)
        a + 3 * (b + -c)**-1
    Use cmp_matchtransform()|apply_rewrites_matchrewrite() for pattern matching, cmp_eqtransform()|apply_rewrites_replacements() for syntactic replacements.
    '''
    expr = expression
    if (_cache is not None):
        trace = _cache.setdefault(expr, [])
        for _ in range(recursion_limit):
            _expr = expr
            for rewrite in rewriters:
                expr_ = rewrite(expr)
                if (expr_ == expr):  continue
                trace.append((expr, (rewrite.__func__, rewrite.__self__), expr_))
                expr = expr_
            if (expr == _expr):  break
        return expr
    for _ in range(recursion_limit):
        _expr = expr
        for rewrite in rewriters:
            expr = rewrite(expr)
        if (expr == _expr):  break
    return expr


@modulefunc
def _get_apply_rewrites(transformfunc: Ⲉƒx[[opterm, opterm, opterm], opterm], canon_ref: dict):
    '''
    Binds ʻtransformfuncʼ (cmp_matchtransform, cmp_eqtransform, or other method(_cmp_transform, <cmp-func>)) to a dictionary of {ʻpatternʼ: ʻrewriteʼ} pairs.  The returned callable can be applied to an expression object for rewrite or replace transformations:
        >>> canonref = {(X/Y): (X*Y**-1),  (X-Y): (X+-Y)}
        >>> apply_rewrites = _get_apply_rewrites(cmp_matchtransform, canonref)
        >>> apply_rewrites((a/2 - 3/b))
        (a*0.5 + -(3*b**-1))
    ____________________
    Predefined globals:
    |    apply_rewrites_matchrewrite := memmethod(_get_apply_rewrites, cmp_matchtransform)
    |    apply_rewrites_replacements := memmethod(_get_apply_rewrites, cmp_eqtransform)
    ____________________
    '''
    return memmethod(_apply_rewrites, _get_rewriters(transformfunc, canon_ref))


get_rewriters_matchrewrite = memmethod(_get_rewriters, cmp_matchtransform)
get_rewriters_replacements = memmethod(_get_rewriters, cmp_eqtransform)
modulefuncs(["get_rewriters_matchrewrite", "get_rewriters_replacements"])

apply_rewrites_matchrewrite = memmethod(_get_apply_rewrites, cmp_matchtransform)
apply_rewrites_replacements = memmethod(_get_apply_rewrites, cmp_eqtransform)
modulefuncs(["apply_rewrites_matchrewrite", "apply_rewrites_replacements"])


@modulefunc
def _rewriter(transformfunc: Ⲉƒx, pattern: opterm=None, rewrite: opterm=None, /):
    '''
    Binds ʻtransformfuncʼ (cmp_matchtransform, cmp_eqtransform, or other method(_cmp_transform, <cmp-func>)) to a ʻpatternʼ and a ʻrewriteʼ expression.  If called with incomplete args, the output is a partially-bound memmethod.  Fully-bound, returns a callable that can be applied to an expression object for rewrite or replace transformations:
        >>> matchrewriter = _rewriter(cmp_matchtransform)
        >>> rewriter = matchrewriter(X/Y, rewrite=X*Y**-1)
        >>> rewriter((a/2 - 3/b))
        (a*0.5 - 3*b**-1)
    ____________________
    Predefined globals:
    |    matchrewriter := memmethod(_rewriter, cmp_matchtransform)
    |    eq_rewriter := memmethod(_rewriter, cmp_eqtransform)
    ____________________
    '''
    if (pattern is None):  return memmethod(_rewriter, transformfunc)
    if (rewrite is None):  return memmethod(_rewriter, transformfunc, pattern)
    return memmethod(transformfunc, pattern, rewrite)

matchrewriter = memmethod(_rewriter, cmp_matchtransform)
eq_rewriter = memmethod(_rewriter, cmp_eqtransform)
modulefuncs(["matchrewriter", "eq_rewriter"])

opterm.matchrewriter = property(matchrewriter)
opterm.eq_rewriter = property(eq_rewriter)


#        ★        #        ★        #        ★        #        ★        #        ★        #

__globals__ = (lambda:x).__globals__

"""
x = opvar('a', value=Unknown)[ⲈLᴛ]
print(f"\n{x = }\n{x.value = }\n{x.referent = }\n{x.referent_value = }\n")
x = opvar('b', value=x)
print(f"\n{x = }\n{x.value = }\n{x.referent = }\n{x.referent_value = }\n")
x = opvar('c', value=5.0)
print(f"\n{x = }\n{x.value = }\n{x.referent = }\n{x.referent_value = }\n")
x = opvar('d', value=x)
print(f"\n{x = }\n{x.value = }\n{x.referent = }\n{x.referent_value = }\n")
"""
