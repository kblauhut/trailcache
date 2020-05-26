from colorama import init, Fore
from trailcache.core import run_script


def main():
    init()
    print("Please enter your token.")
    token = input()

    print("Set the request limit [Default = 25]")
    limit = input()

    print("Set the max trail to cache distance in m [Default = 200]")
    distance = input()

    run_script(token, limit, distance)
    print(Fore.GREEN + "success")
