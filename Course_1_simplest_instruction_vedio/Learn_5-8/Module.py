# 同一文件夹下的python文件可以直接import
import sys
import os
sys.path.append('/Users/apple/Documents/python/venv/')  # 这两句话可以加入路径

import hello
hello.print_hello()

from hello import print_hello

from folder import file
