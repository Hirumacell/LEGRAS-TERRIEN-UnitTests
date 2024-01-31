import os

class PalindromeDetect:
    @classmethod
    def detect(cls, chain):
        mirror = chain[::-1]

        start = "Bonjour" + os.linesep + mirror + os.linesep

        return (start + "Bien dit!" if chain == mirror else start) + os.linesep + "Au revoir"