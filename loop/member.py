
"""
아이디 비밀번호 이름 를 받아서
회원가입 목록 탈퇴하는 프로그램을 개발하시오
"""


class Member(object):

    def __init__(self,id,pw,name):
        self.id = id
        self.pw = pw
        self.name = name

    def print(self):
        pass

    def print_member(self):
        print(f"{self.id} {self.pw} {self.name}")

    def del_member(self):
        pass

    @staticmethod
    def get_members(ls):
        [i.print_member() for i in ls]

    @staticmethod
    def new_id_pw_name():
        return Member(input("아이디: "), input("패스워드: "), input("이름: "))
    @staticmethod
    def print_menu():
        print("1. 가입")
        print("2. 목록 출력")
        print("3. 삭제")
        print("0. 종료")

        menu = int(input("몇번? "))
        return menu

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print(" ### 가입 ###")
                member = Member.new_id_pw_name()
                ls.append(member)
            elif menu == 2:
                print(" ### 목록 ###")
                print("id password 이름")
                Member.get_members(ls)
            elif menu == 3:
                print(" ### 삭제 ###")
                member = Member.new_id_pw_name()
                member.del_member()

            elif menu == 0:
                print(" ### 종료 ###")
                break
            else:
                print("*"*30)
                print("맞는 번호를 치세요")

Member.main()