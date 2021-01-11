# 如何引入 a.py

import sys
sys.path.append('..')
from run import a
# import run.a

a.aaa()

def multi(a, b):
  print(a*b)
  return a * b