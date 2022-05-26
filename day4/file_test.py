# 파일 테스트

# f = open('C:/Repository/StudyPython_2022/day4/sample2.log',
#          mode='w', encoding='utf-8')
f = open('./day4/sample3.log',
         mode='a', encoding='utf-8')

f.write('테스트, 테스트!!\n')

f.close()
print('로그파일 생성완료')
