import sys
from itertools import chain, count, repeat, cycle
from types import DynamicClassAttribute
from inspect import getfullargspec, CO_VARARGS, CO_VARKEYWORDS
sys.path.append(__file__.rsplit("futilities", 1)[0])
from abcd._mathdomains_abcd_ import Iterable, Callable
from futilities.aliases import (
    function, method, code as CodeType, 
    mappingproxy, 
    )


_globs = list(globals())


__doc__ = "Miscellaneous convenience functions for manipulating, copying, modifying, defining, and analyzing instances, functions, and classes."

__all__ = [
    'DefaultObject'
    
    'get_name', 'get_name_or_str', 
    'get_func', 'get_code', 
    'get_co_dict', 'get_closure', 
    
    'code_co_attrnames', 'code_co_attrnames_grouped', 
    
    'copy_function', 'copy_code', 
    'rename_function', 'edit_function', 
    
    'classproperty', 'hashproperty', 
    
    'sovereign', '_ꜱᴛʀ', 
    
    'g_constfunc', 'constfuncs_all', 
    'const_False', 'const_True', 'const_None', 'const_0', 'const_1', 'const_inf', 'const_nan', 
    
    'new_singleton_instance', 'singleton_type', 
    'is_singleton', 'register_singleton', 
    
    
    'get_nin', 
    ]



_Dflt = DefaultObject = object.__new__(type('DefaultObjectType', (), 
                                                                                        {'__new__': None, '__init__': None, 
                                                                                        '__repr__': lambda self: "DefaultObject"}))



"  ________________  Attribute Finder Utilites  ________________  "

def get_name(obj, /, default=str, *, names: Iterable[str]=None): #('name', '__name__', '_name')):
    "Returns obj.__name__ if available, or obj.name, obj._name, otherwise default(obj) or just default."
    if names is None:  return getattr(obj, '__name__', None) \
                                             or getattr(obj,     'name',      None) \
                                             or getattr(obj,   '_name',      None) \
                                             or (default(obj) if callable(default) else default)
    for name in names:
        try:
            attr = getattr(obj, name)
        except AttributeError:  pass
        else:  return attr
    else:  return (default(obj) if callable(default) else default)

def get_name_or_str(obj, *, strf=str, reprf=repr):
    "Returns obj.__name__ if available, or obj.name, obj._name, otherwise str(obj) (or repr for strings)."
    return getattr(obj, '__name__', None) \
            or getattr(obj,     'name',      None) \
            or getattr(obj,   '_name',      None) \
        or (reprf(obj) if isinstance(obj, str) else strf(obj))


def get_func(f, default=_Dflt, get_attrname=False):
    "Returns f.__func__ if available, or f.func, or f.fget.  If ‘default’ is Ellipsis, returns ‘f’ upon failure, otherwise ‘default’ is returned."
    if not get_attrname:  return getattr(f, '__func__', None) \
                                                      or getattr(f,     'func',     None) \
                                                      or getattr(f,      'fget',     None) \
                                                  or (f if default is _Dflt else default)
    for name in ('__func__', 'func', 'fget'):
        try:
            fcf = getattr(f, name)
        except AttributeError:  pass
        else:  return (name, fcf)
    else:  return (None, (fcf if default is _Dflt else default))


def get_code(f, default=_Dflt, get_attrname=False):
    "Returns the code attribute of ‘f’.  Methodology copied and altered from the dis module.  If ‘default’ is Ellipsis, returns ‘f’ upon failure, otherwise ‘default’ is returned."
    ##★##    Extract internal function object if ‘f’ is, method, property, or similar.
    f = get_func(f, get_attrname=False)
    #if isinstance(f, code): r):  return (True, f) if get_attrname else f
    ##★##    Extract code object by trying possible attrnames 1 by 1 in order of decreasing likelihood:
    ##    {function  '__code__',  generator: 'gi_code',   (async generator): 'ag_code',  coroutine: 'cr_code'}
    if not get_attrname:  return getattr(f, '__code__', 0) \
                                                      or getattr(f, 'gi_code', 0) \
                                                      or getattr(f, 'ag_code', 0) \
                                                      or getattr(f, 'cr_code', 0) \
                                                  or (f if default is _Dflt else default)
    for name in ('__code__', 'gi_code', 'ag_code', 'cr_code'):
        try:
            fco = getattr(f, name)
        except AttributeError:  pass
        else:  return (name, fco)
    else:  return (None, (f if default is _Dflt else default))



"  ________________  FunctionType Copying & Editing Utilites  ________________  "

