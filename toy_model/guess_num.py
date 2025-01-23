import random

NUM = random.randint(1,20)


def guess_num(NUM) :
    for i in range(4):
        input_num = int(input(f"기회가 {4-i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
        if input_num == NUM: 
            return f"축하합니다. {i+1}번만에 숫자를 맞히셨습니다."
        elif input_num < NUM:
            print("Up")
        else:
            print("Down")
    return f"아쉽습니다. 정답은 {NUM}였습니다."


result = guess_num(NUM)
print(result)