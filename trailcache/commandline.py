from tqdm import tqdm
from colorama import init, Fore
from trailcache.struct import Settings, Filters


def init_colorama():
    init()


def get_user_info():
    print("Please enter your token.")
    token = input()

    print("Set the request limit [Default = 25]")
    request_limit = int(input())

    print("Set the max trail to cache distance in m [Default = 200]")
    distance = int(input())

    filters = Filters(distance, [34, 8, 243, 5, 1], [54, 2, 45, 4, 25],
                      [1, 5], [1, 5])
    settings = Settings(token, request_limit, filters)

    return settings


def print_err(info):
    print("[" + Fore.LIGHTRED_EX + "ERROR" + Fore.RESET + "] " + info)


def print_info(info):
    print("[" + Fore.LIGHTBLUE_EX + "INFO" + Fore.RESET + "] " + info)


def print_ok(info):
    print("[" + Fore.GREEN + "OK" + Fore.RESET + "] " + info)


class ProgressBar:
    def __init__(self, info, n):
        self.info = info
        self.n = n
        self.bar = tqdm(total=n, desc="[" + Fore.LIGHTYELLOW_EX +
                        "STATUS" + Fore.RESET + "] ", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}")

    def update(self):
        self.bar.update(1)

    def close(self):
        self.bar.close()
