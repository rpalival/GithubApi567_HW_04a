import json
import requests

username = input("Enter your github username/userID: ")

def user_repos(user):
    
    repo_api_url = f"https://api.github.com/users/{user}/repos"
    api_response = requests.get(repo_api_url)

    if api_response.status_code != 200:
        print("No Username / No Response")
        return False
    
    repos = api_response.json()

    if len(repos) == 0:
        print("The user has no Repositories")
        return False

    for repo in repos:
        commits_api_url = f"https://api.github.com/repos/{user}/{repo['name']}/commits"
        commit_response = requests.get(commits_api_url)
        commits = commit_response.json()
        print(f"Repo: {repo['name']} Number of commits: {str(len(commits))}")
        
    return True

if __name__ == "__main__":
    username = input("Enter your github username/userID: ")
    user_repos(username)