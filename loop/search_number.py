'''
랜덤숫자 10개를 뽑아서 
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발하시오.
예 [12 23 48   ......]
사용자의 값이 12인 경우
12 48만 되도록 한다.
'''
from random_list import Random_list
class Search_number:
    def __init__(self,a) -> None:
        self.a = int(a)
        rl = Random_list()
        self.list_a = rl.get_extract_random(1,100,10)

    def print(self):
        list_a = self.list_a
        a= self.a
        print(list_a)
        for i in list_a:      
            if i % a ==0:
                print(f"{a}의 배수 :{i}")
            else:
                print(i)
                
    @staticmethod
    def main():
        a = input("값 :")

        sn = Search_number(a)
        sn.print()

Search_number.main()