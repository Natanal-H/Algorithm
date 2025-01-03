# 프로그래머스 문제 풀이 - 특정한 문자를 대문자로 바꾸기 (181873)

## 문제 정보
# **문제 이름**: 특정한 문자를 대문자로 바꾸기
# **문제 번호**: 181873
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181873)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, 
# my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())
