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
        # ETANT DONNE une chaîne
        chain = "kayak"

        # QUAND on saisit un palindrome
        result = PalindromeDetect.detect(chain)

        # ALORS celui-ci est renvoyé ET "Bien dit" est envoyé ensuite
        expected = chain + os.linesep + "Bien dit!"
        self.assertIn(expected, result)


    def test_helloInFirst(self):
        # ETANT DONNE une chaîne
        chain = "test"
        expected = "Bonjour"

        # QUAND on saisit une chaîne
        result = PalindromeDetect.detect(chain)

        # ALORS "Bonjour" est envoyé avant toute réponse
        firstLine = result.split(os.linesep)[0]
        self.assertEqual(firstLine, expected)


    def test_GoodbyeInLast(self):
        # ETANT DONNE une chaîne
        chain = "test"
        expected = "Au revoir"

        # QUAND on saisit une chaîne
        result = PalindromeDetect.detect(chain)

        # ALORS "Au revoir" est envoyé en dernier
        lastLine = result.split(os.linesep)[-1]
        self.assertEqual(lastLine, expected)

if __name__ == '__main__':
    unittest.main()