from dataclasses import dataclass
from typing import Optional, Any

from .zippers import Crumb, Zipper


@dataclass
class SnailfishPair:
    left: "SnailfishNumber"
    right: "SnailfishNumber"


@dataclass
class SnailfishNumber:
    value: int | SnailfishPair

    def __add__(self, other: "SnailfishNumber") -> "SnailfishNumber":
        return SnailfishNumber(SnailfishPair(self, other)).reduce(explode_depth=4, split_at=10)

    def explode(self, depth: int = 4) -> Optional["SnailfishNumber"]:
        match Zipper(self, []).find_pair_at_depth(depth):
            case Zipper(
                SnailfishNumber(SnailfishPair(SnailfishNumber(left), SnailfishNumber(right))),
                crumbs,
            ):
                left_sibling = next((index for index, crumb in enumerate(crumbs) if crumb.right_sibling is None), None)
                right_sibling = next((index for index, crumb in enumerate(crumbs) if crumb.left_sibling is None), None)
                if left_sibling is not None:
                    crumbs[left_sibling] = Crumb(crumbs[left_sibling].left_sibling.add_right(left), None)
                if right_sibling is not None:
                    crumbs[right_sibling] = Crumb(None, crumbs[right_sibling].right_sibling.add_left(right))
                return Zipper(SnailfishNumber(0), crumbs).to_snailfish_number()
        return None

    def add_left(self, value: int) -> "SnailfishNumber":
        match self:
            case SnailfishNumber(SnailfishPair(left, right)):
                return SnailfishNumber(SnailfishPair(left.add_left(value), right))
            case SnailfishNumber(old_value):
                return SnailfishNumber(old_value + value)

    def add_right(self, value: int) -> "SnailfishNumber":
        match self:
            case SnailfishNumber(SnailfishPair(left, right)):
                return SnailfishNumber(SnailfishPair(left, right.add_right(value)))
            case SnailfishNumber(old_value):
                return SnailfishNumber(old_value + value)

    def split(self, split_at: int = 10) -> Optional["SnailfishNumber"]:
        match self:
            case SnailfishNumber(SnailfishPair(left, right)):
                if (new_left := left.split(split_at)) is not None:
                    return SnailfishNumber(SnailfishPair(new_left, right))
                if (new_right := right.split(split_at)) is not None:
                    return SnailfishNumber(SnailfishPair(left, new_right))
            case SnailfishNumber(value):
                if value >= split_at:
                    left = SnailfishNumber(value // 2)
                    right = SnailfishNumber(value - left.value)
                    return SnailfishNumber(SnailfishPair(left, right))
        return None

    def reduce(self, explode_depth: int = 4, split_at: int = 10) -> "SnailfishNumber":
        result = self
        while (new_result := result.explode(explode_depth)) is not None:
            result = new_result
        if (new_result := result.split(split_at)) is not None:
            return new_result.reduce(explode_depth, split_at)
        return result

    @property
    def magnitude(self) -> int:
        match self:
            case SnailfishNumber(SnailfishPair(left, right)):
                return 3 * left.magnitude + 2 * right.magnitude
            case SnailfishNumber(value):
                return value

    def to_list(self):
        match self:
            case SnailfishNumber(SnailfishPair(left, right)):
                return [left.to_list(), right.to_list()]
            case SnailfishNumber(value):
                return value

    @staticmethod
    def from_list(nested_list: list[Any] | int) -> "SnailfishNumber":
        match nested_list:
            case [left, right]:
                return SnailfishNumber(
                    SnailfishPair(SnailfishNumber.from_list(left), SnailfishNumber.from_list(right))
                )
            case _:
                return SnailfishNumber(nested_list)