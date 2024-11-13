# 프로그래머스 문제 풀이 - [PCCE 기출문제] 8번 / 닉네임 규칙 (340200)

## 문제 정보
# **문제 이름**: [PCCE 기출문제] 8번 / 닉네임 규칙
# **문제 번호**: 340200
# **문제 레벨**: 0
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340200)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 온라인 서비스를 이용하기 위해서 닉네임이 필요합니다. 이때 닉네임이 될 수 있는 조건은 다음과 같습니다.
# 닉네임의 길이가 4자 이상 8자 이하여야합니다.
# 닉네임에는 소문자 l과w, 대문자 O와 W를 사용할 수 없습니다.
# 이외의 영어 대소문자와 숫자는 모두 사용이 가능합니다.
#
# 주어진 solution 함수는 사용할 수 없는 닉네임 nickname을 받아 사용할 수 있는 닉네임으로 바꿔주는 함수입니다. 
# 이때 닉네임을 변경하는 규칙은 다음과 같으며 첫 번째 규칙부터 순서대로 적용합니다.
# 소문자 l을 대문자 I로 변경합니다.
# 소문자 w를 두 개의 소문자 v, 즉 vv로 변경합니다.
# 대문자 W를 두 개의 대문자 V, 즉 VV로 변경합니다.
# 대문자 O를 숫자 0으로 변경합니다.
# 수정된 닉네임의 길이가 4 미만일 경우 뒤에 소문자 o를 길이가 4가 될때까지 이어붙입니다.
# 수정된 닉네임의 길이가 8보다 클 경우 8번째 문자까지만 사용합니다.

## 코드
def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer
