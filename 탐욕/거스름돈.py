class Solution:
   def solution(self, money):
      title = " ### 화폐교환 ###"
      aster = "*"*30
      answer = f"요청금액 : {money} 원"     
      unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   
      dc = {}
      print (f'{title} \n {aster} \n {answer}')
      for i in unit:
         cnt = money // i
         dc[i] = cnt
         money = money % i
      for k,v in dc.items():
         print(f' {k}원 : {v}매')
      print(f' {aster}')  
      return 

if __name__=="__main__":
   solution = Solution()
   money = int(input("화폐교환할 금액입력: "))
   solution.solution(money)

 #round curl square ankle brcae (){}[] <>
 # quote ' " 

