from __future__ import annotations

import typing as t

from construct.core import ContextKWType

T_co = t.TypeVar("T_co", covariant=True)

class ConstructProto(t.Protocol[T_co]):
    def parse(self, data: bytes, **contextkw: ContextKWType) -> T_co: ...
    def build(self, obj: T_co, **contextkw: ContextKWType) -> bytes: ...

_IntConstruct = ConstructProto[int]

Int_T: _IntConstruct
Int8ub_T: _IntConstruct
Int8ul_T: _IntConstruct
Int8sb_T: _IntConstruct
Int8sl_T: _IntConstruct
Int8un_T: _IntConstruct
Int8sn_T: _IntConstruct

Int16ub_T: _IntConstruct
Int16ul_T: _IntConstruct
Int16sb_T: _IntConstruct
Int16sl_T: _IntConstruct
Int16un_T: _IntConstruct
Int16sn_T: _IntConstruct

Int24ub_T: _IntConstruct
Int24ul_T: _IntConstruct
Int24sb_T: _IntConstruct
Int24sl_T: _IntConstruct
Int24un_T: _IntConstruct
Int24sn_T: _IntConstruct

Int32ub_T: _IntConstruct
Int32ul_T: _IntConstruct
Int32sb_T: _IntConstruct
Int32sl_T: _IntConstruct
Int32un_T: _IntConstruct
Int32sn_T: _IntConstruct

Int64ub_T: _IntConstruct
Int64ul_T: _IntConstruct
Int64sb_T: _IntConstruct
Int64sl_T: _IntConstruct
Int64un_T: _IntConstruct
Int64sn_T: _IntConstruct

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
