#!/usr/bin/python3

import os
import time
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("-i", "--ip", help="Target IP", required=True, dest="target_ip")

# Read arguments from the command line
args = parser.parse_args()

# Target
target = args.target_ip

# NMAP
nmap = "nmap"
nmap_sc_sv = "-sC -sV"
nmap_all_ports = "-p-"



print("\n");
print("##########");
print("\n");




# # NIKTO
# nikto_command = "nikto -host http://" + target + "/"
# print("Running Nikto...");
# print("* " + nikto_command);
# time.sleep(0.5);
# os.system(nikto_command);

# print("\n");
# print("##########");
# print("\n");

# # Gobuster
# gobuster_command = "gobuster dir -u http://" + target + "/ -w /usr/share/seclists/Discovery/Web-Content/big.txt -x php,txt --random-agent"
# print("Running Gobuster (with big.txt | php,txt extensions | random agent)...")
# print("* " + gobuster_command);
# time.sleep(0.5);
# os.system(gobuster_command)

