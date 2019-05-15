# random 숫자 출력을 위한 모듈 호출
from random import randint
print("★★★★★★★★★★ 김상헌 짱짱맨 ★★★★★★★★★★★★★★★★★★★★★★★★★★")
print("★★★★★★★★★★ 야구 게임 규칙 ★★★★★★★★★★★★★★★★★★★★★★★★★")
print("★★★★★★★★★★ 예린아 사랑해 ★★★★★★★★★★★★★★★★★★★★★★★★★★")
print("★★★★★★★★★★ 1.컴퓨터는 0 ~ 9 사이의 랜덤한 수를 가집니다.★★★★★★★★★★")
print("★★★★★★★★★★ 2.사용자는 3가지의 숫자를 골라줍니다.(0 ~ 9)★★★★★★★★★★")
print("★★★★★★★★★★ 3.컴퓨터의 숫자 위치와 값이 동일하면 스트라이크★★★★★★★★★★")
print("★★★★★★★★★★ 4.컴퓨터의 숫자 값은 같지만 위치가 다르면 볼 ★★★★★★★★★★")
print("★★★★★★★★★★ 5.컴퓨터의 숫자 값은 같지만 위치가 다르면 볼 ★★★★★★★★★★")
print("★★★★★★★★★★ 6.3 Strike를 최대한 빨리 맞추면 되는 게임! ★★★★★★★★★★")
print("★★★★★★★★★★ 7. 당신의 두뇌를 테스트 해줍니다.!!!!!!!!! ★★★★★★★★★★")

print("★★★★★★★★★★★★ 시작을 원한다면 엔터 쳐주세요 ★★★★★★★★★★★★")

trash = input("")
# 컴퓨터의 random값을 저장할 numbers 배열과 사용자 입력 받을 answers를 정의
numbers = []
answers = []

# strike와 ball 값을 0으로 초기화
strike = 0
ball = 0

# i 값을 0으로 초기화 한뒤에 numbers 배열에 랜덤한 수 3개를 넣어준다.
i = 0
while i < 3:
    numbers.append(randint(0, 9))
    i += 1

# 비교할 변수 j와 index값을 0으로 초기화 해준뒤에 비교를 시작하는데,
# 배열중에 중복된게 있다면 새로 랜덤한 값을 넣어준다. 다른 값이 나오면,
# 비교대상 변수 j를 늘려준다. 반복해서 중복 값을 제거해준다.
i = 0
while i < 3:
    j = 0
    while j < i:
        if numbers[i] == numbers[j]:
            numbers[i] = randint(0, 9)
        else:
            j += 1
    i += 1

chance = 0
# 안내 멘트를 출력해준다.
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다")
while strike < 3:
    chance += 1
    strike = 0
    ball = 0
    print("0에서 9사이의 세 수를 하나씩 차례대로 입력하세요")

    # index 변수를 0으로초기화 해주고, count 변수로 몇개의 수를 입력하는지 알려준다.
    i = 0
    count = 1
    while count <= 3:
        answers.insert(i, int(input("%d번째 수를 입력하세요 : " % count)))
        # 수를 입력했는데, 0~9 사이의 수가 아니라면 맞을때까지 입력시킨다.
        if answers[i] > 9 or answers[i] < 0:
            while answers[i] > 9 or answers[i] < 0:
                del answers[i]
                answers.insert(j, int(input("%d번째 수가 범위를 벗어났습니다. 다시 입력하세요 : " % count)))
        # 입력값이 2개가 넘어가면 j값을 1로 주어 이전 값과 중복을 체크한다.
        # 중복되었다면 입력된 배열은 삭제해주고 새로 입력 받게한다.
        # 중복이 안되어있는걸 확인하면 반복문에서 나가서 count와 i값을 올려 새로운 값을 입력받는다.
        if i >= 1:
            j = 1
            while j <= len(answers) :
                if answers[j-1] == answers[j]:
                    del answers[i]
                    answers.insert(j, int(input("%d번째 수가 중복되었습니다 다시 입력하세요 : " % count)))
                else:
                    break

        count += 1
        i += 1
    # index변수와 비교대상변수 j를 0으로 초기화 해준다.
    i = 0
    j = 0
    while i < 3:
        if numbers[i] == answers[i]:
            strike += 1
        else:
            j = 1
            while j < 3:
                if numbers[i] == answers[j]:
                    ball += 1
                    j += 5
                else:
                    j += 1
        i += 1
    print("%d Strike %d Ball " %(strike, ball))

print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % chance)

input("")
