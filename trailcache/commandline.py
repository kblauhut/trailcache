from colorama import init, Fore


def get_user_info():
    init()
    print("Please enter your token.")
    token = input()

    print("Set the request limit [Default = 25]")
    limit = int(input())

    print("Set the max trail to cache distance in m [Default = 200]")
    distance = int(input())

    user_info = [token, limit, distance]
    return user_info


def print_err(info):
    print("[" + Fore.LIGHTRED_EX + "ERROR" + Fore.RESET + "]" + info)


def print_info(info):
    print("[" + Fore.LIGHTBLUE_EX + "INFO" + Fore.RESET + "]" + info)


def print_ok(info):
    print("[" + Fore.GREEN + "OK" + Fore.RESET + "]" + info)
