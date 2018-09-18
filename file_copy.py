#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
思路：
1.定义一个函数，名为copyFile()
2.定义两个变量，接收用户输入的源文件路径和目标文件路径
3.定义每次读取文件的大小buf_size
4.分别打开两个文件，源文件使用只读的模式打开，目标文件使用写的模式打开
5.把每次从源文件读取的buf_size大小的文件，写入目标文件
6.定义__name__变量，如果测试使用直接调用此函数

"""
def copyFile():
    source = input("请输入你需要备份的文件路径：")
    des = input("请输入你备份的目标文件路径：")
    buf_size = 4096

    d_file = open(des,'w')
    size = open(source,'r').read(buf_size)
    d_file.write(size)

if __name__ == '__main__':
    copyFile()
