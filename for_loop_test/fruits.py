"""
과일판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력된 값은 없다.
출력되는 결과는 다음과 같다.
### 과일가격표 ###
********************************
1번과일: 바나나
2번과일: 사과
3번과일: 망고
********************************
"""

class Fruits(object):

    def __init__(self) -> None:
        self.menu = ["바나나", "사과", "망고"]
        pass
    def print_fruits(self):
        print("과일번호표")
        print("*"*30)
        unit = ["사과","바나나","망고"]
        a=1
        for i in self.menu:
            print(f"{a}번과일: {i}")
            a+=1
        print("*"*30)

    @staticmethod
    def main():
        fruits = Fruits() #인스턴스를 만들어라
        fruits.print_fruits()
Fruits.main()       
