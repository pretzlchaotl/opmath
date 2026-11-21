
import sys, os
from more_itertools import unique_everseen
sys.path.append(__file__.rsplit("abcd", 2)[0])
from abcd import _abcd_, _collections_abcd_, _numbers_abcd_, _mathdomains_abcd_
from abcd._abcd_ import *
from abcd._numbers_abcd_ import *
from abcd._collections_abcd_ import *
from abcd._mathdomains_abcd_ import *


__doc__ = _abcd_.__doc__


[_abcd_, _collections_abcd_, _numbers_abcd_, _mathdomains_abcd_, 
        # function
    get_name, get_nameᐩ, _check_methods, get_cache_token, 
    abstractmethod, update_abstractmethods, 
    ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ, _is_param_expr, _type_repr, 
    deduce_domain, get_annotations, _get_opdomains_from_annotations, deduce_opdomains, 
    typecheck_isinstance, typecheck_issubclass, _GenericAlias_typage_typecheck, 
        # ABCDMeta
    Auto, 
    Object, Oblivion, Type, NonFinite, 
    Callable, Hashable, 
    Lattice, Bool, 
    Number, Complex, Real, Rational, Integral, Natural, 
    Awaitable, Coroutine, AsyncIterable, AsyncIterator, AsyncGenerator, 
    Iterable, Iterator, Reversible, Generator, Sized, Container, Collection, Buffer, 
    Set, MutableSet, Mapping, MappingView, KeysView, ItemsView, ValuesView, MutableMapping, 
    Sequence, MutableSequence, Stringlike, Vector, 
    ⲈXx, ⲈOʙ, ⲈOᴠ, ⲈFᴄ, 
    ⲈIᴛ, ⲈCᴛ, ⲈSᴘ, ⲈMᴘ, ⲈSવ, ⲈCʜ, ⲈVᴄ, 
    ⲈUɴ, ⲈCɴ, ⲈRɴ, ⲈQɴ, ⲈZɴ, ⲈNɴ, 
    ⲈLᴛ, ⲈBʟ, 
    Ⲉ_, Ⲉƒx, Ⲉⲉⰵ, Ⲉⵁ, Ⲉǃǃ, 
        # GenericAlias
    FuncDomainsTypage, 
        # _ⲈƒxGenericAlias
    PredicateTypage, RelationTypage, NAryRelationTypage, 
        # UnionType
    DomainType, TypeDescriptorTypage, TypecheckTypage, TypageCheckTypage, SequenceIndexTypage, 
        # type
    function, method, 
    _GenericAlias, TypeUnion, ABCDMeta, 
    ABCD_UnionSet, ABCD_InvertedSet, ABCD_IntersectionSet, _ABCD_SetStructure_Base, 
        # builtin_function_or_method
    ꓽtypeꓸ__new__, 
        # GenericAliasMeta
    GenericAlias, _CallableGenericAlias, _ⲈƒxGenericAlias, 
        # tuple
    TypeDescriptorTypes, DomainTypage, MathDomainTypes, 
        # list
    _domainnicknames, 
]

__all__ = [
    "_abcd_", "_collections_abcd_", "_numbers_abcd_", "_mathdomains_abcd_", 
        # function
    "get_name", "get_nameᐩ", "_check_methods", "get_cache_token", 
    "abstractmethod", "update_abstractmethods", 
    "ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ", "_is_param_expr", "_type_repr", 
    "deduce_domain", "get_annotations", "_get_opdomains_from_annotations", "deduce_opdomains", 
    "typecheck_isinstance", "typecheck_issubclass", "_GenericAlias_typage_typecheck", 
        # ABCDMeta
    "Auto", 
    "Object", "Oblivion", "Type", "NonFinite", 
    "Callable", "Hashable", 
    "Lattice", "Bool", 
    "Number", "Complex", "Real", "Rational", "Integral", "Natural", 
    "Awaitable", "Coroutine", "AsyncIterable", "AsyncIterator", "AsyncGenerator", 
    "Iterable", "Iterator", "Reversible", "Generator", "Sized", "Container", "Collection", "Buffer", 
    "Set", "MutableSet", "Mapping", "MappingView", "KeysView", "ItemsView", "ValuesView", "MutableMapping", 
    "Sequence", "MutableSequence", "Stringlike", "Vector", 
    "ⲈXx", "ⲈOʙ", "ⲈOᴠ", "ⲈFᴄ", 
    "ⲈIᴛ", "ⲈCᴛ", "ⲈSᴘ", "ⲈMᴘ", "ⲈSવ", "ⲈCʜ", "ⲈVᴄ", 
    "ⲈUɴ", "ⲈCɴ", "ⲈRɴ", "ⲈQɴ", "ⲈZɴ", "ⲈNɴ", 
    "ⲈLᴛ", "ⲈBʟ", 
    "Ⲉ_", "Ⲉƒx", "Ⲉⲉⰵ", "Ⲉⵁ", "Ⲉǃǃ", 
        # GenericAlias
    "FuncDomainsTypage", 
        # _ⲈƒxGenericAlias
    "PredicateTypage", "RelationTypage", "NAryRelationTypage", 
        # UnionType
    "DomainType", "TypeDescriptorTypage", "TypecheckTypage", "TypageCheckTypage", "SequenceIndexTypage", 
        # type
    "function", "method", 
    "_GenericAlias", "TypeUnion", "ABCDMeta", 
    "ABCD_UnionSet", "ABCD_InvertedSet", "ABCD_IntersectionSet", "_ABCD_SetStructure_Base", 
        # builtin_function_or_method
    "ꓽtypeꓸ__new__", 
        # GenericAliasMeta
    "GenericAlias", "_CallableGenericAlias", "_ⲈƒxGenericAlias", 
        # tuple
    "TypeDescriptorTypes", "DomainTypage", "MathDomainTypes", 
        # list
    "_domainnicknames", 
]

