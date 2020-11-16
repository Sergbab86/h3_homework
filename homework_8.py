
ipList = ['216.151.180.231', '216.151.180.232', '216.151.180.237']


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ipList):
        self.ipList = ['216.151.180.231', '216.151.180.232', '216.151.180.237']

    @property
    def ipList(self):
        return self.ipList

    @ipList.setter
    def ipList(self, newList):
        self.ipList = newList

    def reverse_IP(self):
        """Return it's IPs reversed"""
        reversed_ip = []
        for ip in ipList:
            spl_ip = ip.split('.')
            spl_ip.reverse()
            rev_ip = '.'.join(spl_ip)
            reversed_ip.append(rev_ip)
        return reversed_ip

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        new_ip_3 = []
        for ip in ipList:
            ip1 = ip.split('.')
            ip2 = ip1.pop(0)
            new_ip3 = '.'.join(ip1)
            new_ip_3.append(new_ip3)
        return new_ip_3

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        ip_last_part = []
        for ip in ipList:
            ip1 = ip.split('.')
            ip2 = ip1.pop
            ip_last_part.append(ip2)
        return ip_last_part
