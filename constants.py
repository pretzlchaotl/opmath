
import sys
sys.path.append(__file__.rsplit("rhombus", 1)[0])

from rhombus import _ⲉʟⲉᴍⲉɴᴛꜱ_
from rhombus._ⲉʟⲉᴍⲉɴᴛꜱ_ import *
from rhombus import __ᴄꕺʀⲉ__
from rhombus.__ᴄꕺʀⲉ__ import *

__globals__ = (lambda:x).__globals__
__globals__.update(_ⲉʟⲉᴍⲉɴᴛꜱ_.__globals__|__ᴄꕺʀⲉ__.__globals__|globals())

__all__ = [] + _ⲉʟⲉᴍⲉɴᴛꜱ_.__all__
__all__.extend(k for k in __ᴄꕺʀⲉ__.__all__ if k not in __all__)
modulefunc, modulefuncs = g_modulefunc(__all__)


opvalue = opvar


_ꓽ0 = opvar("ꓽ0", value=neutral_zero, domain=ⲈUɴ)
_ꓽᐩ1 = _ꓽ1 = opvar("ᐩ1", value=positive_one, domain=ⲈUɴ)
_ꓽᐨ1 = opvar("ᐨ1", value=negative_one, domain=ⲈUɴ)
_ꓽᐩ1j = opvar("ᐩ1j", value=imaginary_unit, domain=ⲈUɴ)
_ꓽᐨ1j = opvar("ᐨ1j", value=imaginary_unit, domain=ⲈUɴ)
_ꓽᐩꝎ = opvar("ᐩꝎ", value=inf, domain=ⲈUɴ)
_ꓽᐨꝎ = opvar("ᐨꝎ", value=-inf, domain=ⲈUɴ)
_ꓽᐩꝏᐨꞋ = opvar("ᐩꝎ", value=sys.float_info.min, domain=ⲈUɴ)
_ꓽᐨꝏᐨꞋ = opvar("ᐨꝎ", value=-sys.float_info.min, domain=ⲈUɴ)
Infinity = _ꓽᐩꝎ
NegativeInfinity = _ꓽᐨꝎ
Infinitessimal = _ꓽᐩꝏᐨꞋ
NegativeInfinitessimal = _ꓽᐨꝏᐨꞋ

_ꓽɲαɳ = opvar("ꓽɲαɳ", value=nan, domain=ⲈUɴ)
_ꓽꭒɲᶑꬲꝼ = opvar("Undefined", value=Undefined, domain=ⲈXx)



_ꓽƒget_domain = opvar("get_domain", value=get_domain, domain=Ⲉƒx[[ⲈOʙ], ⲈSᴘ])


_ꓽʟⵁ = opvar("ⵁ", value=Bottom, domain=ⲈLᴛ)
_ꓽʟU = opvar("U", value=Top, domain=ⲈLᴛ)
_ꓽBot = _ꓽⵁ = _ꓽʟⵁ[ⲈOʙ]
_ꓽTop = _ꓽU = _ꓽʟU[ⲈOʙ]
_ꓽᴘⵁ = EmptySet = opvar(Oblivion, domain=ⲈSᴘ)
_ꓽᴘU = UniversalSet = opvar(Object, domain=ⲈSᴘ)
_ꓽⲉⵁ = Empty = _ꓽᴘⵁ[ⲈCᴛ]
_ꓽⲉU = Full = _ꓽᴘU[ⲈCᴛ]
_ꓽF = opvar("False", value=False, domain=Ⲉǃǃ)
_ꓽT = opvar("True", value=True, domain=Ⲉǃǃ)
_ꓽᴘⵁ.set_base_key(_ꓽⵁ)
_ꓽᴘU.set_base_key(_ꓽU)
_ꓽF.set_base_key(_ꓽⵁ)
_ꓽT.set_base_key(_ꓽU)

#assert (_ꓽʟⵁ.domain is ⲈLᴛ)
#assert (_ꓽʟU.domain is ⲈLᴛ)
#assert (_ꓽⵁ.domain is ⲈOʙ), _ꓽⵁ.domain
#assert (_ꓽU.domain is ⲈOʙ)
#assert (_ꓽᴘⵁ.domain is ⲈSᴘ)
#assert (_ꓽᴘU.domain is ⲈSᴘ)
#assert (_ꓽⲉⵁ.domain is ⲈCᴛ)
#assert (_ꓽⲉU.domain is ⲈCᴛ)
#assert (_ꓽF.domain is Ⲉǃǃ)
#assert (_ꓽT.domain is Ⲉǃǃ)


constvars_ref = {k: eval(k) for k in (
        "_ꓽ0", "_ꓽ1", "_ꓽᐩ1", "_ꓽᐨ1", "_ꓽᐩ1j", "_ꓽᐨ1j", 
        "_ꓽᐩꝎ", "_ꓽᐨꝎ", "_ꓽᐩꝏᐨꞋ", "_ꓽᐨꝏᐨꞋ", 
        "Infinity", "NegativeInfinity", "Infinitessimal", "NegativeInfinitessimal", 
        "_ꓽɲαɳ", "_ꓽꭒɲᶑꬲꝼ", 
    ) + (
        "_ꓽƒget_domain", 
        "_ꓽBot", "_ꓽTop", "_ꓽⵁ", "_ꓽU", 
        "_ꓽʟⵁ", "_ꓽʟU", 
        "_ꓽF", "_ꓽT", 
        "_ꓽᴘⵁ", "_ꓽᴘU", 
        "EmptySet", "UniversalSet", 
        "_ꓽⲉⵁ", "_ꓽⲉU", 
        "Empty", "Full", 
    )
}


modulefuncs("constvars_ref", *constvars_ref)

#print("Constvars:    {", *("%r: %s" % (k, [v, v.value, v.domain]) \
#    for k,v in constvars_ref.items()), "}", sep=", \n    ")




def _test_cmp():
    
    ꓽᴀ, ꓽʙ, ꓽᴄ = varlist = list(map(opvar, "ᴀʙᴄ"))
    varlistⲈUɴ = [v[ⲈUɴ] for v in varlist]
    varlistⲈLᴛ = [v[ⲈLᴛ] for v in varlist]
    
    
    rghtdom = ('', Oblivion, Object,
                        '', 1, 0, -1, 
                        '', frozenset(), frozenset({()}), 
                        '', False, True, 
                        '', None, ..., 
                        '', *varlistⲈLᴛ, 
                        '', *varlistⲈUɴ, 
                        '')
    for Q in rghtdom:
        print()
        if (Q == ''):  continue
        for P in (_ꓽBot, _ꓽTop):
            for op in map(opfunc, "< > <= >=".split()):
                PⲷQ = f"({P} {op} {Q})"
                ⲷᑕPQᑐ = str(op.func(P, Q))
                print(f"{PⲷQ: >16} = {ⲷᑕPQᑐ: <16}")



if __name__ == "__main__":
    
    print("\n\n\n")
    
    _test_cmp()
    
    print("\n\n")
    exit()

