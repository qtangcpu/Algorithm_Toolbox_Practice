# Uses python3
import sys

def get_change(m):
    a = [10,5,1]
    m = m//10 + (m%10)//5 + ((m%10)%5)//1
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


