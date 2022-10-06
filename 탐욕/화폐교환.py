class Solution:
   def solution(self, money):
      title = " ### 화폐교환 ###"
      aster = "*"*30
      answer = f"요청금액 : {money} 원"
      print (f'{title} \n {aster} \n {answer} \n {aster}')

      unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   
      
      for i in unit:
         count = money // i
         money = money % i
         print(f'{i}원: {count}매')



      return (
       ''' #f'{title} \n {aster} \n {answer} \n {aster}\n '
       f'5만원 : {answer2}매 \n '
       f'1만원 : {answer3}매 \n '
       f'5천원 : {answer4}매 \n '
       f'1천원 : {answer5}매 \n '
       f'5백원 : {answer6}매 \n '
       f'1백원 : {answer7}매 \n ' 
       f'5십원 : {answer8}매 \n ' 
       f'1십원 : {answer9}매'    '''
   )    

if __name__=="__main__":
   solution = Solution()
   money = int(input("화폐교환할 금액입력: "))
   solution.solution(money)

 #round curl square ankle brcae (){}[] <>
 # quote ' " 
 