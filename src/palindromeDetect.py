import os

class PalindromeDetect:
    def __init__(self, language, timeDay):
        self.__language = language
        self.__timeDay = timeDay

    def detect(self, chain):
        mirror = chain[::-1]

        start = (self.salutation() + os.linesep + mirror + os.linesep)

        return (start + self.congrats() if chain == mirror else start) + os.linesep + self.goodbye()

    def congrats(self):
        return self.__language.congrats()

    def salutation(self):
        return self.__language.salutation(self.__timeDay)

    def goodbye(self):
        return self.__language.goodbye(self.__timeDay)
