import json
import requests

def user_repos(user):
    
    if not isinstance(user, str):
        return "Your Input is invalid! Please enter a string."

    repo_api_url = f"https://api.github.com/users/{user}/repos"
    api_response = requests.get(repo_api_url)

    if not api_response.ok:
        return "Invalid username."
    
    repos = api_response.json()
    
    for repo in repos:
        commits_api_url = f"https://api.github.com/repos/{user}/{repo['name']}/commits"
        commit_response = requests.get(commits_api_url)
        commits = commit_response.json()
        print(f"Repo: {repo['name']} Number of commits: {str(len(commits))}")
        
    return True

if __name__ == "__main__":
    user = input("Enter your github username/userID: ")
    user_repos(user)