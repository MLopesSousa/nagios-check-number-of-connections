#!/usr/bin/python

import commands
import sys
import re

def main(): 
        regex = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(:([0-9]){1,5})?$"
        ip = sys.argv[1].strip()
        min_connections_default = False

        try:
                if int(sys.argv[2].split(':')[0]) is not None:
                        min_connections = int(sys.argv[2].split(':')[0])
        except:
                min_connections_default = True
                min_connections = 0

        try:
                if int(sys.argv[2].split(':')[1]) is not None:
                        max_connections = int(sys.argv[2].split(':')[1])
        except:
                max_connections = 65535

        if re.match(regex, ip):
                cmd = "netstat -natu |grep " + ip
                status, sockets  = commands.getstatusoutput(cmd)

                if status > 0:
                        num_connections = 0
                else:
                        num_connections = len(sockets.split('\n'))

                if num_connections == 0 and min_connections_default is True:
                        print("0 connections to IP: " + ip + " found!")
                        sys.exit(0)

                elif num_connections == 0 and min_connections_default is False:
                        print("0 connections to IP: " + ip + " found!")
                        sys.exit(2)

                elif num_connections >= min_connections and num_connections <= max_connections:
                        print(sockets)
                        sys.exit(0)
                else:
                        print("Number of connections: " + str(num_connections) + ", min expected: " + str(min_connections) + ", max expected " + str(max_connections))
                        sys.exit(2)
        else:
                print("The first argument must be an IP address: ")
                sys.exit(2)

if __name__ == "__main__":
        if len(sys.argv) == 3:
                main()
				
        else:
                print("Sintax error: " + sys.argv[0] + " ${IP:PORT} ${MIN_THRESHOLD}:${MAX_THRESHOLD}")
                sys.exit(2)
