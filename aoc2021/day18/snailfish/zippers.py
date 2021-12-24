from dataclasses import dataclass
from typing import Optional

from .snailfish_numbers import SnailfishNumber, SnailfishPair


@dataclass
class Crumb:
    left_sibling: SnailfishNumber | None
    right_sibling: SnailfishNumber | None


@dataclass
class Zipper:
    tree: SnailfishNumber
    crumbs: list[Crumb]

    def go_left(self) -> "Zipper":
        match self:
            case Zipper(SnailfishNumber(SnailfishPair(left, right)), crumbs):
                return Zipper(left, [Crumb(None, right)] + crumbs)

    def go_right(self) -> "Zipper":
        match self:
            case Zipper(SnailfishNumber(SnailfishPair(left, right)), crumbs):
                return Zipper(right, [Crumb(left, None)] + crumbs)

    def go_up(self) -> "Zipper":
        match self:
            case Zipper(tree, [Crumb(None, right), *crumbs]):
                return Zipper(SnailfishNumber(SnailfishPair(tree, right)), crumbs)
            case Zipper(tree, [Crumb(left, None), *crumbs]):
                return Zipper(SnailfishNumber(SnailfishPair(left, tree)), crumbs)

    def find_pair_at_depth(self, depth, /, *, current_depth=0) -> Optional["Zipper"]:
        match self:
            case Zipper(
                SnailfishNumber(SnailfishPair(SnailfishNumber(left), SnailfishNumber(right))), _
            ):
                if current_depth < depth:
                    return self.go_left().find_pair_at_depth(
                        depth, current_depth=current_depth + 1
                    ) or self.go_right().find_pair_at_depth(depth, current_depth=current_depth + 1)
                if current_depth == depth and isinstance(left, int) and isinstance(right, int):
                    return self
        return None

    def to_snailfish_number(self) -> SnailfishNumber:
        result = self
        while len(result.crumbs) > 0:
            result = result.go_up()
        return result.tree
