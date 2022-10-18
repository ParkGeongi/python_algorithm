class Solution:
    def solution(self,name, cm, kg):
        m = cm / 100
        bmi = cm / (m*m)

        if bmi >= 35:
            biman = "고도비만"

        elif bmi >= 30:
            biman = "중도 비만"
            
        elif bmi >= 25:
            biman = "경도 비만"

        elif bmi >= 23:
            biman = "과체중"

        elif bmi >= 18.5:
            biman = "정상"

        else:
            biman = "저체중"
        
        values = f"{name} {cm} {kg} {biman}"
        title = " ### 비만도 계산 ### "
        aster = "*"*30
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        return f"{title} \n {aster} \n {schema} \n {values} \n {aster}"

if __name__ == "__main__":
    solution = Solution()
    name = input("이름 : ")
    cm = int(input("키 : "))
    kg = int(input("몸무게 : "))
    print(solution.solution(name,cm,kg))

    
