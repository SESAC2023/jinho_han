while True:
    try:
        print(input())
    except EOFError:    # EOF: End Of File. 즉 입력값이 더 이상 없는 상황을 뜻함
        break           # 입력값이 더 이상 없으면 멈춰라.
