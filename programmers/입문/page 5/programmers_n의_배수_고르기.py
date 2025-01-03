# 프로그래머스 문제 풀이 - n의 배수 고르기 (120905)

## 문제 정보
# **문제 이름**: n의 배수 고르기
# **문제 번호**: 120905
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120905)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(n, numlist):
    return [num for num in numlist if num % n == 0]
