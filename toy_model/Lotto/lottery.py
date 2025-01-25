#로또 모델 만들기
from random import randint


# 참여 횟수에 제한이 없어서, 한 사람이 한 회차에 여러 번 참여할 수도 있음.
# 고를 수 있는 번호는 1부터 45까지, 참여할 때마다 서로 다른 번호 6개를 선택

# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원

# 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑기
def generate_numbers(n):
    number_list = []
    while len(number_list) < n:
        num = randint(1, 45)
        if num not in number_list:
            number_list.append(num)
    return number_list

# def generate_numbers(n):
#     number_set = set()
#     while len(number_set) < 6:
#         number_set.add(randint(1, 45))
#     return number_set


# 6개의 일반 로또번호와 1개의 보너스 번호 추출
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# def draw_winning_numbers():
#     general_num = generate_numbers(6)
#     general_num.sort()

#     bonus_num = generate_numbers(1)[0]
#     # bonus_num이 general_num에 포함되면 새로운 번호를 생성
#     while bonus_num in general_num:
#         bonus_num = generate_numbers(1)[0]
    
#     return general_num + [bonus_num]
    
#당첨 개수 확인
def count_matching_numbers(numbers, winning_numbers):
    correct_num = 0
    for num in numbers:
        if num in winning_numbers:  # 조건문 추가
            correct_num+=1  # 리스트에 추가
    
    return correct_num

#당첨 금액확인 
def check(numbers, winning_numbers):
    general = winning_numbers[:6]  # 일반 번호 (앞 6개)
    bonus = winning_numbers[6:]    # 보너스 번호 (1개)
    match_num = count_matching_numbers(numbers, general)  # 일반 번호 매칭 수 계산

    if match_num == 6:
        return 1000000000  # 1등
    elif match_num == 5:
        # 보너스 번호 매칭 여부 확인
        if count_matching_numbers(numbers, bonus) == 1:
            return 50000000  # 2등
        else:
            return 1000000  # 3등
    elif match_num == 4:
        return 50000  # 4등
    elif match_num == 3:
        return 5000  # 5등
    else:
        return 0 # 낙첨
