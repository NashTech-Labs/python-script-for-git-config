from subprocess import Popen, PIPE

import os
import yaml
import json
import boto3
import argparse

"""
Runs git config for email and name on command line to allow commits to work
param user: native ID of the requester of the container
"""
def config_git(user):
    # Set the email, check status
    proc = Popen(["git", "config", "user.email", f"{user}@xyz.com"], stdout=PIPE, stderr=PIPE)
    stat_out, stat_err = proc.communicate()
    return_code = proc.returncode

    if return_code:
        raise RuntimeError(f"Git config email failed with code {return_code}:\n{stat_err}\n{stat_out}")

    # Set the name, check status
    proc = Popen(["git", "config", "user.name", user], stdout=PIPE, stderr=PIPE)
    stat_out, stat_err = proc.communicate()
    return_code = proc.returncode

    if return_code:
        raise RuntimeError(f"Git config user failed with code {return_code}:\n{stat_err}\n{stat_out}")