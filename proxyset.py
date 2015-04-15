#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import requests


# get the port with replace string
def getport(str_in):
    means = {"v": "3",
             "m": "4",
             "a": "2",
             "l": "9",
             "q": "0",
             "b": "5",
             "i": "7",
             "w": "6",
             "r": "8",
             "c": "1",
             "+": ""}
    for key, value in means.iteritems():
        str_in = str_in.replace(key, value)
    return str_in


# return ip:port
def ip_with_port(page):
    ret_list = []
    req = requests.get('http://www.cnproxy.com/proxy' + str(page) + '.html')
    if req.status_code == 200:
        table = req.content.split('</table>\n<table>')[1].split('</table>')[0].split(' Country/Area</td></tr>')[1].strip()
        alltr = table.split('<tr><td>')
        for tr in alltr:
            row = tr.split(')</SCRIPT></td>')[0].split('<SCRIPT type=text/javascript>document.write(":"+')
            if len(row) == 2:
                ip = row[0]
                port = getport(row[1])
                ret_list.append(str(ip) + ':' + str(port))
    return ret_list


# test proxy is alive
def is_alive(proxy):
    try:
        req = requests.get('http://www.bing.com', timeout=3, proxies={'http': proxy})
        if req.status_code == 200:
            print proxy, ':yes'
            return True
    except:
        pass


if __name__ == "__main__":
    proxy = []
    alive = []
    for i in range(1, 11, 1):
        proxy.extend(ip_with_port(i))

    print proxy
    for pro in proxy:
        if is_alive(pro):
            alive.append(pro)
    print alive