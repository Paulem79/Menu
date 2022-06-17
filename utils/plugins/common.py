import imp
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from colorate import colorate; colorate()
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from time import sleep

from utils.plugins.variable import *

def main():
    print("")

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - ")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - {author}\x07")
    else:
        pass

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} {g}Loading...{w} - {name} {i}""")
		sys.stdout.flush()

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def transition():
    clear()
    Spinner()
    clear()

def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'

def hometitle():
    size = os.get_terminal_size()
    namemenu = f"{b}{name}{w}".center(size.columns)
    print(f"""\n\n{namemenu}\n""")

banner = r"""
 ╔╦╦═════╦╦╗  
╔╬╬╝     ╚╬╬╗ 
║║║  ╔╦╗  ║║║ 
║║║  ║║║  ║║║ 
║║║  ║║╠╗╔╬╩╝ 
║║║  ╚╩╩╩╩╝ 
╚╩╬╗ 
  ╚╩════════
"""[1:]