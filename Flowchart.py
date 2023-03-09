from typing import List

from AutoGrapher.BracketTypes import BracketType


class Flowchart:
    tokens = []
    brackets: List[BracketType] = []
    functions = []

    def __init__(self, tokens):
        self.tokens = tokens
        self.brackets = []

    # def addBracket(self, bracketType, index=None):
    #     if index is None:
    #         index = len(self.tokens)
    #     self.brackets[index] = bracketType

    def addToken(self, token, bracketType=None, index=None):
        if index is None:
            index = len(self.tokens)
        self.tokens.insert(index, token)

        if bracketType is not None:
            self.brackets.insert(index, bracketType)
        else:
            self.brackets.insert(index, BracketType.ROUND)

    def registerFunction(self, func, indentation):
        self.functions.append(func)
