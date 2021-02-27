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
        return _codec_map.get(obj_type, DefaultCodec())

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

class TreeNodeListCodec(_BaseCodec):

    def encode(self, _object: List[TreeNode]) -> List[List[int]]:
        return list(map(BiTree.level_order, _object))

    def decode(self, _serial: List[List[int]]) -> List[TreeNode]:
        return list(map(BiTree.new, _serial))

_codec_map = {
    TreeNode: BiTreeCodec(),
    ListNode: LinkListCodec(),
    List[TreeNode]: TreeNodeListCodec()
}
