data = input()
if type(data) == str:
    print(ord(data))       # ord(문자열): ord는 문자를 입력값으로 받으며, 문자의 아스키코드를 출력해준다. (소문자, 대문자 모두)
else:
    print(chr(int(data)))  # chr(정수): chr은 정수를 입력값으로 받으며, 숫자의 아스키코드를 출력해준다.
