# 기본 템플릿
```
import sys
sys.setrecursionlimit(int(1e6))   # 재귀 깊이 한도 해제
input = sys.stdin.readline

from collections import deque
```

</br>


# 코딩테스트 TIP  

### 1.입력 받기
#### 1) input() 함수
- 입력 예제: 7
- 코드
  - ```data = input()```

#### 2) split() + map() 함수
- 입력 예제: 7 6
- 코드
  - ```N, M = map(int, input().split())```
- 코드 설명
  - ```input()```으로 한 줄의 입력을 받아와서, 공백(default)을 기준으로 분리한다.
  - 이때 ```split()```을 하면 리스트가 생성된다.
  - 리스트의 개별 원소에 각각 함수를 적용하기 위해 ```map()```함수를 사용한다.
 
#### 3) sys.stdin.readline().strip()
- 입력 예제: 2 </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7 6 5 </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 9 8 1
- 코드
    ```
    import sys
       input = sys.stdin.readline
       N = int(input())
       for _ in range(N):
           a, b, c = map(int, input().rstrip().split())
    ```
- 코드 설명
  - ```sys.stdin.readline```은 ```input()```보다 입력을 빠르게 받는다. 그러므로 앞으로 계속 사용할 것.
  - **'여러 줄을 입력 받을 때'** for문을 통해 입력을 받는다. 즉 ```sys.stdin.readline```를 여러 번 사용하는 것이다.
  - ```sys.stdin.readline()```은 "줄 바꿈" 혹은 "공백"도 입력으로 받기 때문에, ```strip()```을 공백을 제거해준다.
    - strip(): 양쪽 공백 제거
    - rstrip(): 오른쪽 공백 제거
    - lstrip(): 왼쪽 공백 제거

</br>

### 2.출력 하기

</br>

### 3.아스키코드

</br>

### 4.RecursionError

</br>

### 5.Stack

</br>

### 6.Deque

</br>

### 7.DFS(Depth First Search)

</br>

### 8.BFS(Breadth First Search)


</br>


### 9.기타
zfill()

