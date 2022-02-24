"""python program to map an IP address to its corresponding AS
To run program, type this into terminal: python3 ip2as.py DB_091803.txt IPlist.txt"""
import sys
from ipaddress import *

if __name__ == '__main__':
    # get the file names from the command line
    dbfile = sys.argv[1]
    ipfile = sys.argv[2]

    # open the files and read through them
    with open(dbfile, "r") as db:
        dbLines = db.readlines()
    with open(ipfile, "r") as ip:
        ipLines = ip.readlines()

    # convert dbList into a dict
    dbDict = {}
    dbList = []
    # go through the db line by line
    for idx, line in enumerate(dbLines):
        # convert into ip network
        line = line.split()
        try:
            line[0] = line[0] + '/' + line[1]
            line[0] = ip_network(line[0])
            dbDict[line[0]] = int(line[2])  # the key is the IP subnet and the value is the AS
            dbList.append(line[0])
        except:  # error checking for bad networks
            continue

    # open a file to print output
    output = open('myoutput.txt', 'w')
    # go through the IP list and find its corresponding value from the db Dict
    for ip in ipLines:
        ip = ip.replace('\n', '')
        address = ip_address(ip)
        subnets = []
        # go through the dbList and find the right one
        for network in dbList:
            if address in network:
                subnets.append(network)
        # if only one subnet then print out
        if len(subnets) == 1:
            output.write(f'{str(subnets[0])} {dbDict[subnets[0]]} {address}\n')
        else:
            # the longest matching prefix will be the last subnet from the list
            output.write(f'{str(subnets[-1])} {dbDict[subnets[-1]]} {address}\n')
    # close file
    output.close()
