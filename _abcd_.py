
import sys
from _weakrefset import WeakSet
import weakref
from itertools import repeat


__doc__ = "This module hijacks ABCDMeta from _py_abc and replaces many of its methods to be compatible with setlike-/lattice-ops, making abstract types defined in numbers and collections.abc usable as domain objects in symbolic computation.  Downstream packages are just duplicates of the above packages, with the final import package, _mathdomains_abcd_.py, compiling the more mathematically relevant ABCD’s and renaming them to avoid name collisions.  This is 100% free to use however you wish, but check python’s documentation before running of with the stuff I stole from them."'''
How to use:
    • Paste the folder wherever you import from, import from "[...].abcd._mathdomains_abcd_" the ABCD’s you need (duplicates of all the familiar ABC’s are included for convenience.  Be vigilant about name collisions).
    • Create compound types using lattice (&, |, -) operators
    • Check sub/superclass using cmp (<, >, <=, >=) operators
    • Check instance using contains ( in , not in ) keywords
Before injecting into your own projects, might be a good idea to correct any of my blunders.  Any hashed-out test lines were left in because I thought they might be useful.  I also used some unicode symbols that look like punctuation, which shouldn’t be an issue for more up-to-date versions of python, but should be easy enough to fix if they give you trouble.

Domains I added:
    Auto
    Object
    Oblivion
    NonFinite
    Type
    Lattice
    Bool
    Natural
    Stringlike
    Vector
'''


__all__ = ["DomainType", "get_name", "get_nameᐩ"]
def g_modulefuncfuncs(_all_: list):
    ǁ_ᴀʟʟ_ǁ = _all_
    def modulefunc(member: str):
        name = get_name(member)
        (name in  ǁ_ᴀʟʟ_ǁ) or ǁ_ᴀʟʟ_ǁ.append(name)
        return member
    def modulefuncs(*members: str):
        if (len(members) == 1):
            members = members[0]
        names = map(get_name,  members)
        ǁ_ᴀʟʟ_ǁ.extend(names)
        return members
    return modulefunc, modulefuncs

modulefunc, modulefuncs = g_modulefuncfuncs(__all__)


" (-(#)  (–(##)    (—(####)        (    This & That    )        (####)—)    (##)–)  (#)-) "

_mro_len = None


def get_name(ob, /, default: type=str):
    try:  return ob.__name__
    except AttributeError:  pass
    try:  return ob.name
    except AttributeError:  return default(ob) if callable(default) else default
def get_nameᐩ(ob, /, default: type=str):
    name = get_name(ob, default=default)
    return (name if name.isidentifier() else f"({name})")

function, method = modulefuncs(*map(type, type("C", (), {"m": (lambda x: (type(x).m, x.m))})().m()))

 
_GenericAlias = type(tuple[int])
TypeUnion = type(tuple|int)

modulefuncs("_GenericAlias", "TypeUnion")


@modulefunc
def _check_methods(C, *methods):
    "(stolen)"
    mro = C.__mro__
    for method in methods:
        for B in mro:
            try:
                if (B.__dict__[method] is None):  return NotImplemented
            except KeyError:  continue
            else:  break
        else:  return NotImplemented
    return True


@modulefunc
def get_cache_token():
    "(stolen)"
    """Returns the current ABC cache token.

    The token is an opaque object (supporting equality testing) identifying the
    current version of the ABC cache for virtual subclasses. The token changes
    with every call to ``register()`` on any ABC.
    """
    return ABCDMeta._abc_invalidation_counter



" (-(#)  (–(##)    (—(####)        (    AbstractMethod    )        (####)—)    (##)–)  (#)-) "

@modulefunc
def abstractmethod(funcobj):
    "(stolen)"
    """A decorator indicating abstract methods.
    Requires that the metaclass is ABCDMeta or derived from it.  A
    class that has a metaclass derived from ABCDMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.
    Usage:
        class C(metaclass=ABCDMeta):
            @abstractmethod
            def my_abstract_method(self, arg1, arg2, argN):
                ...
    """
    funcobj.__isabstractmethod__ = True
    return funcobj



@modulefunc
def update_abstractmethods(cls):
    "(stolen)"
    """Recalculate the set of abstract methods of an abstract class.
        If a class has had one of its abstract methods implemented after the
    class was created, the method will not be considered implemented until
    this function is called. Alternatively, if a new abstract method has been
    added to the class, it will only be considered an abstract method of the
    class after this function is called.
        This function should be called before any use is made of the class,
    usually in class decorators that add methods to the subject class.
        Returns cls, to allow usage as a class decorator.
        If cls is not an instance of ABCDMeta, does nothing.
    """
    if not hasattr(cls, '__abstractmethods__'):
        # We check for __abstractmethods__ here because cls might by a C
        # implementation or a python implementation (especially during
        # testing), and we want to handle both cases.
        return cls
    
    abstracts = set()
    # Check the existing abstract methods of the parents, keep only the ones
    # that are not implemented.
    for scls in cls.__bases__:
        for name in getattr(scls, '__abstractmethods__', ()):
            value = getattr(cls, name, None)
            if getattr(value, "__isabstractmethod__", False):
                abstracts.add(name)
    # Also add any other newly added abstract methods.
    for name, value in cls.__dict__.items():
        if getattr(value, "__isabstractmethod__", False):
            abstracts.add(name)
    cls.__abstractmethods__ = frozenset(abstracts)
    return cls




" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
"(-( (–( (—(# # ##  ###   #####     ########        ABCDMeta        ########      #####   ###  ## # #)—) )–) )-)"
" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "




ꓽtypeꓸ__new__ = type.__new__
modulefunc("ꓽtypeꓸ__new__")

