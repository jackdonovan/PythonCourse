import sys
from os import system
import psutil as ps


def showMem():
    system('cls')
    print('Here are your memory statisctics:')
    print(ps.virtual_memory()) 
    
def showData():
    system('cls')
    print('These are your disk partitions: ')
    print(ps.disk_partitions())
    print('This is your current disk usage:')
    print(ps.disk_usage('/'))
    
def showNet():
    system('cls')
    print('These are the addresses set for your NIC: ')
    print(ps.net_if_addrs())
    print('Here is some more information about your NIC(s):')
    print(ps.net_if_stats())

def showUsers():
    system('cls')
    print('Here are the current users on this system: ')
    ps.users()

def showCpu():
    system('cls')
    print("Logical Processors:", ps.cpu_count())
    print("Physical Processors:", ps.cpu_count(logical=False))
    print(ps.cpu_times())
    print(ps.cpu_freq(percpu=True))

def main():
    entered = ''
    while entered != 'x':

        print (" _________________________________________________________ ")
        print ("[ Enter cpu to view cpu stats  | Enter mem for memory stat]")
        print ("[ Enter dat to view disk stats | Enter usr for user stats ]")
        print ("[ Press x then enter to exit   | Enter net for net stats  ]")
        print ("[_________________________________________________________]")
        entered = input()

        if entered == 'cpu':
            showCpu()
        if entered == 'mem':
            showMem()
        if entered == 'dat':
            showData()
        if entered == 'net':
            showNet()
        if entered == 'usr':
            showUsers()
    print("Exiting")
main()