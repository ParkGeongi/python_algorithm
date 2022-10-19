"""
이름 주민번호(950101 - 1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25 (만)
성별: 남성
주소: 서울
********************************
"""

class Intro(object):
    def __init__(self, name,id, home) -> None:
        self.name = name
        self.id = id
        self.home = home
        self.age = 0
        self.gender = ""
    
    def set_age(self):
        id = self.id

        if id[7]  == "1": # gender check 주민 번호 (id) 7번 째 자리 성별판별번호 인덱스
            self.age = 2022 - 1900 - int(id[0:2]) 
        elif id[7] == "3":
            self.age = 2022 - 2000 - int(id[0:2])
        elif id[7] == "2":
            self.age = 2022 - 1900 - int(id[0:2])
        elif id[7] == "4":
            self.age = 2022 - 2000 - int(id[0:2])
         

    def set_gender(self):
        id = self.id
        if id[7] == "1":
            self.gender = "남"
        elif id[7] == "3":
            self.gender = "남"
        elif id[7] == "2":
            self.gender = "여"
        elif id[7] == "4":
            self.gender ="여"    


    def print_intro(self):

        print(self.id[0:2])

        print(" #### 성적표 ###")
        print("*"* 30)
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"성별 : {self.gender}")
        print(f"주소 : {self.home}")
        print("*"* 30)

    @staticmethod
    def main():

        name = input("이름 : ")
        id = input("주민번호 : ")
        home = input("주소 : ")
        intro2 = Intro(name,id,home)
        intro2.set_age()
        intro2.set_gender()
        intro2.print_intro()


Intro.main()