def copy_function(func: function, name: str=None, *, doc: str=_Dflt, code: CodeType=None, globals: dict=_Dflt, defaults: tuple=_Dflt, kwdefaults: dict=_Dflt, closure: tuple=_Dflt, annotations: dict=_Dflt, attributes: dict=_Dflt, internal_names_replacements: dict=_Dflt, **co_replacements):
    "Returns a copy of 'func' with the given replacements.  Keyword-Parameters left alone are set to DefaultObject by default, and will not be altered in order to allow setting those attributes to None, if desired.  Optional 'internal_names_replacements' dict should map names in co_names, co_varnames, co_freevars, and co_cellvars to their replacements (unless those names are kwargs in co_replacements)."
    if code is None:
        code = get_code(func)
    if name is None:
        name = func.__name__
    fname = get_name(func)
    qualname = func.__qualname__.removesuffix(fname) + name
    co_replacements['co_name'] = func.__name__ = name
    co_replacements['co_qualname'] = func.__qualname__ = qualname
    if doc is not _Dflt:
        fdoc = func.__doc__ = doc
        fco_consts = co_replacements.get('co_consts', None) or code.co_consts
        co_replacements['co_consts'] = fco_consts = (fdoc, *fco_consts[1:])
    if internal_names_replacements is not _Dflt:
        for coname in ("co_names", "co_varnames", "co_freevars", "co_cellvars"):
            if coname not in co_replacements:
                co_replacements[coname] = tuple(internal_names_replacements.get(n, n) \
                                                                             for n in getattr(code, coname))
    code = code.replace(**co_replacements)
    newfunc = function(code=code, 
                                                        globals=func.__globals__ if globals is _Dflt else globals, 
                                                        name=name, 
                                                        argdefs=func.__defaults__ if defaults is _Dflt else defaults, 
                                                        closure=func.__closure__ if closure is _Dflt else closure, 
                                                        kwdefaults=func.__kwdefaults__ if kwdefaults is _Dflt else kwdefaults
                                                        )
    if (globals is not _Dflt) and (newfunc.__globals__ is not globals):
        newfunc.__globals__ = globals
    newfunc.__annotations__ = func.__annotations__ if annotations is _Dflt else annotations
    if (attributes is _Dflt) and (func.__dict__.keys() - newfunc.__dict__.keys()):
        newfunc.__dict__.update(func.__dict__)
    elif (attributes is not _Dflt):
        newfunc.__dict__ = attributes
    return newfunc


def edit_function(func: function, name: str=None, *, doc: str=_Dflt, code: CodeType=None, globals: dict=_Dflt, defaults: tuple=_Dflt, kwdefaults: dict=_Dflt, closure: tuple=_Dflt, annotations: dict=_Dflt, internal_names_replacements: dict=None, co_replacements: dict=None, **kwargs):
    "Returns 'func' with the given replacements.  Keyword-Parameters set to DefaultObject will not be altered.  Optional 'internal_names_replacements' dict should map names in co_names, co_varnames, co_freevars, and co_cellvars to their replacements (unless those names are kwargs in co_replacements)."
    if func is _Dflt or func is None:
        vars_ = vars()
        vars_.pop('func')
        return (lambda f: edit_function(f, **vars_))
    if code is None:
        code = get_code(func)
    if kwargs:
        if co_keys := kwargs.keys() & code_co_attrnames:
            if (co_replacements is None):
                co_replacements = {}
            co_replacements.update({k: kwargs.pop(k) for k in co_keys})
        if kwargs:
            if (internal_names_replacements is None):
                internal_names_replacements = kwargs
            else:
                internal_names_replacements.update(kwargs)
    if name is not None:
        fname = get_name(func)
        qualname = func.__qualname__.removesuffix(fname) + name
        co_replacements['co_name'] = func.__name__ = name
        co_replacements['co_qualname'] = func.__qualname__ = qualname
    if doc is not _Dflt:
        fdoc = func.__doc__ = doc
        co_replacements['co_consts'] = fco_consts = (fdoc, *code.co_consts[1:])
    if internal_names_replacements is not _Dflt:
        for coname in ("co_names", "co_varnames", "co_freevars", "co_cellvars"):
            if coname not in co_replacements:
                co_replacements[coname] = tuple(internal_names_replacements.get(n, n) \
                                                                             for n in getattr(code, coname))
    if co_replacements:
        code = code.replace(**co_replacements)
    
    func.__code__ = code
    if globals is not _Dflt:
        func.__globals__ = globals
    if defaults is not _Dflt:
        func.__defaults__ = defaults
    if closure is not _Dflt:
        func.__closure__ = closure
    if kwdefaults is not _Dflt:
        func.__kwdefaults__ = kwdefaults
    if annotations is not _Dflt:
        func.__annotations__ = annotations
    
    return func


def rename_function(f, name, qualprefix="<locals>", alter_localnames=False, doc=_Dflt, other_localnames: dict=None, **kwargs):
    "Renames a function ‘f’ to ‘name’.  Applies to the .__name__ & .__qualname__ attributes, and .__code__.(co_name, †co_names, †co_varnames) attributes [†if ‘alter_localnames’ is true.  To replace other names in these attributes, set key:value pairs in ‘other_localnames’ to oldname: newname."
    fname = f.__name__
    name = name or fname
    
    if qualprefix:
        fname = f"{qualprefix}.{fname}"
    f.__qualname__ = qualname = f.__qualname__.removesuffix(fname) + name
    f.__name__ = name
    
    fco = f.__code__
    
    if (doc is not _Dflt):
        f.__doc__ = doc
        if (not alter_localnames):
            f.__code__ = fco.replace(co_consts=(doc, *fco.co_consts[1:]))
    
    if alter_localnames:
        if other_localnames is None:
            other_localnames = {}
        other_localnames[fname] = name
        fco_consts = kwargs.pop('co_consts', fco.co_consts)
        if kwargs:
            other_localnames |= kwargs
        f.__code__ = fco.replace(co_name=name, co_qualname=qualname, \
                                     co_names=tuple(other_localnames.get(n, n) for n in fco.co_names), \
                                     #co_varnames=tuple(other_localnames.get(n, n) for n in fco.co_varnames), \
                                     co_freevars=tuple(other_localnames.get(n, n) for n in fco.co_freevars), \
                                     co_cellvars=tuple(other_localnames.get(n, n) for n in fco.co_cellvars), \
                                     co_consts=((fco_consts[0] if (doc is _Dflt) else doc), *fco_consts[1:]))
    else:
        f.__code__ = fco.replace(co_name=name, co_qualname=qualname)
    
    return f


class classproperty(DynamicClassAttribute, property):
    """A property that works at both class and instance level."""\
    "\n(Pretty sure I stole this; I don’t remember where from)"
    __slots__ = "fget", "fset", "fdel", "_name", "__isabstractmethod__"
    
    def __get__(self, instance, owner):
        # If accessed from instance or class, always call on the class
        return self.fget(owner)
    def __set__(self, instance, value):
        if self.fset is None: raise AttributeError("can't set attribute")
        # Pass class to setter, not instance
        self.fset(None if instance is None else type(instance), value)
    
    def setter(self, fset):  return classproperty(self.fget, fset)


