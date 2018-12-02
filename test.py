import tensorflow as tf
import numpy as np
import time

if __name__ == '__main__':
    print("aaa")
    nowTime = time.localtime()
    date = time.strftime("%Y-%m-%d %H:%M:%S", nowTime)
    with open('./BOM.txt', 'a') as f:
        f.write("\n" + date)