import random

#단어장 생성 함수 정의
def make_vocabulary():
    while True:
        english = input("영어 단어를 입력하세요 (종료하려면 'q'를 입력하세요): ")
        if english == "q":
            break
        korean = input("한국어 뜻을 입력하세요 (종료하려면 'q'를 입력하세요): ")
        if korean == "q":
            break
        yield f"{english} : {korean}\n" #return의 경우 함수가 종료됨. 때문에 반복사용을 위해서는 재호출이 필요한데 yield의 경우는 값을 반환한 뒤에도 함수의 상태를 유지하여 중단된 시점부터 다시 실행이 가능하게 함
        

#단어 문제 맞추기 함수 정의 (순서대로)
def guess_vocabulary(vocab_list):
    for line in vocab_list:
        word = line.strip().split(":") # 공백 제거 및 ":" 을 기준으로 나누기 
        question, answer = word[1].strip(), word[0].strip() #질문과 답 할당
        user_input = input(f"{question}: ").strip()
        if user_input.lower() == answer.lower():  # 대소문자 구분 없이 정답 확인
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {answer}입니다.")


#단어 문제 맞추기 고급(랜덤)
def random_voca_quiz(vocab_list):
    while True:
        line = random.randint(0, len(vocab_list) - 1)
        word = vocab_list[line].strip().split(":") # 공백 제거 및 ":" 을 기준으로 나누기 

        question, answer = word[1].strip(), word[0].strip() #질문과 답 할당
        user_input = input(f"{question}: ").strip()

        if user_input.lower() == "q":  # 사용자가 'q'를 입력하면 종료
                print("퀴즈를 종료합니다!")
                break
        elif user_input.lower() == answer.lower():  # 대소문자 구분 없이 정답 확인
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {answer}입니다.")



# #문제 맞추기 함수 호출
# with open('vocabulary.txt', 'r') as vocab_list:
#     guess_vocabulary(vocab_list)

#랜점 문제 맞추기 함수 호출
with open('vocabulary.txt', 'r') as vocab_list:
    vocab_list = vocab_list.readlines()  # 파일 내용을 한 줄씩 읽어 리스트로 변환. len 을 사용하기 위함
    random_voca_quiz(vocab_list)



# #단어장 생성 함수 호출 후 반복 
# with open('vocabulary.txt', 'a') as vocab_list:
#     for line in make_vocabulary():
#         vocab_list.write(line)

