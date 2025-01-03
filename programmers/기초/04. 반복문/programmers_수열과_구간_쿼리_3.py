# 프로그래머스 문제 풀이 - 수열과 구간 쿼리 3 (181924)

## 문제 정보
# **문제 이름**: 수열과 구간 쿼리 3
# **문제 번호**: 181924
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181924)
# **풀이 날짜** : 2024-11-05

## 문제 
# 문제 설명 :
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
# queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(arr, queries):
    for a, b in queries :
        arr[a], arr[b] = arr[b], arr[a]
    return arr