def hashproperty(ref: dict=None, setter: bool=True, deleter: bool=False, doc: str=None, _property=property):
    "Returns a property object derived from a reference dictionary (creates a defaultdict(lambda: None) if ʽrefʼ is None).  Useful for giving subclasses of immutable types mutable attributes."
    if (ref is None):
        ref = defaultdict(lambda: None)
    setter = ref.__setitem__ if setter else None
    deleter = ref.__delitem__ if deleter else None
    return _property(ref.__getitem__, setter, deleter, doc=doc)




"  ________________  Sovereign Decorator  ________________  "


sovereign_methods_ref = {
    'copy': (function, {'self': object}, None, None), 
    'from_bytes': (classmethod, {'cls': type, 'bytes': bytes, 'byteorder': str, 'signed': bool}, None, {'signed': False}), 
    'fromhex': (classmethod, {'cls': type, 'string': str}, None, None), 
    '__abs__': (function, {'self': object}, None, None), 
    '__invert__': (function, {'self': object}, None, None), 
    '__neg__': (function, {'self': object}, None, None), 
    '__pos__': (function, {'self': object}, None, None), 
    'conjugate': (function, {'self': object}, None, None), 
    '__floor__': (function, {'self': object}, None, None), 
    '__ceil__': (function, {'self': object}, None, None), 
    '__trunc__': (function, {'self': object}, None, None), 
    '__round__': (function, {'self': object, 'ndigits': int}, (0,), None), 
    '__or__': (function, {'self': object, 'other': object}, None, None), 
    '__and__': (function, {'self': object, 'other': object}, None, None), 
    '__xor__': (function, {'self': object, 'other': object}, None, None), 
    '__lshift__': (function, {'self': object, 'other': object}, None, None), 
    '__rshift__': (function, {'self': object, 'other': object}, None, None), 
    '__add__': (function, {'self': object, 'other': object}, None, None), 
    '__sub__': (function, {'self': object, 'other': object}, None, None), 
    '__mul__': (function, {'self': object, 'other': object}, None, None), 
    '__truediv__': (function, {'self': object, 'other': object}, None, None), 
    '__pow__': (function, {'self': object, 'other': object}, None, None), 
    '__floordiv__': (function, {'self': object, 'other': object}, None, None), 
    '__mod__': (function, {'self': object, 'other': object}, None, None), 
    '__matmul__': (function, {'self': object, 'other': object}, None, None), 
    '__divmod__': (function, {'self': object, 'other': object}, None, None), 
    '__ror__': (function, {'self': object, 'other': object}, None, None), 
    '__rand__': (function, {'self': object, 'other': object}, None, None), 
    '__rxor__': (function, {'self': object, 'other': object}, None, None), 
    '__rlshift__': (function, {'self': object, 'other': object}, None, None), 
    '__rrshift__': (function, {'self': object, 'other': object}, None, None), 
    '__radd__': (function, {'self': object, 'other': object}, None, None), 
    '__rsub__': (function, {'self': object, 'other': object}, None, None), 
    '__rmul__': (function, {'self': object, 'other': object}, None, None), 
    '__rtruediv__': (function, {'self': object, 'other': object}, None, None), 
    '__rpow__': (function, {'self': object, 'other': object}, None, None), 
    '__rfloordiv__': (function, {'self': object, 'other': object}, None, None), 
    '__rmod__': (function, {'self': object, 'other': object}, None, None), 
    '__rmatmul__': (function, {'self': object, 'other': object}, None, None), 
    '__rdivmod__': (function, {'self': object, 'other': object}, None, None), 
    
    'union': (function, {'self': object, 'other': Iterable}, None, None), 
    'intersection': (function, {'self': object, 'other': Iterable}, None, None), 
    'symmetric_difference': (function, {'self': object, 'other': Iterable}, None, None), 
    'difference': (function, {'self': object, 'other': Iterable}, None, None), 
    'capitalize': (function, {'self': object}, None, None), 
    'title': (function, {'self': object}, None, None), 
    'upper': (function, {'self': object}, None, None), 
    'lower': (function, {'self': object}, None, None), 
    'casefold': (function, {'self': object}, None, None), 
    'swapcase': (function, {'self': object}, None, None), 
    'zfill': (function, {'self': object, 'width': int}, None, None), 
    'expandtabs': (function, {'tabsize': int, 'self': object}, (8,), None), 
    'center': (function, {'self': object, 'width': int, 'fillchar': str}, (' ',), None), 
    'ljust': (function, {'self': object, 'width': int, 'fillchar': str}, (' ',), None), 
    'rjust': (function, {'self': object, 'width': int, 'fillchar': str}, (' ',), None), 
    'removeprefix': (function, {'self': object, 'prefix': str}, None, None), 
    'removesuffix': (function, {'self': object, 'suffix': str}, None, None), 
    'lstrip': (function, {'self': object, 'chars': str}, (None,), None), 
    'strip': (function, {'self': object, 'chars': str}, (None,), None), 
    'rstrip': (function, {'self': object, 'chars': str}, (None,), None), 
    'join': (function, {'self': object, 'iterable': Iterable}, None, None), 
    'format': (function, {'self': object}, None, None), 
    'format_map': (function, {'self': object, 'table': dict}, None, None), 
    'translate': (function, {'self': object, 'table': dict}, None, None), 
    'replace': (function, {'self': object, 'old': str, 'new': str, 'count': int}, (-1,), None), 
    '__add__': (function, {'self': object, 'other': object}, None, None), 
    '__mul__': (function, {'self': object, 'other': object}, None, None), 
    '__mod__': (function, {'self': object, 'other': object}, None, None), 
    '__rmul__': (function, {'self': object, 'other': object}, None, None), 
    '__rmod__': (function, {'self': object, 'other': object}, None, None), 
}


