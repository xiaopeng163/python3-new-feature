"""
pep3134.py
Created by Peng Xiao on 2018-07-23. xiaoquwl@gmail.com
"""

def compute(a, b):
    try:
        a/b
    except Exception as e:
        log(e)


def log(error):
    with open('logfile.txt', 'w') as f:  # oops, forgot the 'w'
        f.write(str(error))



if __name__ == "__main__":
    compute(1, 0)