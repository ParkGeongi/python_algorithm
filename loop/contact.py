"""
이름 전화번호 이메일 주소를 받아서
연락처 입력 출력 삭제하는 프로그램을 개발하시오
단, 인명은 여러명 저장 가능합니다.
"""


class Contact(object):
    def __init__(self, name,phone_num, email, addres) -> None:
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.addres = addres
    @staticmethod
    def delete_contact(self, ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]




    def print(self):
        name = self.name
        phone_num = self.phone_num
        email = self.email
        addres = self.addres
        values = f"{name} {phone_num} {email} {addres}"
        print(values)

    def print_info(self):
        print(f"{self.name} {self.phone_num} {self.email} {self.addres}")

    @staticmethod
    def get_contacts(ls):
       [_.print_info() for _ in ls]



    @staticmethod
    def new_contact():
        name = input("이름을 입력하세요: ")
        phone_num = input("전화번호을 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        addres = input("주소을 입력하세요: ")
        return Contact(name, phone_num, email, addres)

    @staticmethod #화면을 처리하는것은 static
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = int(input("메뉴 선택: "))
        return menu

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 연락처 등록 ###")
                contact = Contact.new_contact()
                ls.append(contact)
            elif menu == 2:
                print(" ### 연락처 출력 ###")
                Contact.get_contacts(ls)
            elif menu == 3:
                print(" ### 연락처 삭제 ###")
                contact.delete_contact(ls, input(" 삭제할 사람 이름 :"))

            elif menu == 4:
                print(" ### 어플 종료 ###")
                break


Contact.main()
