class User:

    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

        User.count += 1


    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다")

    def login(self, email, password):
        if self.email == email and self.password == password:
            self.say_hello()
        else:
            print("로그인이 실패하였습니다. 없는 아이디이거나 잘못된 비밀번호입니다.")   

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"
    
    # 팔로우
    def follow(self, another_user):
        self.following_list.append(another_user)  # self.following_list에 another_user 추가
        another_user.followers_list.append(self)  # another_user.followers_list에 self 추가
        
    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        return len(self.followers_list)
    
    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다")


    @staticmethod
    def valid_email(email):
        return "@" in email




user1 = User("정혜현","qwe123@naver.com", "12345")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")

User.print_number_of_users()