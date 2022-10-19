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
    def __init__(self,b) -> None: # __init__ 생성자임
        self.b = b
        self.menu = ["바나나","사과", "망고"]
        
    def print_menu(self):
        print("### 과일 ###")
        print("*"*30)
        a=1
        b = self.b 
        menu = self.menu
        for i in menu:
            print(f"{a} 번 과일 : {i}")
            a+=1
        print("*"*30)
        for i in menu:
            if b == "바" and i == "바나나":
                print(f"검색한 과일 : {i}")
            elif b == "사" and i == "사과":
                print(f"검색한 과일 : {i}")
            elif b == "망" and i == "망고":
                print(f"검색한 과일 : {i}")
        """if b == "바":
            print(f"검색한 과일 : {menu[0]}")
        elif b == "사":
            print(f"검색한 과일 : {menu[1]}")
        elif b == "망":
            print(f"검색한 과일 : {menu[2]}")"""

        print("*"*30)

    @staticmethod ##외부에 노출되는것이 스테틱
    def main():
        b = input("과일 첫글자 : ")
        fruits = Fruits(b) #인스턴스 = 생성자
        fruits.print_menu()

Fruits.main()


