# 프로그래머스 문제 풀이 - 문자열 여러 번 뒤집기 (181913)

## 문제 정보
# **문제 이름**: 문자열 여러 번 뒤집기
# **문제 번호**: 181913
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181913)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
# queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
# my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, queries):
    for s, e in queries :        
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string
