import random
class Solution:
    def solution(self, money):
        unit = [50000,10000,5000,1000,500,100,50,10]
        dc = {}

        for i in unit:
            cnt = money // i
            dc[i] = cnt
            money = money % i           
        

        for k,v in dc.items():
            print(f' {k} 원 : {v}매')
        print("*"*30)
        return 

if __name__ == "__main__":
    solution = Solution()
    print("*"*30)
    money = int(input(' 요청금액 :'))
    solution.solution(money)

