from frenchLanguage import FrenchLanguage
from palindromeDetect import PalindromeDetect


class PalindromeDetectBuilder:
    __language = FrenchLanguage()

    @classmethod
    def buildDefault(self):
        return PalindromeDetectBuilder.build(self)

    def build(self):
        return PalindromeDetect(self.__language)

    def choosenLanguage(self, language):
        self.__language = language
        return self
