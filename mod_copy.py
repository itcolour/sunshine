#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
思路：
1.导入shutil模块
2.shutil模块，可以实现对文件和目录的备份操作
3.定义两个变量s_file和d_file，接收用户的输入
4.调用shutil.copy()方法可以实现对文件的备份，shutil.copytree()方法可以实现对目录的备份
5.使用pycharm直接运行

"""
import shutil

s_file = input("请输入需要备份的源文件路径：")
d_file = input("请输入需要备份的目标文件的路径：")

shutil.copy(s_file,d_file)