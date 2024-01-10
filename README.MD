## General

This is tool that gathers information from open source investigative methods.

## Setup

1. Check if python3 is installed
   python3 --version
   If NOT(ubuntu):
   sudo apt update
   sudo apt install python3

## Commands

### python3 passive.py --help

shows different options

### python3 passive.py -fn "Jean Dupont"

Search adress and number associated with given name

### python3 passive.py -u "@user1"

Search social media with given user name

### python3 passive.py -ip 127.0.0.1

Search information about this ip adress.
You can enter your ip for example. https://www.whatismyip.com/

## Audit questions:

https://github.com/01-edu/public/tree/master/subjects/cybersecurity/passive/audit

### What is OSINT?

OSINT aka Open-source intelligence is basically gathering information from open sources.

### What are used investigative methods?

The methods are investigative search by full name, ip address and username.

### How this program works?

This program reads commandline arguments (like -fn, -u, -ip) and provided argument for which we need to investigate on.
For full name it does web scraping from www.whitepages.be, ip address it uses http://ip-api.com and username it checks if that platform userpage exists or not.