@modulefunc
class ABCDMeta(type):
    "(stolen; updated)\n"\
    """Metaclass for defining Abstract Base Classes (ABCDs).
    Use this metaclass to create an ABC.  An ABC can be subclassed
    directly, and then acts as a mix-in class.  You can also register
    unrelated concrete classes (even built-in classes) and unrelated
    ABCs as 'virtual subclasses' -- these and their descendants will
    be considered subclasses of the registering ABC by the built-in
    issubclass() function, but the registering ABC won't show up in
    their MRO (Method Resolution Order) nor will method
    implementations defined by the registering ABC be callable (not
    even via super()).
    """
    
    # A global counter that is incremented each time a class is
    # registered as a virtual subclass of anything.  It forces the
    # negative cache to be cleared before its next use.
    # Note: this counter is private. Use `abc.get_cache_token()` for
    #       external code.
    
    __module__ = "abcd"
    
    _ᱻɪꜱɪɴᴠᱻ: bool = False
    _opjoin: type = None
    
    _abc_invalidation_counter: int = 0
    _instances: dict[tuple, frozenset] = {}
    def __new__(metacls, name: str, bases: tuple, namespace: dict, *, _ɪᴅ_ᴋᴇʏ: tuple=None, **kwargs):
        #print(f"    ::ɴᴇᴡ:: {metacls.__name__}({name!r}, {bases}, {namespace}, \n        **{kwargs})")
        namespace = dict(namespace)
        namespace["ᱻɪꜱɪɴᴠᱻ"] \
                = ᱻɪꜱɪɴᴠᱻ = bool(kwargs.pop("ᱻɪꜱɪɴᴠᱻ", namespace.get("ᱻɪꜱɪɴᴠᱻ", metacls._ᱻɪꜱɪɴᴠᱻ)))
        key = (metacls.__name__, name, bases, frozenset(namespace), ᱻɪꜱɪɴᴠᱻ) \
                if (_ɪᴅ_ᴋᴇʏ is None) else _ɪᴅ_ᴋᴇʏ
        try:  return metacls._instances[key]
        except KeyError:  pass
        cls = ꓽtypeꓸ__new__(metacls, name, bases, namespace, **kwargs)
        del cls.__module__
        # Compute set of abstract method names
        abstracts = {name
                     for name, value in namespace.items()
                     if getattr(value, "__isabstractmethod__", False)}
        for base in bases:
            for name in getattr(base, "__abstractmethods__", set()):
                value = getattr(cls, name, None)
                if getattr(value, "__isabstractmethod__", False):
                    abstracts.add(name)
        try:
            del cls.__abstractmethods__
        except AttributeError:  pass
        cls.__abstractmethods__ = frozenset(abstracts)
        # Set up inheritance registry
        setattr(cls, "_abc_registry", set())
        setattr(cls, "_abc_cache", WeakSet())
        setattr(cls, "_abc_negative_cache", WeakSet())
        setattr(cls, "_abc_negative_cache_version", ABCDMeta._abc_invalidation_counter)
        setattr(cls, "_abc_backregistry", set())
        
        metacls._instances[key] = cls
        return cls
    
    def __str__(self):  return self.__name__
    __repr__ = __str__
    __hash__ = type.__hash__
    
    def register(cls, subclass):
        """Register a virtual subclass of an ABC.
        Returns the subclass, to allow usage as a class decorator.
        """
        if not isinstance(subclass, type):
            raise TypeError("Can only register classes")
        if issubclass(subclass, cls):
            return subclass  # Already a subclass
        # Subtle: test for cycles *after* testing for "already a subclass";
        # this means we allow X.register(X) and interpret it as a no-op.
        if issubclass(cls, subclass):
            # This would create a cycle, which is bad for the algorithm below
            raise RuntimeError("Refusing to create an inheritance cycle")
        cls._abc_registry.add(subclass)
        ABCDMeta._abc_invalidation_counter += 1  # Invalidate negative cache
        if isinstance(subclass, ABCDMeta):
            subclass._abc_backregistry.add(cls)
        #print(f"\n{cls = }            {subclass = }\n{cls._abc_registry = }\n{cls._abc_backregistry = }")
        return subclass
    
    def _dump_registry(cls, file=None):
        """Debug helper to print the ABC registry."""
        print(f"Class: {cls.__module__}.{cls.__qualname__}", file=file)
        print(f"Inv. counter: {get_cache_token()}", file=file)
        for name in cls.__dict__:
            if name.startswith("_abc_"):
                value = getattr(cls, name)
                if isinstance(value, WeakSet):
                    value = set(value)
                print(f"{name}: {value!r}", file=file)
    
    def _abc_registry_clear(cls):
        """Clear the registry (for debugging or testing)."""
        cls._abc_registry.clear()
        cls._abc_backregistry.clear()
    
    def _abc_caches_clear(cls):
        """Clear the caches (for debugging or testing)."""
        cls._abc_cache.clear()
        cls._abc_negative_cache.clear()
    
    def __instancecheck__(cls, instance):
        """Override for isinstance(instance, cls)."""
        #print(f"__instancecheck__{(cls, instance)}:")
        #print("# Inline the cache checking")
        subclass = instance.__class__
        if (subclass is bool) and issubclass(cls, Number):  return False
        if subclass in cls._abc_cache:  return True
        subtype = type(instance)
        if subtype is subclass:
            if (cls._abc_negative_cache_version == ABCDMeta._abc_invalidation_counter) \
                and (subclass in cls._abc_negative_cache):  return False
            #print=("# Fall back to the subclass check.")
            return ABCDMeta.__subclasscheck__(cls, subclass) #or cls.__subclasscheck__(subclass)
        return (cls.__subclasscheck__(subclass) or cls.__subclasscheck__(subtype))
    
    def __subclasscheck__(cls, subclass):
        """Override for issubclass(subclass, cls)."""
        #print(f"__subclasscheck__{(cls, subclass)}:")
        if not isinstance(subclass, TypeDescriptorTypes):
            raise TypeError('issubclass() arg 1 must be a class or alias')
        if (not isinstance(subclass, type)):
            if isinstance(subclass, TypeUnion):
                return any(map(cls.__subclasscheck__, subclass.__args__)) #and "(true)0"
        if (subclass is bool) and issubclass(cls, Number):  return False
        #print("# Check cache")
        if subclass in cls._abc_cache:
            return True #and "(true)1"
        #print("# Check negative cache; may have to invalidate")
        if cls._abc_negative_cache_version < ABCDMeta._abc_invalidation_counter:
            #print("# Invalidate the negative cache")
            cls._abc_negative_cache = WeakSet()
            cls._abc_negative_cache_version = ABCDMeta._abc_invalidation_counter
        elif subclass in cls._abc_negative_cache:  return False
        #print("# Check the subclass hook")
        ok = cls.__subclasshook__(subclass)
        if ok is not NotImplemented:
            assert isinstance(ok, bool)
            if ok:
                cls._abc_cache.add(subclass)
            else:
                cls._abc_negative_cache.add(subclass)
            return ok #and "(true)2"
        #print("# Check if it's a direct subclass")
        if cls in getattr(subclass, '__mro__', ()):
            cls._abc_cache.add(subclass)
            return True #and "(true)3"
        #print("# Check if it's a subclass of a registered class (recursive)")
        for rcls in cls._abc_registry:
            if issubclass(subclass, rcls):
                cls._abc_cache.add(subclass)
                return True #and "(true)4"
        #print("# Check if it's a subclass of a subclass (recursive)")
        for scls in cls.__subclasses__():
            if typecheck_issubclass(subclass, scls):
                cls._abc_cache.add(subclass)
                return True #and "(true)5"
        #print("# No dice; update negative cache")
        cls._abc_negative_cache.add(subclass)
        return False
    
    def __subclasses__(cls):
        subclasses = type.__subclasses__(cls)
        #return subclasses
        try:  return (subclasses + list(cls._abc_registry))
        except AttributeError:  return subclasses
    
    def mro(cls):
       superclasses = type.mro(cls)
       try:
           virtual_bases = cls._abc_backregistry
       except AttributeError:  pass
       else:
           superclasses.extend(virtual_bases)
       return superclasses
   
    def __lt__(self, other):
        isinv = self.ᱻɪꜱɪɴᴠᱻ
        if (self == other):  return False
        if (other is Auto):  return False
        if isinstance(other, TypeDescriptorTypes):  return typecheck_issubclass(self, other, strict=True)
        else:  return NotImplemented
    def __gt__(self, other):
        isinv = self.ᱻɪꜱɪɴᴠᱻ
        if (self == other):  return False
        if (other is Auto):  return False
        if isinstance(other, TypeDescriptorTypes):  return typecheck_issubclass(other, self, strict=True)
        else:  return NotImplemented
    def __le__(self, other):
        isinv = self.ᱻɪꜱɪɴᴠᱻ
        if (self == other):  return True
        if (other is Auto):  return False
        if isinstance(other, TypeDescriptorTypes):  return typecheck_issubclass(self, other, strict=False)
        else:  return NotImplemented
    def __ge__(self, other):
        #print(f">>> {self}.__ge__({other};\n>>>     {(self <= other) = }")
        isinv = self.ᱻɪꜱɪɴᴠᱻ
        if (self == other):  return True
        if (other is Auto):  return False
        if isinstance(other, TypeDescriptorTypes):  return typecheck_issubclass(other, self, strict=False)
        else:  return NotImplemented
    
    _op_ref: dict[str, tuple[type]] = {}
    @classmethod
    def _opref_get(metacls, op: str, *args: tuple[type], fallback: function=None):
        try:  return cls._op_ref[op, *args]
        except KeyError:  pass
        if (fallback is None): return None
        try:  return fallback(op, *args)
        except (ValueError, TypeError):  return fallback
    
    def __contains__(self, other: object):
        try:
            domain = other.domain
        except AttributeError:  pass
        else:
            if (domain <= self):  return True
        return isinstance(other, self)
    
    def complement(self):
        key = " ~", self
        try:  return ABCDMeta._op_ref[key]
        except KeyError:  pass
        try:
            T = ABCDMeta._opjoin(" ~", self)
        except TypeError:
            Meta = type(self)
            name = get_name(self)
            isinv = ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ(self)
            if ᱻɪꜱɪɴᴠᱻ := (not isinv):
                name = f"~{name}" if name.isidentifier() else f"~({name})"
            elif name.startswith("~"):
                name = name.removeprefix("~")
            args = (self,)
            T = (ABCD_InvertedSet if ᱻɪꜱɪɴᴠᱻ else ABCD_UnionSet)(name, (), {"__args__": args}, 
                                        ᱻɪꜱɪɴᴠᱻ=ᱻɪꜱɪɴᴠᱻ, 
                                        _ɪᴅ_ᴋᴇʏ=(" ~", args, ᱻɪꜱɪɴᴠᱻ))
        
        ABCDMeta._op_ref[key] = T
        ABCDMeta._op_ref[" ~", T] = self
        return T
    
    def union(self, other):
        key = "|", self, other
        try:  return ABCDMeta._op_ref[key]
        except KeyError:  pass
        if (self == other):  return self
        args = P, Q = self, other
        T = ABCD_UnionSet(f"{get_nameᐩ(self)}|{get_nameᐩ(other)}",  
                                        (),  {"__args__": args},  
                                        _ɪᴅ_ᴋᴇʏ=("|", args, False), 
                                        )
        ABCDMeta._op_ref[key] = T
        return T
    def intersection(self, other):
        key = "&", self, other
        try:  return ABCDMeta._op_ref[key]
        except KeyError:  pass
        if (self == other):  return self
        args = P, Q = self, other
        T = ABCD_IntersectionSet(f"{get_nameᐩ(self)}&{get_nameᐩ(other)}",  
                                    (),  {"__args__": args},  
                                    _ɪᴅ_ᴋᴇʏ=("&", args, False), )
        ABCDMeta._op_ref[key] = T
        return T
    def difference(self, other):  return (self & ~other)
    def reverse_difference(self, other):  return (~self & otber)
    
    __invert__ = complement
    
    __or__ = __ror__ = union
    __and__ = __rand__ = intersection
    __sub__ = difference
    __rsub__ = reverse_difference
    
    def __class_getitem__(cls, spec):
        if not isinstance(spec, tuple):
            spec = (spec,)
        return GenericAlias(cls, spec)


