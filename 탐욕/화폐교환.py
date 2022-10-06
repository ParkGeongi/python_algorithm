
class Solution:
   def solution(self, money):
      title = " ### 화폐교환 ###"
      aster = "*"*30
      answer = f"요청금액 : {money} 원"
      answer2 = int(money / 50000)
      answer3 = int((money % 50000) / 10000)
      answer4 = int((money % 10000) /5000 )
      answer5 = int((money % 5000)  / 1000)
      answer6 = int((money % 1000)  / 500)
      answer7 = int((money % 500)  / 100)
      answer8 = int((money % 100)  / 50)
      answer9 = int((money % 50)  / 10)
      
      
      return (
       f'{title} \n {aster} \n {answer} \n {aster}\n '
       f'5만원 : {answer2}매 \n '
       f'1만원 : {answer3}매 \n '
       f'5천원 : {answer4}매 \n '
       f'1천원 : {answer5}매 \n '
       f'5백원 : {answer6}매 \n '
       f'1백원 : {answer7}매 \n ' 
       f'5십원 : {answer8}매 \n ' 
       f'1십원 : {answer9}매'
   )    
   
if __name__=="__main__":
   solution = Solution()
   money = int(input("화폐교환할 금액입력: "))
   print(solution.solution(money))

