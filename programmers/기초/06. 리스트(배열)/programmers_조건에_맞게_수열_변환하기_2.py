# 프로그래머스 문제 풀이 - 조건에 맞게 수열 변환하기 2 (181881)

## 문제 정보
# **문제 이름**: 조건에 맞게 수열 변환하기 2
# **문제 번호**: 181881
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181881)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.
# 이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, arr(x) = arr(x + 1)인 x가 항상 존재합니다. 
# 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.
# 단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.

## 코드
def solution(arr):
    count = 0
    while True :
        a = []
        
        for v in arr :
            if v >= 50 and v % 2 == 0:
                a.append(v // 2)
            elif v < 50 and v % 2:
                a.append(v * 2 + 1)
            else :
                a.append(v)
        
        if a == arr :
            return count
        else :
            arr = a        
       
        count += 1
