import random

class Solution:
    def solution(self):
        keys = ['1st','2nd','3rd','4th','5th']
        dc={}
        '''randnumber = random.randint(1,11)
        randnumber2 = random.randint(1,11)
        randnumber3 = random.randint(1,11)
        randnumber4 = random.randint(1,11)
        randnumber5 = random.randint(1,11) '''
        print('### 버블정렬 ###')
        print('*'*30)
        for i in keys:
            dc[i] = random.randint(1,100)

        for k,v in dc.items():
            print(f' {k} : {v} ')
        
        print('*'*30)
        
if __name__ == "__main__":

    solution = Solution()
    solution.solution()

    