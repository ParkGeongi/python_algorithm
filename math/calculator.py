class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def execute(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            result = "잘못된 연산입니다."

        return result

    def print_info(self):
        result = self.execute()
        print(f"{self.num1} {self.op} {self.num2} = {result}")
    @staticmethod
    def get_calculators(ls):
        for i in ls:
            i.print_info()


    @staticmethod
    def new_calculator():
        num1 = int(input("숫자 : "))
        op = input("+ - * / % : ")
        num2 = int(input("숫자 : "))
        return Calculator(num1, op, num2)

    @staticmethod
    def print_menu():
        print("1.calculator 등록")
        print("2.calculator 출력")
        print("3.calculator 삭제")
        print("0.calculator 종료")
        menu = int(input("몇번 ? "))
        return menu

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 0:
                print(" ### 종료 ### ")
                break
            elif menu == 1:
                print(" ### 등록 ### ")
                calculator = Calculator.new_calculator()
                ls.append(calculator)
            elif menu == 2:
                print(" ### 출력 ### ")
                Calculator.get_calculators(ls)

            elif menu == 3:
                print(" ### 삭제 ### ")
            else:
                print("")
Calculator.main()