mutable_methodnames = [
    '__setattr__', '__delattr__', 
    '__setitem__', '__delitem__', 
    '__ior__', '__iand__', '__ixor__', '__ilshift__', '__irshift__', 
        '__iadd__', '__isub__', '__imul__', '__itruediv__', '__ipow__', 
        '__ifloordiv__', '__imod__', 
        '__imatmul__', 
    'sort', 'reverse', 
    'add', 'append', 'insert', 'extend', 
    'update', 'intersection_update', 'symmetric_difference_update', 'difference_update', 
    'remove', 'discard', 'pop', 'clear', 
    ]


def sovereign(cls: type=None, *, base: type|tuple[type]=None, inherits_from_base: bool=True, ignore: tuple[str]=(), ignore_from_cls_namespace: bool=False, methods_ref_supplement: dict=None, nullify_methods: bool|tuple[str]=False, nullify_mutable_methods: bool=False):
    if cls is None:
        "Edits a class’ namespace so that all inherited methods which produce an instance of the same class are updated to do the same with the new class (so an int subclass, Z, would produce instances of Z when added, multiplied, etc.).  Can be used as a decorator (leave ʻclsʻ as default None) or as a regular function.  Methodnames in ʻignoreʼ will not be converted, and if ʻignore_from_cls_namespaceʻ is true, methods defined in the new class’ namespace will be ignored as well.  If ʻnullify_methodsʼ, the methods in question will all be set to raise a NotImplementedError.  Alternatively, the parameter may be set to a list of names to nullify.  If ʻnullify_mutable_methodsʼ, then methods which alter or update an instance will be set to raise a NotImplementedError."
        vars_ = dict(vars())
        vars_.pop("cls")
        return (lambda cls: sovereign(cls, **vars_))
    
    if base is None:
        base = cls
    elif isinstance(base, tuple):
        base = type("_", base, {})
    
    if (ignore is sovereign_methods_ref):
        methods_ref = (methods_ref_supplement or {})
        ignore = ()
    elif (methods_ref_supplement is not None):
        methods_ref = sovereign_methods_ref | methods_ref_supplement
    else:
        methods_ref = sovereign_methods_ref
    
    if ignore_from_cls_namespace:
        ignore = tuple(chain(ignore, cls.__dict__))
    
    if nullify_methods:
        if (nullify_methods == True):
            nullify_methods = methods_ref
        else:
            for name in filter(dir(base).__contains__, nullify_methods):
                if ignore and (name in ignore):  continue
                setattr(cls, name, _g_raise_notimplemented_error(name))
    
    _done = {}
    for name in filter(dir(base).__contains__, methods_ref):
        if ignore and (name in ignore):  continue
        _method = getattr(cls, name, None)
        if (_method is None):  continue
        _method = _g_raise_notimplemented_error(name) \
                             if nullify_methods and (name in nullify_methods) \
                             else  _sovereign_make_method(_method, name, methods_ref, _done)
        setattr(cls, name, _method)
    
    if nullify_mutable_methods:
        for name in filter(dir(base).__contains__, mutable_methodnames):
            if ignore and (name in ignore):  continue
            setattr(cls, name, _g_raise_notimplemented_error(name))
    
    if inherits_from_base:
        cls._ɴᴇᴡ = property(type)
    else:
        cls._ɴᴇᴡ = cls
    
    cls._sovereign_methods = tuple(filter(dir(base).__contains__, methods_ref))
    return cls

def _g_raise_notimplemented_error(methodname: str):
    def _raise_notimplemented_error(self, *_, **__):
        raise NotImplementedError(\
            f"{type(self).__name__!r} does not define a {methodname!r} method.")
    rename_function(_raise_notimplemented_error, methodname, alter_localnames=False)
    return _raise_notimplemented_error
def _ggg_raise_notimplemented_error(*methodnames: str):
    return list(map(_g_raise_notimplemented_error, methodnames))


def _sovereign_make_method(_method: Callable, /, name: str=None, methods_ref: dict=mappingproxy(sovereign_methods_ref), _done: dict=None, _printout_kwargs: dict|bool=False):
    if (name is None):
        name = get_name(_method)
    typeof, annots, defaults, kwdefs = methods_ref[name]
    _func = get_func(_method)
    if doprint := _printout_kwargs:
        _done = None
        if (_printout_kwargs is True):
            _printout_kwargs = {}
    if _done and (_func in _done):
        func = _done[_func]
    else:
        returntype = annots.pop('return', _Dflt)
        paramstrlist = [(f'{k!s}: {get_name(v)!s}') for k, v in annots.items()] if doprint \
                            else list(annots)
        paramstr = ', '.join(annots)
        argstr = paramstr
        if kwdefs:
            i = 0
            for k, v in kwdefs.items():
                ka = k
                if doprint:
                    a = get_name(annots[k])
                    ka = f"{k!s}: {a!s}"
                if not i:
                    paramstr = paramstr.replace(ka, f'*, {k!s}')
                    i = 1
                paramstr = paramstr.replace(ka, f'{ka!s}={v!r}')
                argstr = argstr.replace(ka, f'{k!s}={k!s}')
        wrapstr = ''
        if (returntype is _Dflt):
            if ('self' in annots):
                wrapstr = 'self._ɴᴇᴡ'
            elif ('cls' in annots):
                wrapstr = 'cls'
        if doprint:
            defstr = f"    def {name}({paramstr}):  return {wrapstr}(super().{name}({argstr}))"
            if (_func is not _method):
                defstr = f"    @{type(_method).__name__}\n{defstr}"
            return print(defstr, **_printout_kwargs)
        defstr = f"lambda {paramstr}: {wrapstr}(_func({argstr}))"
        func = eval(defstr, locals(), locals())
        rename_function(func, name, alter_localnames=False)
        if _done:
            _done[_func] = func
    if (_func is not _method):
        if isinstance(_method, (classmethod, staticmethod)):  return type(_method)(func)
        elif isinstance(_method, property):
            return type(_method)(func, _method.fset, _method.fdel, _method.__doc__)
        try:  return type(_method)(func)
        except (TypeError, ValueError):  pass
    return func




