import os
import requests
import shutil

class GitHubRepoUpdater:
    def __init__(self, github_username, github_repo):
        self.github_username = github_username
        self.github_repo = github_repo

    def check_for_update(self):
        # Fetch the version.txt file from the GitHub repository
        response = requests.get(
            f"https://raw.githubusercontent.com/{self.github_username}/{self.github_repo}/main/version.txt")
        new_version = response.text.strip()

        # Read the local version.txt file
        local_file = os.path.join(os.path.dirname(__file__), "version.txt")
        if os.path.exists(local_file):
            with open(local_file, "r") as file:
                old_version = file.read().strip()
        else:
            old_version = None

        # Compare versions and update if necessary
        if old_version != new_version:
            # Clone the new repository
            os.system(f"git clone https://github.com/{self.github_username}/{self.github_repo} .")

            print("Repository updated.")
        else:
            print("Repository is up to date.")