ABCDMetaꓸmro = ABCDMeta.mro
ABCDMetaꓸ__subclasses__ = ABCDMeta.__subclasses__

@modulefunc
def ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ(T: type):
    try:  return T.ᱻɪꜱɪɴᴠᱻ
    except AttributeError:  return False


" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
"(-( (–( (—(# # ##  ###   #####     ########        Set Structs        ########      #####   ###  ## # #)—) )–) )-)"
" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
 
@modulefunc
class ABCD_UnionSet(ABCDMeta):
    _opsym: str = "|"
    _ᱻɪꜱɪɴᴠᱻ: bool = False
    
    _instances: dict[tuple, frozenset] = {}
    def __new__(metacls, name: str, bases: tuple, namespace: dict, *, ᱻɪꜱɪɴᴠᱻ: bool=None, _ɪᴅ_ᴋᴇʏ: tuple=None, **kwargs):
        if (ᱻɪꜱɪɴᴠᱻ is None):
            ᱻɪꜱɪɴᴠᱻ = metacls._ᱻɪꜱɪɴᴠᱻ
        if ("__args__" not in namespace):
            namespace["__args__"] = ()
        else:
            args = []
            for T in namespace["__args__"]:
                if isinstance(T, ABCD_UnionSet):
                    if (type(T) is ABCD_UnionSet):
                        args.extend(T.__args__)
                        continue
                args.append(T)
            
            namespace["__args__"] = tuple(args)
        key = (metacls._opsym, namespace["__args__"], ᱻɪꜱɪɴᴠᱻ) \
                if (_ɪᴅ_ᴋᴇʏ is None) else _ɪᴅ_ᴋᴇʏ
        return ABCDMeta.__new__(metacls, name, bases, namespace, _ɪᴅ_ᴋᴇʏ=key, **kwargs)
    
    def __subclasscheck__(cls, subclass: type):
        return typecheck_issubclass(subclass, cls.__args__)
    def __instancecheck__(cls, instance: object):
        return typecheck_isinstance(instance, cls.__args__)
    '''
    def __lt__(self, other):
        if isinstance(other, ABCD_UnionSet)
        if any((T < other) for T in self.__args__):  return True
        return ABCDMeta.__lt__(self, other)
    '''