_ꜱᴛʀ_nullified_methodnames = [
    "isalnum", "isalpha", "isascii", "isdecimal", "isdigit", "isidentifier", "islower", "isnumeric", "isprintable", "isspace", "istitle", "isupper", "endswith", "startswith", 
    "count", "index", "find", "rindex", "rfind", 
    "partition", "rpartition", "splitlines", "split", "rsplit", 
    "capitalize", "casefold", "title", "upper", "lower", "swapcase", 
    "zfill", "expandtabs","center", "ljust", "rjust", 
    "removeprefix", "removesuffix", "lstrip", "rstrip", "strip", 
    "replace", "encode", "format", "format_map", "join", "translate", 
    "maketrans", 
    ] + [
    "__lt__", "__gt__", "__le__", "__ge__", 
    "__add__", "__mul__", "__rmul__", "__mod__", "__rmod__", 
    "__iter__", "__len__", "__contains__", "__getitem__", 
    ]
@sovereign(base=str, nullify_methods=_ꜱᴛʀ_nullified_methodnames)
class _ꜱᴛʀ(str):
    "A string subclass with iterable and str methods nullified.  Good base for tokens or variables."

#del _ꜱᴛʀ.__lt__, _ꜱᴛʀ.__gt__, _ꜱᴛʀ.__le__, _ꜱᴛʀ.__ge__, _ꜱᴛʀ.__add__, _ꜱᴛʀ.__mul__, _ꜱᴛʀ.__rmul__, _ꜱᴛʀ.__mod__, _ꜱᴛʀ.__rmod__, _ꜱᴛʀ.__iter__, _ꜱᴛʀ.__len__, _ꜱᴛʀ.__contains__, _ꜱᴛʀ.__getitem__
#del _ꜱᴛʀ.isalnum, _ꜱᴛʀ.isalpha, _ꜱᴛʀ.isascii, _ꜱᴛʀ.isdecimal, _ꜱᴛʀ.isdigit, _ꜱᴛʀ.isidentifier, _ꜱᴛʀ.islower, _ꜱᴛʀ.isnumeric, _ꜱᴛʀ.isprintable, _ꜱᴛʀ.isspace, _ꜱᴛʀ.istitle, _ꜱᴛʀ.isupper, _ꜱᴛʀ.endswith, _ꜱᴛʀ.startswith, _ꜱᴛʀ.count, _ꜱᴛʀ.index, _ꜱᴛʀ.find, _ꜱᴛʀ.rindex, _ꜱᴛʀ.rfind, _ꜱᴛʀ.partition, _ꜱᴛʀ.rpartition, _ꜱᴛʀ.splitlines, _ꜱᴛʀ.split, _ꜱᴛʀ.rsplit, _ꜱᴛʀ.capitalize, _ꜱᴛʀ.casefold, _ꜱᴛʀ.title, _ꜱᴛʀ.upper, _ꜱᴛʀ.lower, _ꜱᴛʀ.swapcase, _ꜱᴛʀ.zfill, _ꜱᴛʀ.expandtabs, _ꜱᴛʀ.center, _ꜱᴛʀ.ljust, _ꜱᴛʀ.rjust, _ꜱᴛʀ.removeprefix, _ꜱᴛʀ.removesuffix, _ꜱᴛʀ.lstrip, _ꜱᴛʀ.rstrip, _ꜱᴛʀ.strip, _ꜱᴛʀ.replace, _ꜱᴛʀ.encode, _ꜱᴛʀ.format, _ꜱᴛʀ.format_map, _ꜱᴛʀ.join, _ꜱᴛʀ.translate, _ꜱᴛʀ.maketrans





"  ________________  Singleton Type Instantiator  ________________  "


mappingproxy = type(type.__dict__)

def _do_nothing(cls, *args, **kwargs):
    "A convenience function that does nothing."
    pass
_singleton_default_namespace = mappingproxy({
    "__slots__": (), 
    "__init_subclass__": _do_nothing, 
    "__init__": None, 
    "copy": None, 
    "_instance": NotImplemented,
    })
def new_singleton_instance(name: str, bases: tuple[type]=(), namespace: dict=mappingproxy({}), *, doc: str=None, bool_value: bool=DefaultObject, preserve_attributes: tuple[str]=(), overwrite=False):
    "Create a new single-instance type like NoneType. EllipsisType, or NotImplementedType, then return its lone instance."
    if not overwrite:
        try:  return singleton_registry[name]
        except KeyError:  pass
    
    _namespace = _singleton_create_namespace(name, doc, bool_value, preserve_attributes, namespace)
    typename = f"{name}Type"
    
    cls = type(typename, (), _namespace)
    
    if ("_instance" not in preserve_attributes):
        _namespace["_instance"] = _instance = object.__new__(cls)
        type.__setattr__(cls, "_instance", _instance)
    
    for name, value in (_namespace.items() - namespace.items()):
        if preserve_attributes and (name in preserve_attributes):  continue
        if (value is None):
            try:
                type.__delattr__(cls, name)
            except TypeError:  pass
    
    singleton_registry.register(_instance, safe=not overwrite)
    return _instance


