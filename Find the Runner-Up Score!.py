if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    l1=sorted(arr)
    print(l1[-2])
