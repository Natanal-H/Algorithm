# ------------------------------------------------------
# 문제 번호 : [1316] 그룹 단어 체커
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1316
# 난이도 : X
# 분류 : 구현, 문자열
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
#
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 코드
N = int(input())
cnt = 0

for n in range(N):
    word = input()
    cnt += 1
    
    for i in range(len(word)-1):
        if word[i] != word[i+1] and word[i+1:].find(word[i]) != -1:
            cnt -= 1
            break   

print(cnt)
