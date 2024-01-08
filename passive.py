import sys
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

args = sys.argv


def help():
    print("Welcome to passive v1.0.0\n"
          "OPTIONS:\n"
          "        -fn :     Search by full name like 'python3 passive.py -fn \"Jean Dupont\"'\n"
          "        -ip :     Search with IP address, like 'python3 passive.py -ip 127.0.0.1'\n"
          "         -u :     Search with username like 'python3 passive.py -u \"@user01\"'")

def search_by_full_name(name):
    print(f"Searching by full name: {name}")
    parts = name.split()
    if len(parts) < 2:
        print("Error: Full name must include first name and last name, separated by space.")
        return

    first_name, last_name = parts[0], parts[1]

    try:
        search_full_name(first_name, last_name)
    except Exception as e:
        print(e)

def search_full_name(first_name, last_name):
    if not first_name or not last_name:
        raise ValueError("Please enter a name including first name and last name, separated by space.")

    url = f"https://www.whitepages.be/Search/Person/?what={first_name} {last_name}&where="
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("https://www.whitepages.be/Search/Person/ API ERROR, try again later")

    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    general_data = soup.select("div.wg-results-list__item")
    addresses = soup.select("span.wg-address")

    for i, item in enumerate(general_data):
        data_str = item['data-small-result']
        try:
            data = json.loads(data_str)
        except json.JSONDecodeError:
            data = {}
        address = addresses[i].text.strip() if len(addresses) > i else "N/A"
        name = data.get('title', 'N/A')
        phone = data.get('phone', 'N/A')
        results.append({"name": name, "phone": phone, "address": address})

    if not results:
        raise Exception("No results found with the given name.")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{timestamp}.txt"
    final_string = ""
    with open(filename, "w") as file:
        for i, result in enumerate(results):
            final_string += f"\t RESULT {i+1} \n\n\tName:\t\t{result['name']}\n\tAddress:\t{result['address']}\n\tPhone:\t\t{result['phone']}\n\n"

        print(final_string, end='')
        file.write(final_string)
    return final_string


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
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{timestamp}.txt"
    with open(filename, "w") as file:
        for platform, availability in results.items():
            final_string = f"{platform}: {availability}\n"
            print(final_string, end='')
            file.write(final_string)


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