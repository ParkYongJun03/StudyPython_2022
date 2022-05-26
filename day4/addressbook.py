# 주소록 프로그램
'''
주소록 프로그램 v 1.0
작성일 2022-05-26 09:14
작성자 liam
설명 파일DB를 활용한 주소록 프로그램 테스트
'''

import os
# 주소록 클래스
Version = 4


class contact:
    address = ''
    name = ''
    e_mail = ''
    phone_number = ''

    if Version == 2 or Version == 3 or Version == 4:
        # None : 이 함수는 리턴에 없습니다.
        def __init__(self, name, address, phone_number, e_mail) -> None:
            #            print(f'주소록 클래스 생성했습니다. address, name, ,e_mail, phone 속성을 넣으세요')
            print(f'주소록 클래스에 추가했습니다')
            self.name = name
            self.address = address
            self.phone_number = phone_number
            self.e_mail = e_mail

    def __str__(self) -> str:  # 줄 바꿀때는 \를 붙인다.
        res_str = f'이름\t: {self.name}\n' + \
            f'주소\t: {self.address}\n' \
            f'폰번호\t: {self.phone_number}\n' \
            f'이메일\t: {self.e_mail}\n' \
            '=============================='
        return res_str

    def isNameExist(self, name) -> bool:
        if self.name == name:
            return True
        else:
            return False


# 화면 클리어 함수
def clearConsole():
    command = 'clear'  # UNIX, LINUX, MACOS
    if os.name in ('nt', 'dos'):  # WINDOW
        command = 'cls'
    os.system(command)


# 사용자 정보 입력


def setContact():
    member = None
    try:
        (name, address, phone_number, e_mail) = input(
            '정보입력(이름, 주소, 폰번호, 이메일)[구분자 : /] > ').split('/')
        member = contact(name, address, phone_number, e_mail)
    except Exception as ex:
        print(f'예외 발생 {ex}')
        print('정확하게 이름/주소/폰번호/이메일 포맷으로 입력해주세요')
    # print(name, address, phone_number, e_mail)
    # 순서 바꾸고 싶으면 이렇게 해도 된다.
    # member = contact(name=name, address=address,
    #                  phone_number=phone_number, e_mail=e_mail)
    return member

# 연락처 리스트 출력 함수


def printContacts(contacts):
    for item in contacts:
        print(item)
    input('Press Any Key to Continue')
# 연락처 삭제 함수


def delContact(contacts, name):
    # 클래스를 enumerate에 넣으면 i에 index가 들어가고 item에는 contacs객체가 들어간다.
    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True:  # 같은 이름이 있으면 다 지워진다
            del contacts[i]
            break  # 같은 이름이 있더라도 제일 첫번째 녀석만 지워지게 함


# 메뉴출력


def getMenu():
    str_menu = ('주소록 프로그램 v1.0\n'  # 괄호를(())를 붙이면 굳이 \를 붙이지 않아도 된다 ref) line : 27
                '1. 연락처 추가 \n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 프로그램 종료\n')
    print(str_menu)
    menu = int(input('메뉴선택 > '))
    return menu


def run():
    contacts = []  # 빈 리스트 변수 초기화
    if Version == 1:
        member = contact()
        member.name = '홍길동'
        member.address = '서울'
        member.phone_number = '010-0000-1111'
        member.e_mail = 'hgd03@naver.com'
        print(member)
    elif Version == 2:
        member = contact('홍길동', '서울', '010-0000-1111', 'hgd03@naver.com')
        print(member)
    elif Version == 3:
        setContact()
    else:
        while True:
            sel_menu = getMenu()
            clearConsole()
            if sel_menu == 1:
                print(f'1번 연락처 추가 메뉴를 입력했습니다.')
                member = setContact()
                if(member != None):
                    contacts.append(member)  # 연락처 리스트에 새 연락처를 추가
            elif sel_menu == 2:
                print(f'2번 연락처 출력 메뉴를 입력했습니다.')
                print(f'총 {len(contacts)}건의 연락처가 있습니다.')
                printContacts(contacts)
            elif sel_menu == 3:
                print(f'3번 연락처 삭제 메뉴를 입력했습니다.')
                name = input('삭제할 이름 입력 > ')
                delContact(contacts, name)
            elif sel_menu == 4:
                break
            clearConsole()


if __name__ == '__main__':  # EntryPoint (프로그램 시작점)
    clearConsole()
    print(__name__)
    print('프로그램 시작')  # 프로그램이 시작됨
    try:
        run()
    except KeyboardInterrupt as ex:
        print('비정상종료')

print('프로그램 종료')
