
from colorsys import rgb_to_yiq
from lib2to3.pytree import type_repr


class Grade(object):
    def __init__(self, name, ko, en, ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total = 0
        self.avg = 0
        self.grade = ""

    def get_total(self):
        self.total = self.ko + self.en + self.ma
        return self.total


    def get_avg(self):
        total = self.get_total()
        self.avg = total / 3
        return self.avg

    def get_grade(self):
        avg = self.avg
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        else : grade = "F"
        self.grade = grade
        return grade
    
    def print_info(self):
        print("이름 국어 영어 수학 총점 평균 등급")
        print(f"{self.name} {self.ko} {self.en} {self.ma} {self.get_total()} {round(self.get_avg(),2)} {self.get_grade()}")
    
    def delete(self, a, ls):
        pass
    
    @staticmethod
    def get_grades(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def new_grade():
        name = input("이름 : ")
        ko = int(input("국어 : "))
        en = int(input("영어 : "))
        ma = int(input("수학 : "))
        return Grade(name,ko,en,ma)

    @staticmethod
    def print_menu():
        print("*"*30)
        print("1. 성적 입력")
        print("2. 성적 출력")
        print("3. 성적 삭제")
        print("4. 종료")
        menu = int(input("몇번? "))
        return menu
    
    @staticmethod
    def main():
        ls =[]
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print("### 등록 ###")
                grade = Grade.new_grade()
                ls.append(grade)
            elif menu == 2:
                print("### 출력 ###")
                print("*"*30)
                Grade.get_grades(ls)
            elif menu == 3:
                print("### 삭제 ###") 
                a=input("뭐 지울래")
                ls = grade.delete(a, ls)
                
            elif menu == 4:
                print("### 종료 ###")
                break
Grade.main()

