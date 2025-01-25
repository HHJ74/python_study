from random import randint

#0~9까지 숫자중 3개를 순서대로 뽑아서 저장
#0~9까지 사용자에게 3개를 차근차근 받음
#컴퓨터가 뽑은 숫자와 사용자가 뽑은 숫자가 위치와 크기가 같은 경우 1S, 숫자만 같은 경우 1B
#컴퓨터가 뽑은 값은 유지한채 사용자는 3S가 될떄까지 게임 진행

#3개 숫자 뽑기
def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        numbers.append(randint(0,9))
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    return numbers

# 유저에게 숫자 받기
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i=1
    new_guess = []
    while i<4:
        num = int(input(f"{i}번째 숫자를 입력하세요: "))
        if num >=0 and num <10: 
            if num not in new_guess:
                i+=1
                new_guess.append(num)
            else:
                print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    
    return new_guess

#점수 계산
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for num in guesses:
        if num in solution:
            if guesses.index(num) == solution.index(num):
                strike_count += 1
            else:
                ball_count += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()

tries = 0
guess = []

while True:
    tries += 1
    guess = take_guess()
    strike_count, ball_count = get_score(guess, ANSWER)
    
    if strike_count == 3:
        print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")
        break
    else:
        print(f"{strike_count}S {ball_count}B")
    
