import os
import unittest

from src.palindromeDetect import PalindromeDetect


class UnitTest(unittest.TestCase):

    def test_mirror(self):
        # ETANT DONNE une chaîne
        chain = "test"

        # QUAND on saisit une chaîne
        result = PalindromeDetect.detect(chain)

        # ALORS celle-ci est renvoyée en miroir
        want = chain[::-1]
        self.assertIn(want, result)


    def test_palindrome(self):
        parameters = [[FrenchLanguage(), "Bien dit !"], [EnglishLanguage(), "Well said !"]]

        for param in parameters:
            with self.subTest(param[0]):
                # ETANT DONNE une chaîne ET l'utilisateur parle une langue
                chain = "kayak"
                language = param[0]

                # QUAND on saisit un palindrome
                result = PalindromeDetect.choosenLanguage(language).detect(chain)

                # ALORS celui-ci est renvoyé ET <Bien dit> de cette langue est envoyé
                expected = chain + os.linesep + param[1]
                self.assertIn(expected, result)


    def test_helloInFirst(self):
        parameters = [[FrenchLanguage(), "Bonjour"], [EnglishLanguage(), "Hello"]]

        for param in parameters:
            with self.subTest(param[0]):
                # ETANT DONNE une chaîne ET l'utilisateur parle une langue
                chain = "test"
                language = param[0]

                # QUAND on saisit une chaîne
                result = PalindromeDetect.choosenLanguage(language).detect(chain)

                # ALORS <Bonjour> de cette langue est envoyé avant toute réponse
                firstLine = result.split(os.linesep)[0]
                self.assertEqual(firstLine, param[1])


    def test_GoodbyeInLast(self):
        parameters = [[FrenchLanguage(), "Au revoir"], [EnglishLanguage(), "Goodbye"]]

        for param in parameters:
            with self.subTest(param[0]):
                # ETANT DONNE une chaîne ET l'utilisateur parle une langue
                chain = "test"
                language = param[0]

                # QUAND on saisit une chaîne
                result = PalindromeDetect.choosenLanguage().detect(chain)

                # ALORS <Au revoir> de cette langue est envoyé en dernier
                lastLine = result.split(os.linesep)[-1]
                self.assertEqual(lastLine, param[1])

if __name__ == '__main__':
    unittest.main()