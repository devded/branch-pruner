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
    # List of branches to exclude from deletion
    new_branch_list = json.loads(branch_list)
    print(new_branch_list)
    branches_to_exclude = [
        'HEAD -> master',
        'master',
        'main',
    ]
    branches_to_exclude.extend(new_branch_list)
    print(branches_to_exclude)
    # Get all remote branches and exclude specified branches
    all_remote_branches = get_remote_branches()
    all_remote_branches = [branch for branch in all_remote_branches if branch not in branches_to_exclude]
    return all_remote_branches

def view_branches(branch_list):
    # Delete the remaining branches
    log_message("Viewing branches that are picked for removal")
    branches = get_valid_branches(branch_list)
    for branch in branches:
        print("View:", branch)
        # Uncomment the line below to actually delete the branches
        # delete_branch(branch)
        
def delete_branches(branch_list):
 # Delete the remaining branches
    log_message("Viewing branches that are picked for removal")
    branches = get_valid_branches(branch_list)
    user_input = input("Do you want to continue? (y/n): ")
    # print(f"user_input {user_input}")
    if user_input == "y":
        log_message("Removing branches that are picked for removal")
        for branch in branches:
            print("View:", branch)
            # Uncomment the line below to actually delete the branches
            # delete_branch(branch)



def log_message(msg):
    a = " " + msg + " "
    print(f"{a.center(len(a) +40, '=')}")