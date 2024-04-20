import subprocess
import json

# Function to retrieve remote branches
def get_remote_branches():
    subprocess.run(['git', 'fetch', '--prune'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    result = subprocess.run(['git', 'branch', '-r'], stdout=subprocess.PIPE, text=True)
    branches = result.stdout.splitlines()
    branches = [branch.strip().replace('origin/', '') for branch in branches]
    return branches

# Function to delete a branch
def delete_branch(branch):
    subprocess.run(['git', 'push', 'origin', '--delete', branch])
    print("Deleted branch:", branch)

def get_valid_branches(branch_list):
    whitelist = json.loads(branch_list)
    branches_to_exclude = [
        'HEAD -> master',
        'master',
        'main',
    ]
    branches_to_exclude.extend(whitelist)
    remote_branches = get_remote_branches()
    branches = [branch for branch in remote_branches if branch not in branches_to_exclude]
    return branches

def view_branches(branch_list):
    branches = get_valid_branches(branch_list)
    print_branches(branches)
   
def print_branches(branches):
    log_message("Viewing branches that are picked for removal")
    for branch in branches:
        print(branch)

        
def delete_branches(branch_list):
    branches = get_valid_branches(branch_list)
    print_branches(branches)
    user_input = input("Do you want to continue? (y/n): ")
    
    if user_input == "y":
        log_message("Removing branches that are picked for removal")
        for branch in branches:
            delete_branch(branch)

def log_message(msg):
    a = " " + msg + " "
    print(f"{a.center(len(a) +40, '=')}")