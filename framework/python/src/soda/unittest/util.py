import subprocess

def print_in_red_color(text):
    command = r'''printf '\033[0;31m''' + text + r'''\033[0m\n' '''
    subprocess.run(command, shell=True)

def print_in_green_color(text):
    command = r'''printf '\033[0;32m''' + text + r'''\033[0m\n' '''
    subprocess.run(command, shell=True)
