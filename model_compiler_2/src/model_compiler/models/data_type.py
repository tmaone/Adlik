# Copyright 2019 ZTE corporation. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import enum
from enum import Enum

from onnx import TensorProto as OnnxTensorProto
from tensorflow.core.framework.types_pb2 import DataType as TfDataType
from tensorrt import DataType as TrtDataType

_ONNX_DATA_TYPE = OnnxTensorProto.DataType  # pylint: disable=no-member


class DataType(Enum):
    # Boolean values.

    BOOL = enum.auto()

    # Integer values.

    INT8 = enum.auto()
    UINT8 = enum.auto()
    INT16 = enum.auto()
    UINT16 = enum.auto()
    INT32 = enum.auto()
    UINT32 = enum.auto()
    INT64 = enum.auto()
    UINT64 = enum.auto()

    # Floating number values.

    FLOAT16 = enum.auto()
    BFLOAT16 = enum.auto()
    FLOAT = enum.auto()
    DOUBLE = enum.auto()

    # Complex values.

    COMPLEX64 = enum.auto()
    COMPLEX128 = enum.auto()

    # String values.

    STRING = enum.auto()

    @staticmethod
    def from_tf_data_type(data_type: int):
        if data_type == TfDataType.DT_HALF:
            return DataType.FLOAT16

        return DataType[TfDataType.Name(data_type)[len('DT_'):]]

    def to_tf_data_type(self) -> int:
        if self == DataType.FLOAT16:
            return TfDataType.DT_HALF

        return TfDataType.Value(f'DT_{self.name}')

    @staticmethod
    def from_onnx_data_type(data_type: int):
        return DataType[_ONNX_DATA_TYPE.Name(data_type)]

    def to_onnx_data_type(self) -> int:
        return _ONNX_DATA_TYPE.Value(self.name)

    @staticmethod
    def from_tensorrt_data_type(data_type: TrtDataType):
        if data_type == TrtDataType.HALF:
            return DataType.FLOAT16

        return DataType[data_type.name]

    def to_tensorrt_data_type(self) -> TrtDataType:
        if self == DataType.FLOAT16:
            return TrtDataType.HALF

        return getattr(TrtDataType, self.name)
