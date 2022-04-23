#!/usr/bin/python3
"""
    You must use the package requests.
"""
import requests
from sys import argv


def getCommitsGitHub(repository, ownername):
    """
    Function:
        Python script that takes api GitHub
        list 10 commits (from the most recent to oldest)
        of the repository.
    Args:
        api (str): GitHub API url.
        repository (str): GitHub repository name.
        ownername (str): GitHub owner name.
    """
    api = 'https://api.github.com/repos/{}/{}/commits'.format(
                                                                ownername,
                                                                repository
                                                            )
    myrequest = requests.get(api)
    myjson = myrequest.json()
    # print(myjson)
    for i in range(0, 10):
        print("{}: {}".format(
            myjson[i].get('sha'),
            myjson[i].get("commit").get("author").get("name")
        ))


if __name__ == '__main__':
    repository = argv[1]
    ownername = argv[2]
    getCommitsGitHub(repository, ownername)
