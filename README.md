# IP2AS
Maps IP addresses to its AS network. 
Can be run from the command line and passed file names as parameters.
The arguments should be [database file] [IP addresses]
The program takes an IP address, performs the longest matching prefix on a compressed version of a routing table and outputs the home AS number for that IP address.
The output is written to a text file.
