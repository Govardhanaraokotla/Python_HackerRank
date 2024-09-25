input_size = int(input())
for _ in range(input_size):
    try:
        numerator, denominator = map(int, input().split())
        print(numerator // denominator)
    except Exception as e:
        print("Error Code:", e)
