# nagios-check-number-of-connections

We can use this script to test if in some server the amount of request is inside the expected behavior. 

To ensure that connections to IP:  10.10.10.1 are not more than 10 and less 2, we can use the script like this.
/usr/lib64/nagios/plugins/check_connections_to.py 10.10.10.1  2:10

To ensure that connections to socket:  10.10.10.1:80 are not more than 10 and less 2, we can use the script like this.
/usr/lib64/nagios/plugins/check_connections_to.py 10.10.10.1:80  2:10

To ensure that connections to IP:  10.10.10.1 are not more than 10  but must have at least 2, we can use the script like this.
/usr/lib64/nagios/plugins/check_connections_to.py 10.10.10.1 2:10

To ensure that connections to IP:  10.10.10.1 are not more than 10  but the minimum is not a concern, we can use the script like this.
/usr/lib64/nagios/plugins/check_connections_to.py 10.10.10.1  :10

To ensure that connections to IP:  10.10.10.1 are not less than 2 but the maximum is not a concern, we can use the script like this.
/usr/lib64/nagios/plugins/check_connections_to.py 10.10.10.1 2:

To ensure that connections to IP:  must exists, we can use the script like this.
/usr/lib64/nagios/plugins/check_connections_to.py 10.10.10.1 :

As any other Nagios plugin the script return code will be 0 to success and 2 in case of behavior unexpected.

09/01/2019