#    def __eq__(self, other):
#        equals = ABCDMeta.__eq__(self, other)
#        if (self._ᱻɪꜱɪɴᴠᱻ):
#            return (equals and ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ(other)) or (~other in self.__args__)
#        return (equals and not ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ(other)) or (other in self.__args__)
#    def __ne__(self, other):  return (not self.__eq__(other))
#    
#    __hash__ = type.__hash__


@modulefunc
class ABCD_InvertedSet(ABCD_UnionSet):
    _opsym: str = " ~"
    _ᱻɪꜱɪɴᴠᱻ: bool = True
    
    _instances: dict[tuple, frozenset] = {}
    
    def __subclasscheck__(cls, subclass: type):
        return (not issubclass(subclass, cls.__args__[0]))
    def __instancecheck__(cls, instance: object):
        return (not isinstance(instance, cls.__args__[0]))
    
#    __hash__ = type.__hash__


@modulefunc
class ABCD_IntersectionSet(ABCD_UnionSet):
    _opsym: str = "&"
    _ᱻɪꜱɪɴᴠᱻ: bool = False
    
    _instances: dict[tuple, frozenset] = {}
    
    def __subclasscheck__(cls, subclass: type):
        return all(typecheck_issubclass(subclass, T) for T in cls.__args__)
    def __instancecheck__(cls, instance: object):
        return all(typecheck_isinstance(instance, T) for T in cls.__args__)
    
#    def __eq__(self, other):
#        equals = ABCDMeta.__eq__(self, other)
#        if (self._ᱻɪꜱɪɴᴠᱻ):  return (equals and ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ(other))
#        return (equals and not ɪꜱᱻɪɴᴠᴇʀᴛᴇᴅᱻ(other))
#    def __ne__(self, other):  return (not self.__eq__(other))
#    
#    __hash__ = type.__hash__


_ABCD_SetStructure_Base = ABCD_UnionSet
modulefunc("_ABCD_SetStructure_Base")


