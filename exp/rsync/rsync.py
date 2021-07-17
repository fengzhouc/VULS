# -*- coding:utf-8 -*-
"""
    Rsync匿名访问漏洞（未授权访问漏洞）验证工具
"""

#引入依赖的包和库文件
import os
import sys
import socket
import logging


#全局配置设置
logging.basicConfig(level=logging.INFO, format="%(message)s")
socket.setdefaulttimeout(3)


#全局变量
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#全局函数：
def str2Binary(content):
    """将文本流转换成二进制流"""
    return content.replace(' ', '').replace('\n', '').decode('hex')


def rsyncCheck(ip, port):
    """执行端口预检查"""
    global client
    try:
        client.connect((ip, port))
    except Exception as reason:
        logging.error("[-] 访问失败：{}".format(reason))
        return False
    helloString = "405253594e43443a2033312e300a"
    try:
        client.send(str2Binary(helloString))
        hellodata = client.recv(1024)
    except Exception as reason:
        logging.error("[-] 通信失败：{}}".format(reason))
        return False
    if hellodata.find("@RSYNCD") >= 0:
        try:
            client.send(str2Binary("0a"))
        except Exception as reason:
            logging.error("[-] 访问失败：{}}".format(reason))
            return False
        while True:
            try:
                data = client.recv(1024)
            except Exception as reason:
                logging.error("[-] 通信失败：{}}".format(reason))
            if data == "":
                break
            else:
                if str(data).find("@RSYNCD: EXIT") >= 0:
                    logging.info("[*] 发现漏洞！")
                    return True
    return False


if __name__ == "__main__":
    ip = sys.argv[1]
    try:
        port = sys.argv[2]
    except Exception as reason:
        port = 873
        logging.error("[-] 端口未输入，按照873默认端口进行")
    try:
        port = int(port)
    except Exception as reason:
        logging.error("[-] 端口输入错误，按照873默认端口进行")
        port = 873
    if not rsyncCheck(ip, port):
        logging.info("[+] 测试安全！")