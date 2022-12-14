import unittest

from GithubApi4a import user_repos

# This code implements the unit test functionality on GithubApi4a.py code

class TestUserRepos(unittest.TestCase):
    def testUserRepo1(self):
        self.assertEqual(user_repos(''), "empty string is invalid input for a username! Please enter a non-empty string.")
    def testUserRepo2(self):
        self.assertEqual(user_repos('hutyuejsnn'), "Invalid username.")
    def testUserRepo3(self):
        self.assertEqual(user_repos('rpalival'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()