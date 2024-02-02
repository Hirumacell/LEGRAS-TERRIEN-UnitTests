import os

class PalindromeDetect:
    def __init__(self, language):
        self.__language = language

    def detect(self, chain):
        mirror = chain[::-1]

        start = (self.__language.salutation() + os.linesep + mirror + os.linesep)

        return (start + self.__language.congrats() if chain == mirror else start) + os.linesep + self.__language.goodbye()
    