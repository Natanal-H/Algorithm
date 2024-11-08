# 프로그래머스 문제 풀이 - 배열 두 배 만들기 (120809)

## 문제 정보
# **문제 이름**: 배열 두 배 만들기
# **문제 번호**: 120809
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120809)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(numbers):
    return [n * 2 for n in numbers]
