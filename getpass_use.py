#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
常用模块：
os,sys,string,psutil,shutil,random,getpass,time

"""
import getpass

username = input("please input your username:")
password = getpass.getpass("please input your password：")

if username == 'tom' and password == '123':
    print("login successful")
else:
    print("login incorrect")
