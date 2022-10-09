import unittest

from GithubApi4a import user_repos

# This code implements the unit test functionality on GithubApi4a.py code

class TestUserRepos(unittest.TestCase):
    def testUserRepo1(self):
        self.assertEqual(user_repos(None), "Your Input is invalid! Please enter a string.")
    def testUserRepo2(self):
        self.assertEqual(user_repos('!'), "Invalid username.")
    def testUserRepo3(self):
        self.assertEqual(user_repos('hutyuejsnn'), "Invalid username.")
    def testUserRepo4(self):
        self.assertEqual(user_repos('rpalival'), True)
    def testUserRepo5(self):
        self.assertEqual(user_repos(False), "Your Input is invalid! Please enter a string.")
    def testUserRepo6(self):
        self.assertEqual(user_repos(567), "Your Input is invalid! Please enter a string.")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()