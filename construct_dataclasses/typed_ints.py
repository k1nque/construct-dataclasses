from __future__ import annotations

import typing as t

import construct as cs
from construct.core import ContextKWType

T_co = t.TypeVar("T_co", covariant=True)


class ConstructProto(t.Protocol[T_co]):
    def parse(self, data: bytes, **contextkw: ContextKWType) -> T_co: ...
    def build(self, obj: T_co, **contextkw: ContextKWType) -> bytes: ...


_IntConstruct = ConstructProto[int]

Int_T: _IntConstruct = t.cast(_IntConstruct, cs.Int)
Int8ub_T: _IntConstruct = t.cast(_IntConstruct, cs.Int8ub)
Int8ul_T: _IntConstruct = t.cast(_IntConstruct, cs.Int8ul)
Int8sb_T: _IntConstruct = t.cast(_IntConstruct, cs.Int8sb)
Int8sl_T: _IntConstruct = t.cast(_IntConstruct, cs.Int8sl)
Int8un_T: _IntConstruct = t.cast(_IntConstruct, cs.Int8un)
Int8sn_T: _IntConstruct = t.cast(_IntConstruct, cs.Int8sn)

Int16ub_T: _IntConstruct = t.cast(_IntConstruct, cs.Int16ub)
Int16ul_T: _IntConstruct = t.cast(_IntConstruct, cs.Int16ul)
Int16sb_T: _IntConstruct = t.cast(_IntConstruct, cs.Int16sb)
Int16sl_T: _IntConstruct = t.cast(_IntConstruct, cs.Int16sl)
Int16un_T: _IntConstruct = t.cast(_IntConstruct, cs.Int16un)
Int16sn_T: _IntConstruct = t.cast(_IntConstruct, cs.Int16sn)

Int24ub_T: _IntConstruct = t.cast(_IntConstruct, cs.Int24ub)
Int24ul_T: _IntConstruct = t.cast(_IntConstruct, cs.Int24ul)
Int24sb_T: _IntConstruct = t.cast(_IntConstruct, cs.Int24sb)
Int24sl_T: _IntConstruct = t.cast(_IntConstruct, cs.Int24sl)
Int24un_T: _IntConstruct = t.cast(_IntConstruct, cs.Int24un)
Int24sn_T: _IntConstruct = t.cast(_IntConstruct, cs.Int24sn)

Int32ub_T: _IntConstruct = t.cast(_IntConstruct, cs.Int32ub)
Int32ul_T: _IntConstruct = t.cast(_IntConstruct, cs.Int32ul)
Int32sb_T: _IntConstruct = t.cast(_IntConstruct, cs.Int32sb)
Int32sl_T: _IntConstruct = t.cast(_IntConstruct, cs.Int32sl)
Int32un_T: _IntConstruct = t.cast(_IntConstruct, cs.Int32un)
Int32sn_T: _IntConstruct = t.cast(_IntConstruct, cs.Int32sn)

Int64ub_T: _IntConstruct = t.cast(_IntConstruct, cs.Int64ub)
Int64ul_T: _IntConstruct = t.cast(_IntConstruct, cs.Int64ul)
Int64sb_T: _IntConstruct = t.cast(_IntConstruct, cs.Int64sb)
Int64sl_T: _IntConstruct = t.cast(_IntConstruct, cs.Int64sl)
Int64un_T: _IntConstruct = t.cast(_IntConstruct, cs.Int64un)
Int64sn_T: _IntConstruct = t.cast(_IntConstruct, cs.Int64sn)

__all__ = [
    "ConstructProto",
    "Int_T",
    "Int8ub_T",
    "Int8ul_T",
    "Int8sb_T",
    "Int8sl_T",
    "Int8un_T",
    "Int8sn_T",
    "Int16ub_T",
    "Int16ul_T",
    "Int16sb_T",
    "Int16sl_T",
    "Int16un_T",
    "Int16sn_T",
    "Int24ub_T",
    "Int24ul_T",
    "Int24sb_T",
    "Int24sl_T",
    "Int24un_T",
    "Int24sn_T",
    "Int32ub_T",
    "Int32ul_T",
    "Int32sb_T",
    "Int32sl_T",
    "Int32un_T",
    "Int32sn_T",
    "Int64ub_T",
    "Int64ul_T",
    "Int64sb_T",
    "Int64sl_T",
    "Int64un_T",
    "Int64sn_T",
]
