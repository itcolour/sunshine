#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

prompt = """(1)水果
(2)纸巾
(3)干果
(4)电器
(5)退出
请选择：[1|2|3|4|5]:"""

while True:
    print("请选择如下菜单：")
    choice = int(input(prompt))

    if choice == 1:
        print("你选择了水果，请支付xx钱")
    elif choice == 2:
        print("你选择了纸巾，请支付xx钱")
    elif choice == 3:
        print("你选择了干果，请支付xx钱")
    elif choice == 4:
        print("你选择了电器，请支付xx钱")
    elif choice == 5:
        sys.exit()