#!/usr/bin/python3
from github import Github
import sys
import os


from config import token
# from reponame import gen_reponame
#
#
# reponame = gen_reponame()
reponame = "gitscript"

def create_repo(token, reponame):
    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(reponame)


def is_repo(token, reponame):
    g = Github(token)
    user = g.get_user()
    try:
        user.get_repo(reponame)
        return True
    except:
        return False


def create_new_git(reponame):
    os.system("mkdir %s" % reponame)
    os.system("git init %s" % reponame)
    create_repo (token, reponame)
    os.chdir(reponame)
    os.system("git remote add origin 'https://github.com/serpent3/%s'" % reponame)


def commit(token, reponame):
    os.system("git add *")
    os.system("git commit")
    os.system("git push origin master")


create_new_git (reponame)
os.system("cp ../g1.py .")
commit(token, reponame)
# print(is_repo(token, reponame))
