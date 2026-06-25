# 딕셔너리(key , value)key(숫자,문자 모두 가능)
#[key](없는값:추가 // 중복값:수정) =    del 삭제  
#key값은 절대중복허용하지 않음. value값은 중복이 이루어져도 문제없음.
#cabinet = {3: '푸', 100: '피글렛' , 3:'스푸', 4:'피글렛'} #{3: '스푸', 100: '피글렛'}
# print(cabinet)

# cabinet[5] = '푸' #{3: '스푸', 100: '피글렛', 4: '피글렛', 5: '푸'}
# print(cabinet)
# cabinet[4] = '푸' #{3: '스푸', 100: '피글렛', 4: '푸', 5: '푸'}
# print(cabinet)
# del cabinet[5]  # {3: '스푸', 100: '피글렛', 4: '푸'}
# print(3 in cabinet)  #True (in)
# print(cabinet)

# # 딕셔너리에서 value 값은 in 체크 불가.
# print( "피글렛" in cabinet)

#key값 valuse값 items(key,valuse)값 가져오는 방법
# cabinet = {3: '푸', 100: '피글렛' , 4:'스티치'}
# print(cabinet.keys())    #([3, 100, 4])
# print(cabinet.values())  #(['푸', '피글렛', '스티치'])
# print(cabinet.items())  #([(3, '푸'), (100, '피글렛'), (4, '스티치')])


# for문을 출력 하시오 (key값 => value값) 
cabinet = {3: '푸', 100: '피글렛' , 4:'스티치'}
# keyList = cabinet.keys()
# for key in keyList :
#   print(cabinet[key])

#전체 삭제하는 기능
cabinet.clear()
print(cabinet)
