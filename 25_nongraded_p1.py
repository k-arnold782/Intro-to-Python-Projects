# Lecture 25, nongraded assignment #P1
import sys

def count_substr(str1, str2):
    count = 0
    len2 = len(str2)
    for idx in range(len(str1) - len2 + 1):
        if str1[idx:idx+len2] == str2:
            count += 1
    return count

# Command line usage: python 25_nongraded_p1.py banana ana
if __name__ == '__main__':
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(count_substr(str1, str2))