def singleton_type(cls: type=None, *, instance_name: str=None, doc: str=DefaultObject, bool_value: object=DefaultObject, preserve_attributes: tuple[str]=(), overwrite=False, base: type=object):
    "    Decorator for defining singleton classes.  If ‘instance_name’ is left as None, it defaults to cls.__name__.removesuffix('Type').  The .__bool__() method will only be defined if ‘bool_value’ is not DefaultObject.  The names in ('__name__', '__init_subclass__', '__init__', 'copy', '__new__', '__repr__', '__str__', '__hash__', '__bool__', '_instance') are overwritten by this function.  Any of those names included in the ‘preserve_attributes’ tuple will be skipped (as will '__bool__' if ‘bool_value’ is not defined).  If ‘overwrite’, the class’ instance will replace any currently registered singleton of the same name, otherwise, if such singleton already exists, a LookupError will be raised.\n"\
    "    This returns the singleton instance, not the type, and cls.__name__ is defined to be replaced by f'{instance_name}Type', unless included in preserve_attributes.  Standard usage allows for:"'''
        >>> @singleton_type(bool_value="")
        >>> class Undefined:
        >>>     pass
        >>> Undefined
        Undefined
        >>> type(Undefined).__name__
        UndefinedType
    '''
    #"    This only returns the updated cls object.  To obtain the singleton itself, use cls._instance or the cls() constructor."
    if (cls is None):
        vars_ = dict(vars())
        vars_.pop("cls")
        return partial(singleton_type, **vars_)
        return (lambda cls=None, **kwg: singleton_type(cls, **(vars_ | kwg)))
    
    if (instance_name is None):
        instance_name = cls.__name__.removesuffix("Type")
    if ("__name__" not in preserve_attributes):
        cls.__name__ = f"{instance_name}Type"
    
    namespace_updates = _singleton_create_namespace(instance_name, doc, bool_value, preserve_attributes, {})
    
    if issubclass(base, type):
        _instance = base.__new__(cls, instance_name, (), {})
    else:
        _instance = base.__new__(cls)
    
    if ("_instance" not in preserve_attributes):
        namespace_updates["_instance"] = _instance
    
    for name, value in namespace_updates.items():
        if preserve_attributes and (name in preserve_attributes):  continue
        type.__setattr__(cls, name, value)
        if (value is None):
            try:
                type.__delattr__(cls, name)
            except TypeError:  pass
    
    singleton_registry.register(_instance, safe=not overwrite)
    return _instance

def _singleton_create_namespace(instance_name: str, doc: str, bool_value: object, preserve_attributes: tuple[str], namespace: dict, cls: type=None):
    "(helper for the singleton_type() and new_singleton_instance() functions)"
    updates = {}
    
    if (doc is not DefaultObject):
        updates["__doc__"] = doc
    
    def __new__(cls, *args, **kwargs):  return cls._instance
    updates["__new__"] = __new__
    
    def __repr__(self):  return instance_name
    def __str__(self):  return instance_name
    updates["__repr__"] = __repr__
    updates["__str__"] = __str__
    
    def __hash__(self):  return hash((type(self), str(self)))
    updates["__hash__"] = __hash__
    
    if (bool_value is not DefaultObject):
        if callable(bool_value):
            __bool__ = bool_value
        else:
            def __bool__(self):  return bool_value
        updates["__bool__"] = __bool__
    
    if preserve_attributes:
        for name in (updates.keys() & preserve_attributes):
            updates.pop(name)
    
    return _singleton_default_namespace | namespace | updates
    
    


class SingletonRegistry(dict):
    "Objects in this dictionary are registered using a keygetter (cls._getkey := get_name) using the .register() method.  Regular dict methods still work, but unless a key is made via keygetter(valur), its value will not be recognized by methods like .is_member() or .has_member(), etc.  Additionally, equivalence for members is defined by identity rather than .__eq__() or .__hash__() checks."
