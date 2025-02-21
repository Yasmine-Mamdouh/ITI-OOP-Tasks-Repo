import os
import subprocess


def clean_temp_files():
    temp_dirs = ["/tmp", "/var/tmp", "~/.cache"]

    for directory in temp_dirs:
        expanded_dir = os.path.expanduser(directory)
        subprocess.run(['sudo', 'rm', '-rf', expanded_dir + '/*'])
        print(f"Cleaned: {expanded_dir}")


clean_temp_files()
