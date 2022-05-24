# 회원관리 프로그램 템플릿

num = 0
user = '회원정보'
menu_num = [f'{user}입력', f'{user}검색', f'{user}수정', f'{user}삭제', '종료']


while True:
    print('메뉴번호를 입력하세요.')
    for i in range(1, 6):
        print(f'{i}. {menu_num[i-1]}')
    num = int(input('숫자 입력 :'))
    print(num)
    if(num == 5):
        break
    print(f'{menu_num[num]}으로 전환')