@modulefunc
class GenericAlias(_GenericAlias, 
metaclass=type("GenericAliasMeta", (type,), {"__repr__": (lambda T: T.__name__)})):
    "Caution: imposter."
    def __new__(cls, origin: type, args: tuple[type], /):
        self = _GenericAlias.__new__(cls, origin, args)
        return self
    
    def __repr__(self):
        return f"{get_name(self.__origin__)}[{', '.join(map(get_name, self.__args__))}]"
    
    def __lt__(self, other):
        if (self == other):  return False
        if (other is Auto):  return False
        if isinstance(other, GenericAlias):
            origin_0 = self.__origin__
            args_0 = self.__args__
            if (args_0[-1] is Auto):
                args_0 = (args_0[:-1] + (args_0[0],))
            origin_1 = other.__origin__
            args_1 = other.__args__
            if (args_1[-1] is Auto):
                args_1 = (args_1[:-1] + (args_1[0],))
            #print(f">>> {origin_0}[{args_0}] ¿<? {origin_1}[{args_1}]")
            if (not typecheck_issubclass(origin_0, origin_1)):  return False
            return all(map(typecheck_issubclass, args_0, args_1))
        if isinstance(other, TypeDescriptorTypes):
            origin = self.__origin__
            if (origin == other):  return True
            return typecheck_issubclass(origin, other)
        return None
    def __gt__(self, other):
        if (self == other):  return False
        if (other is Auto):  return True
        if isinstance(other, GenericAlias):
            origin_0 = self.__origin__
            args_0 = self.__args__
            if (args_0[-1] is Auto):
                args_0 = (args_0[:-1] + (args_0[0],))
            origin_1 = other.__origin__
            args_1 = other.__args__
            if (args_1[-1] is Auto):
                args_1 = (args_1[:-1] + (args_1[0],))
            #print(f">>> {origin_0}[{args_0}] ¿>? {origin_1}[{args_1}]")
            if (not typecheck_issubclass(origin_1, origin_0)):  return False
            return all(map(typecheck_issubclass, args_1, args_0))
        if isinstance(other, TypeDescriptorTypes):
            origin = self.__origin__
            if (origin == other):  return False
            return typecheck_issubclass(other, origin)
        return None
    def __le__(self, other):
        if (self == other):  return True
        if (other is Auto):  return False
        if isinstance(other, GenericAlias):
            origin_0 = self.__origin__
            args_0 = self.__args__
            if (args_0[-1] is Auto):
                args_0 = (args_0[:-1] + (args_0[0],))
            origin_1 = other.__origin__
            args_1 = other.__args__
            if (args_1[-1] is Auto):
                args_1 = (args_1[:-1] + (args_1[0],))
            if (not typecheck_issubclass(origin_0, origin_1)):  return False
            return all(map(typecheck_issubclass, args_0, args_1))
        if isinstance(other, TypeDescriptorTypes):
            origin = self.__origin__
            if (origin == other):  return True
            return typecheck_issubclass(origin, other)
        return None
    def __ge__(self, other):
        if (self == other):  return True
        if (other is Auto):  return True
        if isinstance(other, GenericAlias):
            origin_0 = self.__origin__
            args_0 = self.__args__
            if (args_0[-1] is Auto):
                args_0 = (args_0[:-1] + (args_0[0],))
            origin_1 = other.__origin__
            args_1 = other.__args__
            if (args_1[-1] is Auto):
                args_1 = (args_1[:-1] + (args_1[0],))
            if (not typecheck_issubclass(origin_1, origin_0)):  return False
            return all(map(typecheck_issubclass, args_1, args_0))
        if isinstance(other, TypeDescriptorTypes):
            origin = self.__origin__
            if (origin == other):  return False
            return typecheck_issubclass(other, origin)
        return None
    
    __or__ = ABCDMeta.__or__
    __and__ = ABCDMeta.__and__
    __sub__ = ABCDMeta.__sub__
    
    __ror__ = ABCDMeta.__ror__
    __rand__ = ABCDMeta.__rand__
    __rsub__ = ABCDMeta.__rsub__
    
    def __instancecheck__(self, instance: object):
        origintype = self.__origin__
        typeargs = self.__args__
        try:
            check = typecheck_isinstance(instance, origintype)
        except TypeError:  pass
        else:
            if (not check):  return False
        if (... in typeargs):
            typeargs = tuple((x) for x in typeargs if x is not ...)
        if issubclass(origintype, Callable):
            domain = deduce_domain(instance)
            if not (isinstance(domain, GenericAlias) and (domain.__origin__ <= Callable)):
                return False
            return all(map(typecheck_isinstance, domain.__args__, typeargs))
        if issubclass(origintype, Iterable):
            return all(map(typecheck_isinstance, (instance), typeargs))
        return NotImplemented
    
    def __subclasscheck__(self, subcls: object):
        origintype = self.__origin__
        typeargs = self.__args__
        try:
            check = typecheck_issubclass(subcls, origintype)
        except TypeError:  pass
        else:
            if (check is True):  return True
        if (... in typeargs):
            typeargs = tuple((x) for x in typeargs if x is not ...)
        if issubclass(subcls, GenericAlias):
            subcls_origin = subcls.__origin__
            if (not typecheck_issubclass(subcls_origin, origintype)):  return False
            subcls_typeargs = subcls.__args__
            return all(map(typecheck_issubclass, subcls_typeargs, typeargs))
        return NotImplemented


" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "

" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "



"    ( (   (    (( (   (     (    [/↓[/  |    Typage Junk    |  ∖]↓∖]    )     )   ) ))    )   ) )"

TypeDescriptorTypage = (type | ABCDMeta | GenericAlias | TypeUnion)
TypeDescriptorTypes = TypeDescriptorTypage.__args__

TypecheckTypage = (type|TypeUnion|tuple[type|TypeUnion])
TypageCheckTypage = (TypeDescriptorTypage|tuple[TypeDescriptorTypage])

modulefuncs("TypeDescriptorTypage", "TypeDescriptorTypes", "TypecheckTypage", "TypageCheckTypage")

DomainType = TypeDescriptorTypage

" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
"(-( (–( (—(# # ##  ###   #####     ########        ABCDoms        ########      #####   ###  ## # #)—) )–) )-)"
" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
 
@modulefunc
class Auto(metaclass=ABCDMeta):
    "Placeholder domain for return type which is expected to be the same as the calling methodʼs bound object (the .__self__ attribute, or the functionʼs ʽselfʼ parameter).  Totally symbolic; I might add some sub"
    __slots__ = ()
    
    __init_subclass__ = None
    __new__ = None
    __init__ = None
    register = None
    
    def __class_getitem__(cls, spec: int|slice|list):
        if (spec == 0):  return cls
        return GenericAlias(cls, spec)


 
@modulefunc
class Object(metaclass=ABCDMeta):
    "Overarching domain for all objects."  #Calling issubclass(Auto, Object) always returns False."
    __slots__ = ()
    
    @classmethod
    def __instancecheck__(cls, instance):  return True
    @classmethod
    def __subclasscheck__(cls, subclass):  return issubclass(subclass, object)
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Object):  return True
        return NotImplemented

 
@modulefunc
class Oblivion(Object, metaclass=ABCDMeta):
    "The empty domain.  Calling issubclass(cls, Oblivion) always returns False unless cls is Oblivion."
    __slots__ = ()
    
    @classmethod
    def __instancecheck__(cls, instance):  return False
    @classmethod
    def __subclasscheck__(cls, subclass):  return (subclass is Oblivion)
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Oblivion):  return False
        return NotImplemented

ABCDMeta._op_ref[" ~", Object] = Oblivion
ABCDMeta._op_ref[" ~", Oblivion] = Object

 
@modulefunc
class Type(metaclass=ABCDMeta):
    "Abstract domain class for types, because abc&collections donʼt have one."
    __slots__ = ()

Type.register(type)
Type.register(ABCDMeta)



@modulefunc
class NonFinite(metaclass=ABCDMeta):
    "Overarching domain for nonfinite objects."
    __slots__ = ()

 