#    def __init__(self, ǀ·ᴅᴀᴛᴀ·ǀ=(), ǀ·keygetter·ǀ: Callable=str, ǀ·match·ǀ: Callable=is_, /, **kwargs):
#        super().__init__(ǀ·ᴅᴀᴛᴀ·ǀ, **kwargs)
#        self.keygetter = ǀ·keygetter·ǀ
#        self.match = ǀ·match·ǀ
    __slots__ = ("_doc", )
    def get_doc(self):
        try:  return self._doc
        except AttributeError:  return None
    def set_doc(self, doc: str=None):
        if (doc is not None) and (type(doc) is not str):
            doc = str(doc)
        try:
            current = self._doc
        except AttributeError:  pass
        else:
            if (current is not None):  raise AttributeError("attribute already set")
        return object.__setattr__(self, '_doc', doc)
    __doc__: str = property(get_doc, set_doc)
    
    
    @staticmethod
    def _getkey(instance: object) -> str:
        "Returns a consistent dictionary key under which ʽinstanceʼ would be registered in self.  Defined to be  _getkey(Value) := (get_name(Value) if callable(Value) else str(Value),  but can be customized without issue as long as the returned object is a str (or at least hashable) and adequately identifies the instance."
        return (get_name(instance) if callable(instance) else str(instance))
    
    def __new__(cls):  return singleton_registry
    def __repr__(cls):  return "singleton_registry"
    
    def get_decorator(self, safe: bool=True):
        return partial(self.register, safe=bool(safe), fetch=True)
    
    def register(self, instance=None, /, safe: bool=True, fetch: bool=None): #, suppress=False):
        "Register instance as a singleton.  If 'fetch' is set to true, the registered instance is returned, otherwise None.  If an existing instance has been registered (according to self[self._getkey(instance)] = instance), if 'safe' is true, a LookupError is raised unless 'fetch' is also true, in which case the existing instance is returned, and the input instance will be discarded without saying which is which.  If not 'safe', any existing instance will be replaced."
        if (instance is None):
            fetch = True if (fetch is None) else bool(fetch)
            return partial(self.register, safe=bool(safe), fetch=fetch)
        if not safe:
            self[self._getkey(instance)] = instance
            return (instance if fetch else None)
        #else: 
        key = self._getkey(instance)
        try:
            existing = self[key]
        except KeyError:
            self[key] = instance
            if fetch:  return instance
        else:
            if fetch:  return existing
            raise LookupError(f"singleton {key!r} already exists ({type(existing)!r} instance)")
    def _designate(self, instance):
        "Same as reg.register(instance, safe=False)"
        self[self._getkey(instance)] = instance
    
    def registers(self, *instances, safe=True, fetch=True):
        "Iterated register method."
        if fetch:  return list(self._registers(instances, safe))
        if not safe:
            for _ in map(self._designate, instances):  continue
            return
        _getkey = self._getkey
        for instance in instances:
            key = _getkey(instance)
            try:
                existing = self[key]
            except KeyError:
                self[key] = instance
            else:
                raise LookupError(f"singleton {key!r} already exists ({type(existing)!r} instance)")
    def _registers(self, instances, safe):
        "Iterator for registers method."
        if not safe:
            yield from map(self._designate, instances)
            return
        for instance in instances:
            key = self._getkey(instance)
            try:
                existing = self[key]
            except KeyError:
                self[key] = instance
                yield instance
            else:  yield existing
    
    def is_member(self, instance, /, thorough=False):
        "Checks whether an instance is contained in the registry's values.  If thorough, checks also for the behavior:  type(instance)() is instance  common for singleton objects.  This distinguishes ningletons like True and False from true singletons."
        key = self._getkey(instance)
        if thorough:
            try:
                isit = (self[key] is instance)
            except KeyError:  return False
            else:  return isit and (type(instance)() is instance)
        try:  return (self[key] is instance)
        except KeyError:  return False
    
    def has_member(self, instance_or_key, /, thorough=False):
        "Note that if the input is the instance's string or name (the key), thorough=True will always return False."
        key = self._getkey(instance_or_key)
        if not thorough:  return super().__contains__(key)
        try:  return (self[key] is instance_or_key)
        except KeyError:  return False
    
    def has_members_all(self, *instances_or_keys, thorough=False):
        return all(self.has_member(x, thorough=thorough) for x in instances_or_keys)
    def has_members_any(self, *instances_or_keys, thorough=False):
        return any(self.has_member(x, thorough=thorough) for x in instances_or_keys)
    
    def get_member(self, instance_or_key, /, default=None):
        "Similar to dict.get(), except that if the input instance_or_key is an instance, self[self._getkey(instance_or_key)] will be returned.  Good for replacing duplicates."
        try:  return self[self._getkey(instance_or_key)]
        except KeyError:  return default
    
    def get_members(self, *instances_or_keys, default=None):
        try:
            default = cycle(iter(default))
        except TypeError:
            default = repeat(default)
        return list(map(self.get_member, instances_or_keys, default))





singleton_registry: SingletonRegistry \
        = sys.modules.get("_ꜱɪɴɢʟᴇᴛᴏɴ_ᴄᴀᴄʜᴇ", None)
if singleton_registry is None:
    singleton_registry: SingletonRegistry \
        = sys.modules.setdefault("_ꜱɪɴɢʟᴇᴛᴏɴ_ᴄᴀᴄʜᴇ", 
        dict.__new__(SingletonRegistry, 
            {
                repr(...): ..., 
                "None": None, 
                "NotImplemented": NotImplemented, 
                'False': False, 
                'True': True, 
            }))
    
    register_singleton = singleton_registry.register
    is_singleton = singleton_registry.is_member
    register_singleton(singleton_registry)
    register_singleton(DefaultObject)
    
else:
    register_singleton = singleton_registry.register
    is_singleton = singleton_registry.is_member


"  ________________  Constfunc  Constructor  &  Common  Constfuncs  ________________  "

def _template(_=...):  return 0
def g_constfunc(constval: object, *, as_singleton=True, overwrite=False):
    "Memoized factory for producing functions of the form:  f(x)→constval.  If ʽas_singletonʼ, the constfunc will be registered in the singleton_registry object."
    key = constval, type(constval)
    try:
        _cf = _g_constfunc_mem[key]
    except KeyError:  pass
    else:
        if as_singleton:
            _cf = singleton_registry.register(_cf, safe=(not overwrite), fetch=True)
            _g_constfunc_mem[key] = _cf
            return _cf
    
    constval_str = get_name_or_str(constval, reprf='ʽʽ{0}ˮ'.format)
    name = f"const_{constval_str}"
    qualname = 'g_constfunc.<locals>.' + name
    doc = f"Always returns {constval_str}."
    if isinstance(constval, (bool, int, float, complex, str, bytes, frozenset)) \
    or not (... is not constval is not None):
        _cf = function(\
                        code=_template.__code__.replace(
                                co_name=name, co_qualname=qualname, 
                                co_consts=(doc, constval)), 
                        globals=globals(), name=name, 
                        argdefs=(...,), closure=None, kwdefaults={'_': ...})
    else:
        def _cf(_=...):  return constval
        _cf.__name__ = name
        _cf.__qualname__ = qualname
        _cf.__doc__ = doc
        _cf.__code__ = _cf.__code__.replace(co_name=name, co_qualname=qualname, co_consts=(doc,))
    
    _g_constfunc_mem[key] = _cf
    
    if as_singleton:
        _cf = singleton_registry.register(_cf, safe=(not overwrite), fetch=True)
    
    return _cf
