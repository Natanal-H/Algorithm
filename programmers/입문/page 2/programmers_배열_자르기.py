# 프로그래머스 문제 풀이 - 배열 자르기 (120833)

## 문제 정보
# **문제 이름**: 배열 자르기
# **문제 번호**: 120833
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120833)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