@modulefunc
class Lattice(Object, metaclass=ABCDMeta):
    "Lattice objects support setlike-ops (~, |, &, ^), and include Sets, Bools, and bitwise Integers."
    __slots__ = ()
    
    def meet(self, other):  pass
    def join(self, other):  pass
    
    @abstractmethod
    def __or__(self, other):  return self.join(other)
    @abstractmethod
    def __and__(self, other):  return self.meet(other)
    
    @abstractmethod
    def __lt__(self, other):  return (self != other) and (self == (self & other))
    @abstractmethod
    def __gt__(self, other):  return (self != other) and (self == (self | other))
    @abstractmethod
    def __le__(self, other):  return (self == (self & other))
    @abstractmethod
    def __ge__(self, other):  return (self == (self | other))
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Lattice):
            return _check_methods(C, "__or__", "__and__")
        return NotImplemented
 
@modulefunc
class Bool(Lattice, metaclass=ABCDMeta):
    "Boolean values represent the truthiness of a predicate."
    __slots__ = ()
    
    @classmethod
    def __instancecheck__(cls, instance):
        if ABCDMeta.__instancecheck__(cls, instance):  return True
        return ((instance is True) or (instance is False))
    @classmethod
    def __subclasscheck__(cls, subclass):  return ABCDMeta.__subclasscheck__(cls, subclass)

 
@modulefunc
class _CallableGenericAlias(GenericAlias):
    "Caution: imposter.\n"\
    """ Represent `Callable[argtypes, resulttype]`.
        This sets ``__args__`` to a tuple containing the flattened ``argtypes``
    followed by ``resulttype``.
        Example: ``Callable[[int, str], float]`` sets ``__args__`` to
    ``(int, str, float)``.
    """
    
    __slots__ = ()
    
    def __new__(cls, origin, args):
        if (origin.__qualname__ == Ⲉƒx.__qualname__) and (origin is not Ⲉƒx):
            origin = Ⲉƒx
        if not (isinstance(args, tuple) and len(args) == 2):  raise TypeError(
                "Callable must be used as Callable[[arg, ...], result].")
        t_args, t_result = args
        if isinstance(t_args, (tuple, list)):
            args = (*t_args, t_result)
        elif not _is_param_expr(t_args):  raise TypeError(f"Expected a list of types, an ellipsis, "
                            f"ParamSpec, or Concatenate. Got {t_args}")
        return super().__new__(cls, origin, args)
    
    def __repr__(self):
        __args__ = self.__args__
        if len(__args__) == 2 and _is_param_expr(__args__[0]):  return super().__repr__()
        return (f'{self.__origin__}'
                f'[[{", ".join(map(get_name, __args__[:-1]))}], '
                f'{get_name(__args__[-1])}]')
    
    def __reduce__(self):
        args = self.__args__
        if not (len(args) == 2 and _is_param_expr(args[0])):
            args = list(args[:-1]), args[-1]
        return _CallableGenericAlias, (Callable, args)
    
    def __getitem__(self, item):
        # Called during TypeVar substitution, returns the custom subclass
        # rather than the default types.GenericAlias object.  Most of the
        # code is copied from typing's _GenericAlias and the builtin
        # types.GenericAlias.
        if not isinstance(item, tuple):
            item = (item,)
    
        new_args = super().__getitem__(item).__args__
    
        # args[0] occurs due to things like Z[[int, str, bool]] from PEP 612
        if not isinstance(new_args[0], (tuple, list)):
            t_result = new_args[-1]
            t_args = new_args[:-1]
            new_args = (t_args, t_result)
        return _CallableGenericAlias(Callable, tuple(new_args))
    
    __lt__ = GenericAlias.__lt__
    __gt__ = GenericAlias.__gt__
    __le__ = GenericAlias.__le__
    __ge__ = GenericAlias.__ge__


@modulefunc
def _is_param_expr(obj):
    "(stolen)"
    """Checks if obj matches either a list of types, ``...``, ``ParamSpec`` or
    ``_ConcatenateGenericAlias`` from typing.py
    """
    if obj is Ellipsis:  return True
    if isinstance(obj, list):  return True
    obj = type(obj)
    names = ('ParamSpec', '_ConcatenateGenericAlias')
    return obj.__module__ == 'typing' and any(obj.__name__ == name for name in names)

@modulefunc
def _type_repr(obj):
    "(stolen)"
    """Return the repr() of an object, special-casing types (internal helper).
        Copied from :mod:`typing` since collections.abc
    shouldn't depend on that module.
    (Keep this roughly in sync with the typing version.)
    """
    if isinstance(obj, type):
        if obj.__module__ == 'builtins':  return obj.__qualname__
        return f'{obj.__module__}.{obj.__qualname__}'
    if obj is Ellipsis:  return '...'
    if isinstance(obj, function):  return obj.__name__
    return repr(obj)
 
@modulefunc
class Callable(Object, metaclass=ABCDMeta):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    def __call__(self, *args, **kwds):  return False
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Callable:
            if (type(C) is _CallableGenericAlias):  return True
            return _check_methods(C, "__call__")
        return NotImplemented
    
    __class_getitem__ = classmethod(_CallableGenericAlias)


#Ⲉƒx = Callable

" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
"(-( (–( (—(# # ##  ###   #####     ########        Collections        ########      #####   ###  ## # #)—) )–) )-)"



"(stolen)"
# Private list of types that we want to register with the various ABCs
# so that they will pass tests like:
#       it = iter(somebytearray)
#       assert isinstance(it, Iterable)
# Note:  in other implementations, these types might not be distinct
# and they may have their own implementation specific types that
# are not included on this list.
bytes_iterator = type(iter(b''))
bytearray_iterator = type(iter(bytearray()))
#callable_iterator = ???
dict_keyiterator = type(iter({}.keys()))
dict_valueiterator = type(iter({}.values()))
dict_itemiterator = type(iter({}.items()))
list_iterator = type(iter([]))
list_reverseiterator = type(iter(reversed([])))
range_iterator = type(iter(range(0)))
longrange_iterator = type(iter(range(1 << 1000)))
set_iterator = type(iter(set()))
str_iterator = type(iter(""))
tuple_iterator = type(iter(()))
zip_iterator = type(iter(zip()))
## views ##
dict_keys = type({}.keys())
dict_values = type({}.values())
dict_items = type({}.items())
## misc ##
mappingproxy = type(type.__dict__)
def _get_framelocalsproxy():
    return type(sys._getframe().f_locals)
