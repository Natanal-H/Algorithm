# 프로그래머스 문제 풀이 - 주사위의 개수 (120845)

## 문제 정보
# **문제 이름**: 주사위의 개수
# **문제 번호**: 120845
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120845)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 
# 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)
