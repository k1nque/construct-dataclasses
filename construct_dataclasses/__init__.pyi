# Copyright (C) 2023 MatrixEditor
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import collections.abc
import dataclasses
import typing as t

import construct as cs
from construct.core import Context, ContextKWType, FilenameType, PathType, StreamType

from .typed_ints import (
    Int8sb_T,
    Int8sl_T,
    Int8sn_T,
    Int8ub_T,
    Int8ul_T,
    Int8un_T,
    Int16sb_T,
    Int16sl_T,
    Int16sn_T,
    Int16ub_T,
    Int16ul_T,
    Int16un_T,
    Int24sb_T,
    Int24sl_T,
    Int24sn_T,
    Int24ub_T,
    Int24ul_T,
    Int24un_T,
    Int32sb_T,
    Int32sl_T,
    Int32sn_T,
    Int32ub_T,
    Int32ul_T,
    Int32un_T,
    Int64sb_T,
    Int64sl_T,
    Int64sn_T,
    Int64ub_T,
    Int64ul_T,
    Int64un_T,
    Int_T,
)

__all__ = [
    "ConstructProto",
    "csfield",
    "subcsfield",
    "dataclass_struct",
    "tfield",
    "to_struct",
    "to_object",
    "container",
    "DataclassStruct",
    "DataclassBitStruct",
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

T = t.TypeVar("T")
U = t.TypeVar("U")

class ConstructProto(t.Protocol[T]):
    def parse(self, data: bytes, **contextkw: ContextKWType) -> T: ...
    def build(self, obj: T, **contextkw: ContextKWType) -> bytes: ...

@t.overload
def subcsfield(
    model: type[T],
    subcon: ConstructProto[U],
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[U]: ...
@t.overload
def subcsfield(
    model: type[T],
    subcon,
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[t.Any]: ...
@t.overload
def csfield(
    subcon: ConstructProto[T],
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    depth: int | None = ...,
    reverse: bool = ...,
    aligned: int | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[T]: ...
@t.overload
def csfield(
    subcon: type[T],
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    depth: int | None = ...,
    reverse: bool = ...,
    aligned: int | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[T]: ...
@t.overload
def csfield(
    subcon: cs.Construct,
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    depth: int | None = ...,
    reverse: bool = ...,
    aligned: int | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[t.Any]: ...
@t.overload
def tfield(
    model: type[T],
    subcon: ConstructProto[T],
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[T]: ...
@t.overload
def tfield(
    model: type[T],
    subcon: cs.Construct,
    doc: str | None = ...,
    parsed: cs.Context | None = ...,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field[t.Any]: ...
def csenum(
    model: type,
    subcon: cs.Construct,
    doc: str | None = None,
    parsed: cs.Context | None = None,
    metadata: collections.abc.Mapping | None = ...,
) -> dataclasses.Field: ...
def to_struct(
    model: type,
    depth: int | None = ...,
    reverse: bool = ...,
    aligned: int | None = ...,
    union: str | int | None = ...,
) -> cs.Struct | cs.Union: ...
def to_object(obj: cs.Container | cs.ListContainer, model: type): ...
def dataclass_struct(
    cls: type[T] | None = ...,
    *,
    bitwise: bool = ...,
    depth: int | None = ...,
    reverse: bool = ...,
    union: str | int | None = ...,
) -> type[T]: ...
def container(cls: type[T] | None = ...) -> type[T]: ...

class DataclassStruct(cs.Adapter, t.Generic[T]):
    model: type[T]
    reverse: bool
    depth: int | None
    aligned: int | None
    union: str | int | None
    def __init__(
        self,
        model: type[T],
        depth: int | None = ...,
        reverse: bool = ...,
        aligned: int | None = ...,
        union: str | int | None = ...,
    ) -> None: ...
    def parse(self, data: bytes, **contextkw: ContextKWType) -> T | None: ...
    def parse_file(
        self, filename: FilenameType, **contextkw: ContextKWType
    ) -> T | None: ...
    def parse_stream(
        self, stream: StreamType, **contextkw: ContextKWType
    ) -> T | None: ...
    def build(self, obj: T, **contextkw: ContextKWType) -> bytes: ...
    def build_file(
        self, obj: T, filename: FilenameType, **contextkw: ContextKWType
    ) -> bytes: ...
    def build_stream(
        self, obj: T, stream: StreamType, **contextkw: ContextKWType
    ) -> bytes: ...
    def _decode(self, obj: t.Any, context: Context, path: PathType) -> T | None: ...
    def _encode(self, obj: T, context: Context, path: PathType) -> dict: ...

def DataclassBitStruct(
    model: type[T],
    depth: int | None = ...,
    reverse: bool = ...,
    union: str | int | None = ...,
): ...