FrameLocalsProxy = _get_framelocalsproxy()
del _get_framelocalsproxy
generator = type((lambda: (yield))())
## coroutine ##
async def _coro(): pass
_coro = _coro()
coroutine = type(_coro)
_coro.close()  # Prevent ResourceWarning
del _coro
## asynchronous generator ##
async def _ag(): yield
_ag = _ag()
async_generator = type(_ag)
del _ag

 
@modulefunc
class Hashable(metaclass=ABCDMeta):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    def __hash__(self):  return 0
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Hashable):  return _check_methods(C, "__hash__")
        return NotImplemented
 
@modulefunc
class Awaitable(metaclass=ABCDMeta):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    def __await__(self):  yield
    
    @classmethod
    def __subclasshook__(cls, C):
        if (cls is Awaitable):  return _check_methods(C, "__await__")
        return NotImplemented
    
    __class_getitem__ = classmethod(GenericAlias)
 
@modulefunc
class Coroutine(Awaitable):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    def send(self, value):
        """Send a value into the coroutine.
        Return next yielded value or raise StopIteration."""
        raise StopIteration
    
    @abstractmethod
    def throw(self, typ, val=None, tb=None):
        """Raise an exception in the coroutine.
        Return next yielded value or raise StopIteration."""
        if val is None:
            if tb is None:  raise typ
            val = typ()
        if tb is not None:
            val = val.with_traceback(tb)
        raise val
    
    def close(self):
        """Raise GeneratorExit inside coroutine."""
        try:
            self.throw(GeneratorExit)
        except (GeneratorExit, StopIteration):  pass
        else:  raise RuntimeError("coroutine ignored GeneratorExit")
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Coroutine:  return _check_methods(C, '__await__', 'send', 'throw', 'close')
        return NotImplemented
 
@modulefunc
class AsyncIterable(metaclass=ABCDMeta):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    def __aiter__(self):  return AsyncIterator()
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is AsyncIterable:  return _check_methods(C, "__aiter__")
        return NotImplemented
    
    __class_getitem__ = classmethod(GenericAlias)
 
@modulefunc
class AsyncIterator(AsyncIterable):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    async def __anext__(self):
        """Return the next item or raise StopAsyncIteration when exhausted."""
        raise StopAsyncIteration
    
    def __aiter__(self):  return self
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is AsyncIterator:  return _check_methods(C, "__anext__", "__aiter__")
        return NotImplemented
 
@modulefunc
class AsyncGenerator(AsyncIterator):
    "(stolen)"
    
    __slots__ = ()
    
    async def __anext__(self):
        """Return the next item from the asynchronous generator.
        When exhausted, raise StopAsyncIteration."""
        return await self.asend(None)
    
    @abstractmethod
    async def asend(self, value):
        """Send a value into the asynchronous generator.
        Return next yielded value or raise StopAsyncIteration."""
        raise StopAsyncIteration
    
    @abstractmethod
    async def athrow(self, typ, val=None, tb=None):
        """Raise an exception in the asynchronous generator.
        Return next yielded value or raise StopAsyncIteration."""
        if val is None:
            if tb is None:  raise typ
            val = typ()
        if tb is not None:
            val = val.with_traceback(tb)
        raise val
    
    async def aclose(self):
        """Raise GeneratorExit inside coroutine."""
        try:  await self.athrow(GeneratorExit)
        except (GeneratorExit, StopAsyncIteration):  pass
        else:  raise RuntimeError("asynchronous generator ignored GeneratorExit")
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is not AsyncGenerator:  return NotImplemented
        return _check_methods(C, '__aiter__', '__anext__', 'asend', 'athrow', 'aclose')



@modulefunc
class Iterable(Object, metaclass=ABCDMeta):
    "(stolen)"
    
    __slots__ = ()
    
    @abstractmethod
    def __iter__(self):
        while False:  yield None
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:  return _check_methods(C, "__iter__")
        return NotImplemented
    
    __class_getitem__ = classmethod(GenericAlias)





" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "

" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "


" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
"(-( (–( (—(# # ##  ###   #####     #  Redefine Isinstance & Issubclass  #      #####   ###  ## # #)—) )–) )-)"
" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "

@modulefunc
def deduce_domain(cls: TypeDescriptorTypage, /, *overrides: object):
    try:  return cls.as_domain()
    except AttributeError:  pass
    if (cls in overrides):  return cls
    if (cls is Auto) or (cls is ...):  return Object
    if (get_name(cls) == "Callable"):  return Ⲉƒx
    if isinstance(cls, _ABCD_SetStructure_Base):  return cls
    if isinstance(cls, _CallableGenericAlias):
        if (cls.__origin__ is _collections_abcꓸCallable):
            args = list(map(deduce_domain, cls.__args__))
            cls = _CallableGenericAlias(Ⲉƒx, (args[:-1], args[-1]))
        return cls
    if (not isinstance(cls, TypeDescriptorTypes)):
        cls = type(cls)
        if issubclass(cls, Ⲉƒx):  return deduce_opdomains(cls, as_ⲈƒxGenericAlias=True)
    if (cls in MathDomainTypes):  return cls
    candidates = {dtp for dtp in MathDomainTypes if typecheck_issubclass(cls, dtp)}
    #print(cls, "ᑕ", candidates)
    candidates.remove(ⲈOʙ)
    if (not candidates):  return ⲈOʙ
    return max(candidates, key=lambda T: len(candidates.intersection(ABCDMetaꓸmro(T))))

@modulefunc
def get_annotations(ob):
    try:
        annots = ob.__annotations__
    except AttributeError:
        annots = None
    if (annots is None):  return {'return': object}
    return annots
#    if (annots is None):  return {'return': min(get_domain(ob), get_domain(get_value(ob)))}
#    return {k: as_domain(v) for k, v in annots.items()}

Ⲉƒx = Callable
#modulefunc("Ⲉƒx")

