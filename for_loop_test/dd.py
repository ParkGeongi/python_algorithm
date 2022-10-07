import random
class Solution:
    def solution(self):
        unit = ['1','2','3','4','5']
        dc = {}
        for i in unit:
            rand = random.randint(1,100)
            dc[i] = rand
        
        for k,v in dc.items():
            print(f'{k} : {v}')

        return
if __name__ == "__main__":
    solution = Solution()
    solution.solution()