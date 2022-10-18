
class Grade(object):
    def __init__(self, name, ko, en, ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total = 0
        self.avg = 0
        self.grade = ""

    def set_total(self):
        self.total = self.ko + self.en + self.ma

    def set_avg(self):
        self.avg = self.total / 3

    def set_grade(self):
        avg = self.avg
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        else : grade = "F"
        self.grade = grade

    def print_grade(self):
        print("### 성적표 ###")
        print("********************************")
        print("이름 국어 영어 수학 총점 평균 학점")
        print("*******************************")
        print(f"{self.name} {self.ko} {self.en} {self.ma} {self.total} {self.avg} {self.grade}")
        print("********************************")

    @staticmethod
    def main():
        name = input("이름: ")
        ko = int(input("국어: "))
        en = int(input("영어: "))
        ma = int(input("수학: "))
        grade2 = Grade(name, ko, en, ma)
        grade2.set_total()
        grade2.set_avg()
        grade2.set_grade()
        grade2.print_grade()

Grade.main()
    