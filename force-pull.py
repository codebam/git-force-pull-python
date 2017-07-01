#!/usr/bin/env python3

from git import Repo
import subprocess

repo_dir = '/var/www/html'

repo = Repo(repo_dir)
assert not repo.bare

master = repo.heads.master
origin = repo.remote('origin')
# set references

origin.fetch()
# fetch updates

repo.head.reset(commit='origin/master', **{'hard':True})
# reset head to origin/master forcefully
