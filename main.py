def sushu():
    x=int(input("请输入一个整数："))
    if x ==2:
        print("输入的x是最小的素数")
    for j in range(2,x):
        if x % j == 0:
            print("输入的x是合数")
            break
        if j == x-1:
            print("输入的x是素数")
            break