@modulefunc
def _get_opdomains_from_annotations(annots: dict[str,type], order: tuple[str]=None):
    "Returns a tuple of Domain objects from type annotations provided.  Optional "\
    "'argorder' may be provided to control which varnames correspond to which "\
    "indices in the output.  Final 'return' key may be omitted; it will be auto-derived."
    if (order is None):
        order = tuple(annots)
    domains = [deduce_domain(v) for v in map(annots.get, order)]
    if order and (order[-1] != 'return'):
        codom = annots.get('return')
        if (codom is None):
            codom = domains[0] if (len(frozenset(domains)) == 1) else Object
        domains.append(codom)
    return domains

@modulefunc
def deduce_opdomains(func: Callable, *, as_ⲈƒxGenericAlias: bool=True):
    opdomains = list(map(deduce_domain, _get_opdomains_from_annotations(get_annotations(func))))
    if not opdomains:
        opdomains = ((...,), Object)
    if as_ⲈƒxGenericAlias: return _CallableGenericAlias(Ⲉƒx, (opdomains[:-1], opdomains[-1]))
    return (tuple(opdomains[:-1]), opdomains[-1])


@modulefunc
def typecheck_isinstance(instance: object, typage: TypageCheckTypage):
    "Like isinstance(), but compatable with GenericAlias, TypeUnion, etc., as well as type."
    try:  return isinstance(instance, typage)
    except TypeError as exc:
        exc_str = str(exc)
        problem_index = exc_str.find(" arg")
        problem_index = (problem_index != -1) and exc_str[exc_str.index(" ", problem_index+3)+1]
        if (problem_index is False):  raise exc
    
    if isinstance(typage, GenericAlias):
        return _GenericAlias_typage_typecheck(instance, typage, typecheck_isinstance)
    elif isinstance(typage, TypeUnion):
        return any(typecheck_isinstance(instance, T) for T in typage.__args__)
        #raise ValueError(f"TypeUnion should be valid typage for isinstance({instance!r}, {typage!r})")
    elif isinstance(typage, tuple):
        return any(typecheck_isinstance(instance, T) for T in typage)
    
    del exc_str #= subscript(exc_str)
    raise TypeError(vars())


@modulefunc
def typecheck_issubclass(subcls: type, typage: TypageCheckTypage, *, strict: bool=False):
    "Like issubclass(), but compatable with GenericAlias, etc., as well as type.\n"\
    "\n    [Note on TypeUnion instancecheck]:  As would be expected, isinstance(x, (TypeA, ClassB)) is considerably faster than isinstance(x, (TypeA | ClassB))"
    #print(f"    #    ? issubclass({get_name(subcls)},  {get_name(typage)})  ")
    if strict and (subcls == typage):  return False
    try:
        P = issubclass(subcls, typage)
    except TypeError as exc:
        exc_str = str(exc)
        problem_index = exc_str.find(" arg")
        problem_index = (problem_index != -1) and exc_str[exc_str.index(" ", problem_index+3)+1]
        if (problem_index is False):  raise exc
    else:
        #print(f"    #    ? issubclass({get_name(subcls)},  {get_name(typage)})  ")]
        return P
    
    if (typage is Object):  return isinstance(subcls, TypeDescriptorTypes)
    if (subcls is Object):  return (typage is Object)
    if (typage is Auto):  return isinstance(subcls, TypeDescriptorTypes)
    if (subcls is Auto):  return isinstance(subcls, TypeDescriptorTypes)
    
    if (problem_index == '1'):
        #    #    issubclass(~type, TypecheckTypage) ==> '1'    #    #
        #print(f"    #    ? issubclass({(subcls)},  {(typage)})  ")
        if isinstance(subcls, GenericAlias):
            subcls_origin = subcls.__origin__
            subcls_typeargs = subcls.__args__
            #if isinstance(typage, (type, ABCDMeta)):  return typecheck_issubclass(subcls_origin, typage)
            if isinstance(typage, GenericAlias):
                typage_origin = typage.__origin__
                if (not typecheck_issubclass(subcls_origin, typage_origin)):  return False
                typage_typeargs = typage.__args__
                if (... in subcls_typeargs):
                    subcls_typeargs = subcls_typeargs[:subcls_typeargs.index(...)]
                if (... in typage_typeargs):
                    typage_typeargs = typage_typeargs[:typage_typeargs.index(...)]
                if issubclass(typage_origin, Callable):
                    return all(map(typecheck_issubclass, subcls_typeargs, typage_typeargs))
                return (set(subcls_typeargs).issubset(set(typage_typeargs)))
            if isinstance(typage, TypeUnion):
                if (not typecheck_issubclass(subcls_origin, typage)):  return False
                typage_typeargs = typage.__args__
                return any(typecheck_issubclass(T, typage) for T in subcls_typeargs)
            if isinstance(typage, tuple):
                return any(typecheck_issubclass(T, typage) for T in subcls_typeargs)
            return (subcls <= typage)
            return typecheck_issubclass(subcls_origin, typage)
            
        if isinstance(subcls, TypeUnion):
            return all(typecheck_issubclass(T, typage) for T in subcls.__args__)
            
        if isinstance(subcls, tuple):
            return any(typecheck_issubclass(T, typage) for T in subcls)
            
        #    #    issubclass(~type, ~TypecheckTypage)==> '1'    #    #
    elif (problem_index == '2'):
        #    #    issubclass(type, ~TypecheckTypage) ==> '2'    #    #
        if isinstance(typage, TypeUnion):
            return any(typecheck_issubclass(subcls, T) for T in typage.__args__)
        if isinstance(typage, tuple):
            return any(typecheck_issubclass(subcls, T) for T in typage)
    #print(f"    #    ? issubclass({(subcls)},  {(typage)})  ")
    
    del exc_str
    raise TypeError(vars())


@modulefunc
def _GenericAlias_typage_typecheck(instance: object, typage: GenericAlias, typechecker: type(typecheck_issubclass)):
    if (typechecker is typecheck_isinstance):  return GenericAlias.__instancecheck__(typage, instance)
    if (typechecker is typecheck_issubclass):  return GenericAlias.__subclasscheck__(typage, instance)
    return NotImplemented


" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "
" # #  ##   ###     #####        ########             #############             ########        #####     ###   ##  # # "

