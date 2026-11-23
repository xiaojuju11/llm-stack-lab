#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-command replacement for `git push` on D:\\llm-stack-lab.

git over HTTPS to github.com is blocked here (Connection was reset), but the
GitHub REST API works. This wrapper calls the REST-API-based sync script, so
after `git commit` you can run `python push.py` instead of `git push`.

It uploads only new/changed files, never deletes, never touches secrets, and
reuses the contribution email. If there is nothing new, it exits without
creating an empty commit.
"""
import os
import subprocess
import sys

REPO_DIR = r"D:\llm-stack-lab"
SYNC = os.path.join(
    os.path.expanduser("~"),
    "WorkBuddy", "2026-11-08-19-58-42", "daily-github", "sync_local.py",
)


def main():
    if not os.path.isfile(SYNC):
        print("ERROR: sync script not found: %s" % SYNC, file=sys.stderr)
        return 1
    try:
        subject = subprocess.check_output(
            ["git", "-C", REPO_DIR, "log", "-1", "--pretty=%s"],
            text=True, encoding="utf-8",
        ).strip()
    except Exception:
        subject = ""
    subject = subject or "sync local study notes"
    # Don't double-prefix when the local commit is already conventional.
    import re
    if re.match(r"^(feat|fix|docs|chore|refactor|style|test|build|ci|perf|revert)(\(.+\))?!?:", subject):
        message = subject
    else:
        message = "chore(sync): %s" % subject
    return subprocess.call([
        sys.executable, SYNC,
        "--local", REPO_DIR,
        "--repo", "llm-stack-lab",
        "-m", message,
    ])


if __name__ == "__main__":
    sys.exit(main())
