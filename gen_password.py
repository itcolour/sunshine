#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import string
import random

ch1 = string.ascii_letters + string.digits
str1 = ''

for i in range(8):
    str1 = str1 + random.choice(ch1)

print(str1)