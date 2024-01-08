import sys
import requests

args = sys.argv


def help():
    print("Welcome to passive v1.0.0\n"
          "OPTIONS:\n"
          "-fn : Searches by full name like 'python3 passive.py -fn \"Jean Dupont\"'\n"
          "-ip : Search with IP address, like 'python3 passive.py -ip 127.0.0.1'\n"
          "-u : Searches with username like 'python3 passive.py -u \"@user01\"'")

def search_by_full_name(name):
    print(f"Searching by full name: {name}")

def search_by_ip(ip):
    print(f"Searching by IP: {ip}")

def search_by_username(username):
    print(f"Searching by username: {username}")
    check_all_usernames(username)

def check_all_usernames(username):
    results = {
        "GitHub": check_github_username(username),
        "TikTok": check_tiktok_username(username),
        "YouTube": check_youtube_username(username),
        "Instagram": check_instagram_username(username),
        "Reddit": check_reddit_username(username)
    }
    with open("results.txt", "w") as file:
        for platform, availability in results.items():
            result_line = f"{platform}: {availability}\n"
            print(result_line, end='')
            file.write(result_line)


def check_github_username(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    return "Yes" if response.status_code == 200 else "No"

def check_tiktok_username(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    return "Yes" if response.status_code == 200 else "No"

def check_youtube_username(username):
    url = f"https://www.youtube.com/{username}"
    response = requests.get(url)
    return "Yes" if response.status_code == 200 else "No"

def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}"
    response = requests.get(url)
    return "Yes" if response.status_code == 200 else "No"

def check_reddit_username(username):
    url = f"https://www.reddit.com/user/{username}"
    response = requests.get(url)
    return "Yes" if response.status_code == 200 else "No"

def parse_args(args):
    if "--help" in args:
        help()
    elif "-fn" in args:
        name_index = args.index("-fn") + 1
        if name_index < len(args):
            search_by_full_name(args[name_index])
        else:
            print("Full name not provided")
    elif "-ip" in args:
        ip_index = args.index("-ip") + 1
        if ip_index < len(args):
            search_by_ip(args[ip_index])
        else:
            print("IP address not provided")
    elif "-u" in args:
        username_index = args.index("-u") + 1
        if username_index < len(args):
            search_by_username(args[username_index])
        else:
            print("Username not provided")
    else:
        print("Unknown command. Use '--help' for guidelines.")

parse_args(sys.argv[1:])