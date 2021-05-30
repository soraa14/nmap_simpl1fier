#!/usr/bin/python3

import os
import time
import argparse
from colorama import Fore, Style

# Initiate the parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("--i", help="Target IP", dest="target_ip", required=True)
parser.add_argument("--scsv", help="-sC -sV", nargs="?", const="-sC -sV")
parser.add_argument("--ap", help="-p-", nargs="?", const="-p-")
parser.add_argument("--all", help="-sC -sV -p-", nargs="?", const="-sC -sV -p-")


# Read arguments from the command line
args = parser.parse_args()

# Targets
target = args.target_ip

if args.target_ip:
    normal_command = "nmap" + " " + target
    print(Fore.GREEN + "Running... " + normal_command)
    print(Style.RESET_ALL)
    time.sleep(0.5)
    os.system(normal_command)

if args.scsv:
    scsv_command = "nmap" + " " + args.scsv + " " + target
    print(Fore.GREEN + "Running... " + scsv_command)
    print(Style.RESET_ALL)
    time.sleep(0.5)
    os.system(scsv_command)

if args.ap:
    ap_command = "nmap" + " " + args.ap + " " + target
    print(Fore.GREEN + "Running... " + ap_command)
    print(Style.RESET_ALL)
    time.sleep(0.5)
    os.system(ap_command)

if args.all:
    all_command = "nmap" + " " + args.all + " " + target 
    print(Fore.GREEN + "Running... " + all_command)  
    print(Style.RESET_ALL)
    time.sleep(0.5)
    os.system(all_command)  