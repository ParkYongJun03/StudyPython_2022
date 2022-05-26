# 주소록 프로그램
'''
주소록 프로그램 v 1.0
작성일 2022-05-26 09:14
작성자 liam
설명 파일DB를 활용한 주소록 프로그램 테스트
'''

import os
# 주소록 클래스


class contact:
    address = ''
    name = ''
    e_mail = ''
    phone_number = ''

    # None : 이 함수는 리턴에 없습니다.
    def __init__(self, name, address, phone_number, e_mail) -> None:
        #            print(f'주소록 클래스 생성했습니다. address, name, ,e_mail, phone 속성을 넣으세요')
        # print(f'주소록 클래스에 추가했습니다')
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

# 파일 저장 함수


dir_name = 'C:/Repository/StudyPython_2022/day4/'  # 절대경로


def saveContacts(contacts):
    global dir_name  # 바깥에 있는 dir_name가져올 수 있음
    f = open(f'{dir_name}contacts.txt', mode='w', encoding='utf-8')
    for item in contacts:
        f.write(f'{item.name}/{item.address}/{item.phone_number}/{item.e_mail}\n')
    f.close()

# 파일 로드 함수


def loadContacts(contacts):
    global dir_name  # 바깥에 있는 dir_name가져올 수 있음
    f = open(f'{dir_name}contacts.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break

        # replace: 탈출문자(\n, \r)문자는 무조건 지워줘야한다. \n은 저장할때만 써라
        lines = line.replace('\n', '').split('/')
        contact_l = contact(lines[0], lines[1], lines[2], lines[3])
        contacts.append(contact_l)
    f.close()  # 필수
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


# 연락처 검색 함수


def searchContact(contacts, name):
    # 클래스를 enumerate에 넣으면 i에 index가 들어가고 item에는 contacs객체가 들어간다.
    isFind = False
    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True:
            print(contacts[i])  # item=contacts[i]
            isFind = True
    if isFind == False:
        print('검색된 결과가 없습니다.')
    input('Press Any Key to Continue')

# 연락처 검색 함수


def editContact(contacts, name):
    # 클래스를 enumerate에 넣으면 i에 index가 들어가고 item에는 contacs객체가 들어간다.
    isFind = False
    editTgt = []
    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True:
            editTgt.append((i, item))
            isFind = True
    if isFind == False:
        print('검색된 결과가 없습니다.')
    else:
        clearConsole()
        print(f'검색된 결과로 {len(editTgt)}건의 이름이 있습니다.')
        while editTgt:
            print(f'저장된 정보는 다음과 같습니다. \n{editTgt[0][1]}')
            try:
                a = int(input('이름은 1번, 주소는 2번, 번호는 3번, e_mail은 4번을 입력해주세요\n > '))
                if a == 1:
                    contacts[editTgt[0][0]].name = input(
                        f'저장된 이름 {editTgt[0][1].name} -> 새로 저장할 이름 : ')
                elif a == 2:
                    contacts[editTgt[0][0]].address = input(
                        f'저장된 주소 {editTgt[0][1].address} -> 새로 저장할 주소 : ')
                elif a == 3:
                    contacts[editTgt[0][0]].phone_number = input(
                        f'저장된 번호 {editTgt[0][1].phone_number} -> 새로 저장할 번호 : ')
                elif a == 4:
                    contacts[editTgt[0][0]].e_mail = input(
                        f'저장된 e_mail {editTgt[0][1].e_mail} -> 새로 저장할 e_mail : ')
                else:
                    clearConsole()
                    print('정해진 숫자 범위 이내로 입력해주세요[1, 2, 3, 4]')
                    continue
            except Exception as ex:
                clearConsole()
                print(f'예외 발생 {ex}')
                print('정확한 포맷으로 입력해주세요')
                continue
            print(f'새로 저장된 정보는 다음과 같습니다. \n{contacts[editTgt[0][0]]}')
            del editTgt[0]
    input('Press Any Key to Continue')

# 메뉴출력


def getMenu():
    str_menu = ('주소록 프로그램 v1.1\n'  # 괄호를(())를 붙이면 굳이 \를 붙이지 않아도 된다 ref) line : 27
                '1. 연락처 추가 \n'
                '2. 연락처 출력\n'
                '3. 연락처 검색\n'  # 22.05.26 16:09 주석추가
                '4. 연락처 수정\n'  # 22.05.26 16:32 주석추가
                '5. 연락처 삭제\n'
                '6. 프로그램 종료\n')
    print(str_menu)
    menu = int(input('메뉴선택 > '))
    return menu


def run():
    contacts = []  # 빈 리스트 변수 초기화
    try:
        loadContacts(contacts)
    except:
        print('저장된 contacts.txt가 없습니다')
        input('press any key to continue')
    while True:
        sel_menu = getMenu()
        clearConsole()
        if sel_menu == 1:
            print(f'1번 연락처 추가 메뉴')
            member = setContact()
            if(member != None):
                contacts.append(member)  # 연락처 리스트에 새 연락처를 추가
        elif sel_menu == 2:
            print(f'2번 연락처 출력 메뉴')
            print(f'총 {len(contacts)}건의 연락처가 있습니다.')
            printContacts(contacts)
        elif sel_menu == 3:
            print(f'3번 연락처 검색 메뉴')
            name = input('검색할 이름 입력 > ')
            searchContact(contacts, name)
        elif sel_menu == 4:
            print(f'4번 연락처 수정 메뉴')
            name = input('수정할 이름 입력 > ')
            editContact(contacts, name)
        elif sel_menu == 5:
            print(f'5번 연락처 삭제 메뉴')
            name = input('삭제할 이름 입력 > ')
            delContact(contacts, name)
        elif sel_menu == 6:
            saveContacts(contacts)
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
