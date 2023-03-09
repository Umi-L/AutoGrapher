from enum import Enum

class BracketType(Enum):
    ROUND = 1
    SQUARE = 2
    RHOMBUS = 3
    STADIUM = 4
    CYLINDER = 6
    CIRCLE = 7
    HEXAGON = 8
    PARALLELOGRAM = 9
    TRAPEZOID = 10

    # special brackets
    BEGIN_SUBGRAPH = 11
    END_SUBGRAPH = 12

    def openBracket(self):
        if self == BracketType.ROUND:
            return "("
        elif self == BracketType.SQUARE:
            return "["
        elif self == BracketType.RHOMBUS:
            return "{"
        elif self == BracketType.STADIUM:
            return "(["
        elif self == BracketType.CYLINDER:
            return "[("
        elif self == BracketType.CIRCLE:
            return "(("
        elif self == BracketType.HEXAGON:
            return "{{"
        elif self == BracketType.PARALLELOGRAM:
            return "[\\"
        elif self == BracketType.TRAPEZOID:
            return "[/"

    def closeBracket(self):
        if self == BracketType.ROUND:
            return ")"
        elif self == BracketType.SQUARE:
            return "]"
        elif self == BracketType.RHOMBUS:
            return "}"
        elif self == BracketType.STADIUM:
            return "])"
        elif self == BracketType.CYLINDER:
            return ")]"
        elif self == BracketType.CIRCLE:
            return "))"
        elif self == BracketType.HEXAGON:
            return "}}"
        elif self == BracketType.PARALLELOGRAM:
            return "/]"
        elif self == BracketType.TRAPEZOID:
            return "\\]"

    def wrap(self, text):
        return self.openBracket() + text + self.closeBracket()