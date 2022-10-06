class Solution:
    
     def solution(slef, a, b, c):
        title="###성적표###"
        answer = a + b + c
        
        return f"{title} \n총점 : {answer}"

if __name__=="__main__":
        solution = Solution()

        a= int(input("국어 성적: "))
        b= int(input("수학 성적: "))
        c= int(input("영어 성적: "))

        print(solution.solution(a,b,c))