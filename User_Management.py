import subprocess


def create_user(username):
    result = subprocess.run(
        ['id', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"User '{username}' already exists!")
        return

    subprocess.run(['sudo', 'useradd', username])
    print(f"User '{username}' has been created.")


def remove_user(username):
    subprocess.run(['sudo', 'userdel', '-r', username])
    print(f"User '{username}' has been deleted.")


def add_user_to_group(username, groupname):
    subprocess.run(['sudo', 'usermod', '-aG', groupname, username])
    print(f"User '{username}' has been added to group '{groupname}'.")


def set_user_password(username, password):
    subprocess.run(['echo', f"{username}:{password}", '|', 'sudo', 'chpasswd'])
    print(f"Password for '{username}' has been updated.")


def change_file_permissions(filename, permissions):
    subprocess.run(['sudo', 'chmod', permissions, filename])
    print(f"Permissions of '{filename}' changed to {permissions}.")


def change_file_owner(filename, owner, group):
    subprocess.run(['sudo', 'chown', f"{owner}:{group}", filename])
    print(f"Owner of '{filename}' changed to {owner}:{group}.")


def grant_sudo_access(username):
    subprocess.run(['sudo', 'usermod', '-aG', 'sudo', username])
    print(f"User '{username}' now has sudo privileges.")


def lock_user(username):
    subprocess.run(['sudo', 'passwd', '-l', username])
    print(f"User '{username}' has been locked.")


def unlock_user(username):
    subprocess.run(['sudo', 'passwd', '-u', username])
    print(f"User '{username}' has been unlocked.")


# Example usage

# create_user('Yasmine')
# add_user_to_group('Yasmine', 'sudo')
# set_user_password('Yasmine', '2442000')
# grant_sudo_access('Yasmine')
# change_file_permissions('/etc/passwd', '644')
# change_file_owner('/etc/passwd', 'root', 'root')
# lock_user('Yasmine')
# unlock_user('Yasmine')
# remove_user('Yasmine')
