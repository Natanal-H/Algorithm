# 프로그래머스 문제 풀이 - 치킨 쿠폰 (120884)

## 문제 정보
# **문제 이름**: 치킨 쿠폰
# **문제 번호**: 120884
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120884)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(chicken):
    answer = 0
    
    while chicken >= 10 :
        answer += chicken // 10
        chicken = chicken % 10 + chicken // 10
    
    return answer
