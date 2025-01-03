# 프로그래머스 문제 풀이 - 문자열 바꿔서 찾기 (181864)

## 문제 정보
# **문제 이름**: 문자열 바꿔서 찾기
# **문제 번호**: 181864
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181864)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. 
# myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

## 코드
def solution(myString, pat):
    return int(pat in myString.replace('A','b').replace('B','a').upper())
