from abc import ABC, abstractmethod
from typing import Any, List

from soda.leetcode.bitree import BiTree, TreeNode
from soda.leetcode.linklist import LinkList, ListNode

class _BaseCodec(ABC):

    @abstractmethod
    def encode(self, _object: Any) -> Any:
        pass

    @abstractmethod
    def decode(self, serial_data: Any) -> Any:
        pass

class CodecFactory:

    @classmethod
    def create(cls, obj_type: Any) -> _BaseCodec:
        if obj_type is TreeNode:
            return BiTreeCodec()
        elif obj_type is ListNode:
            return LinkListCodec()
        else:
            return DefaultCodec()

class DefaultCodec(_BaseCodec):

    def encode(self, _object: Any) -> Any:
        return _object

    def decode(self, serial_data: Any) -> Any:
        return serial_data

class BiTreeCodec(_BaseCodec):

    def encode(self, _object: TreeNode) -> List[int]:
        return BiTree.level_order(_object)

    def decode(self, serial_data: List[int]) -> TreeNode:
        return BiTree.new(serial_data)

class LinkListCodec(_BaseCodec):

    def encode(self, _object: ListNode) -> List[int]:
        return LinkList.list_values(_object)

    def decode(self, serial_data: List[int]) -> ListNode:
        return LinkList.new_s(serial_data)