_g_constfunc_mem = {}


def constfuncs_all():
    "Get a list of all functions created by the “g_constfunc” factory."
    return list(_g_constfunc_mem.values())


const_False = g_constfunc(False)
const_True = g_constfunc(True)
const_None = g_constfunc(None)
const_0 = g_constfunc(0)
const_1 = g_constfunc(1)
const_inf = g_constfunc(float('inf'))
const_nan = g_constfunc(float('nan'))


'''
#@#@#@#@#@#@#

import regex as rex, operator
_wordsplit = method(rex.split, rex.compile(r"\b"))
with open(__file__, 'r') as rf:
    filedata = rf.read()
filedata = filedata.rsplit("#@#@#@#@#@#@#", 1)[0]
filedata_wordsplitted = _wordsplit(filedata)

wordpool = _globs
wordcounts = [(k, filedata_wordsplitted.count(k)) for k in wordpool]
wordcounts = dict(sorted(wordcounts, key=operator.itemgetter(1)))
print(*wordcounts.items(), sep="\n")
'''



'''
       ᴵ ᵏⁿᵉʷ ᵃ ᵐᵃⁿ ʷʰᵒ ʰᵘⁿᵍ ᵈʳʸʷᵃˡˡ, ʰᵉ ʰᵘⁿᵍ ⁱᵗ ᵐⁱᵍʰᵗʸ ᕐᵘⁱᶜᵏ,
     ᴬ ᵗʳⁱᵖ ᵒʳ ᵗʷᵒ ᵗᵒ ᵗʰᵃᵗ ᵇˡᵘᵉ ʳᵒᵒᵐ ʷᵒᵘˡᵈ ʰᵉˡᵖ ʰⁱᵐ ᵈᵒ ᵗʰᵉ ᵗʳⁱᶜᵏ,
    ᴴⁱˢ ᶠᵒʳᵉᵐᵃⁿ ᵖᵃᵗ ʰⁱᵐ ᵒⁿ ᵗʰᵉ ᵇᵃᶜᵏ ʷʰᵉⁿᵉᵛᵉʳ ʰᵉ ʷᵒᵘˡᵈ ᶜᵒᵐᵉ ᵃʳᵒᵘⁿᵈ,
              ’ᶜᵃᵘˢᵉ ᵗʰᵒˢᵉ ᵈᵃᵐⁿᵉᵈ ᵇˡᵘᵉ⁻ᶜᵒˡˡᵃʳ ᵗʷᵉᵉᵏᵉʳˢ,
                    ᵀʰᵉʸ’ʳᵉ ᵇᵉˡᵒᵛᵉᵈ ⁱⁿ ᵗʰⁱˢ ᵗᵒʷⁿᐧ
'''


#    #    #    #    #    #    #    #    #    #    #    #    #
#     GET    TEXT    SIGNATURE    &    NIN     #
#    #    #    #    #    #    #    #    #    #    #    #    #

from regex import compile as rex_compile

def _get_txtsig_from_doc(f):
    fdoc = f.__doc__
    fnam = getattr(f, '__name__', None) or type(f).__name__
    if (fdoc is None):  raise AttributeError("Couldn’t derive text_signature")
    if (not fdoc.startswith(fnam)):
        _fdoc = fdoc.split(".", 1)[1]
        if _fdoc.startswith(fnam):
            fdoc = _fdoc
        else:  raise ValueError(fdoc)
    return fdoc.splitlines()[0].removeprefix(fnam).rsplit(')', 1)[0] + ')'

def get_txtsig(f, errors="ignore"):
    txtsig = getattr(f, '__text_signature__', None)
    if (txtsig is not None):  return txtsig
    try:  return _get_txtsig_from_doc(f)
    except Exception:
        if (get_name(f) == '__new__') \
        or isinstance(f, type):  return '($m, /)'
        if errors == "raise":  raise

_txsg_rst = r"^\(\$[\w]+, |[\W--=]+"
_txsg_splitter = rex_compile(_txsg_rst)
def _get_nin_from_txtsig(f):
    txtsig = f if (type(f) is str) else get_txtsig(f)
    if (txtsig is None):
        if (get_name(f) == '__new__'):
            txtsig = '($m, /)'
        if isinstance(f, type):  return get_nin(f.__new__)
        raise AttributeError("Cannot find any kind of ‘arity’ for this object, nor any way to deduce it.")
    txtsig = f'{txtsig}'
    has_varargs = bool(txtsig.count('*') % 2) and ('*,' not in txtsig)
    if has_varargs:
        txtsig = txtsig[:txtsig.index("*")]
    nin = len(list(filter(None, _txsg_splitter.split(txtsig.replace('=', '')))))
    return nin, has_varargs
def _get_nin_from_codeobject(fco: CodeType):
    has_varargs = bool(fco.co_flags & CO_VARARGS)
    return fco.co_argcount, has_varargs
def _get_nin_from_argspec(fullargspec: type(getfullargspec(lambda: None))):
    has_varargs = (fullargspec.varkw is not None)
    nin = len(fullargspec.args)
    return nin, has_varargs

def get_nin(f):
    try:  return get_nin._mem[f]
    except KeyError:
        get_nin._mem[f] = nin = _get_nin(f)
        return nin
def _get_nin(f):
    fco = get_code(f)
    if (type(fco) is CodeType):  return _get_nin_from_codeobject(fco)
    try:  return _get_nin_from_txtsig(f)
    except Exception:  pass
    try:
        fullargspec = getfullargspec(f)
    except TypeError:  return (0, None)
    else:  return _get_arity_from_argspec(fullargspec)
get_nin._mem = {}


