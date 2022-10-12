import json
from sys import api_version
import unittest
from unittest import mock

from GithubApi4a import user_repos
#just checking if i cloned a right branch
# This code implements the unit test functionality on GithubApi4a.py code

switcher = {
    'https://api.github.com/users/rpalival/repos':'rpalival_repos.json',
    'https://api.github.com/repos/rpalival/567_HW_02a_TestTriangle/commits':'567_HW_2a_commits.json',
    'https://api.github.com/repos/rpalival/GithubApi567_HW_04a/commits':'Github567_HW_4a_commits.json',
    'https://api.github.com/repos/rpalival/HW-01-Testing-triangle-classification/commits':'HW_01_testing_triangle_commits.json',
    'https://api.github.com/repos/rpalival/SSW_567_A/commits':'SSW_567_A_commits.json',
}

class MockResponse:
    def __init__(self,json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

    ok=True 
    
class StCode:
    ok = False

def mock_get_repo(*args):

    if args[0] in switcher:
        with open(switcher[args[0]], encoding="utf-8") as f:
            return MockResponse(json.load(f))
    return StCode


class TestUserRepos(unittest.TestCase):
    def testUserRepo1(self):
        self.assertEqual(user_repos(''), "empty string is invalid input for a username! Please enter a non-empty string.")

    @mock.patch('requests.get', side_effect = mock_get_repo)
    def testUserRepo2(self,mock_A):
        self.assertEqual(user_repos('hutyuejsnn'), "Invalid username.")

    @mock.patch('requests.get', side_effect = mock_get_repo)
    def testUserRepo3(self,mock_B):
        self.assertEqual(user_repos('rpalival'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
