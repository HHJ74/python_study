
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
        
#함수 호출 후 반복 
with open('vocabulary.txt', 'a') as f:
    for line in make_vocabulary():
        f.write(line)