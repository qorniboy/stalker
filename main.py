import subprocess
import json
import pandas as pd
import argparse

def call_amass(whois=False, isProxy=False):
  return

parser = argparse.ArgumentParser(
                    prog = 'python3 stalker.py',
                    description = 'Passive Reconnaisance Automation by Qorniboy',
                    epilog = 'Text at the bottom of help')

parser.add_argument('-c', '--config')      

args = parser.parse_args()
print(args.config)