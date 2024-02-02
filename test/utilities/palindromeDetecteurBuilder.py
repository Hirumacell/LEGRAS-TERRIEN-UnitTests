from frenchLanguage import FrenchLanguage
from palindromeDetect import PalindromeDetect
from timeDay import TimeDay


class PalindromeDetectBuilder:
    __language = FrenchLanguage()
    __timeDay = TimeDay.Default

    @classmethod
    def buildDefault(self):
        return PalindromeDetectBuilder.build(self)

    def build(self):
        return PalindromeDetect(self.__language, self.__timeDay)

    def choosenLanguage(self, language):
        self.__language = language
        return self

    def choosenTimeDay(self, timeDay):
        self.__timeDay = timeDay
        return self
