while True:
    try:
        print(input())
    except EOFError:    # EOF: End Of File. 즉 입력값이 더 이상 없는 상황을 뜻함 => 그런데 이때 EOFError를 사용하기 위해서는 sys.stdin.readline()을 사용해서는 안됨. input()을 사용해야 함.
        break           # 입력값이 더 이상 없으면 멈춰라.
