#문자열에서 자주사용하는 방법: slicing [],find,replace,count(),upper(),lower(),isupper(),islower()

#문자열 """ ~~~ """ ''' ~~~ ''' :여백,또는 공백 기능까지 모두 포함해서 문자열 취금한다.

# message = "파이썬을 공부하고 있습니다."
# print(message,type(message))

# message2 = """
# 파이선을
# 공부 
# 하고 있습니다.
# """
# print(message2,type(message2))

#슬라이싱[]

#jumin = "990829-1550823"
# 
# print("사용자 성별번호:", jumin[7])
# print("사용자 연도:", jumin[0:2])
# print("사용자 월:", jumin[2:4])
# print("사용자 일:", jumin[4:6])
# print("사용자 생년월일:", jumin[:6])
# print("사용자 뒷자리:", jumin[7:])
# print("사용자 뒷자리 검증번호 이전:", jumin[7:-1])
# print("사용자 주민번호 문자열 길이:", len(jumin))

# for i in range(0,len(jumin)) :
#   if jumin[i] =="-" :
#     continue
#   print(jumin[i] ,  end="")

# 문자열 처리함수
# message = "Python is Amazing"
# print(message.lower()) #소문자로 변경되는 함수
# print(message.upper()) #대문자로 변경되는 함수
# print(message.isupper()) #(is = bool 값을 준다 T/F )
# print(message.replace("Python","Java")) # ****특정값을 수정한다.****

# message = "Python is Amazing"
# findIndex = message.find("n")
# print(findIndex) #5

# findIndex2 = message.find("n",findIndex+1)
# print(findIndex2) #15


# findIndex3 = message.find("is")
# print(findIndex3) #7

# findIndex4 = message.find("kim")
# print(findIndex4) #-1



#find , index 차이점
#find 진행시 타겟이 없을시 -1 값을 주고 다음문장을 실행
#index 진행시 타켓이 없을시 ValueError 발생시키고 중지(try catch로)
#index 개념보다 find를 사용하는것이 좋다.****

# message = "Python is Amazing"

# findIndex = message.index("n")
# print(findIndex) #5

# findIndex2 = message.index("n",findIndex+1)
# print(findIndex2) #15


# findIndex3 = message.index("is")
# print(findIndex3) #7

# # findIndex4 = message.index("kim")
# # print(findIndex4) 

# findIndex5 = message.index("n",6,-1)
# print(findIndex5) 

# message = "Python is Amazing"
# print(message.count("n")) #2
# print(message.count("k")) #0
# print(len(message)) #17

# 문자열 포맷
# print("java" + "python") #javapython
# print("java" , "python") #java python

# age = 20
# print("나는 %d살입니다." %20) #나는 20살입니다.
# print("나는 %d살입니다." %age) #나는 20살입니다.

# like = "파이썬"
# print("나는 %s을 좋아합니다." %"파이썬") #나는 파이썬을 좋아합니다.
# print("나는 %s을 좋아합니다." %like) #나는 파이썬을 좋아합니다.

# grade = "A"
# score = 96.50
# print("java 언어의 점수는 %c 등급입니다 "%"A")   #java 언어의 점수는 A 등급입니다 
# print("java 언어의 점수는 %c 등급입니다 "%grade) #java 언어의 점수는 A 등급입니다 
# print("java 언어의 점수는 %.2f 입니다 " %96.50 )  #java 언어의 점수는 96.50 입니다 
# print("java 언어의 점수는 %.2f 입니다 " %score )  #java 언어의 점수는 96.50 입니다

# fruit1 = "수박"
# fruit2 = "참외"
# print("나는 좋아하는 과일은 %s 과 %s 입니다"%("수박","참외"))
# #나는 좋아하는 과일은 수박 과 참외 입니다
# print("나는 좋아하는 과일은 %s 과 %s 입니다"%(fruit1,fruit2))
# #나는 좋아하는 과일은 수박 과 참외 입니다


# age = 20
# print("나는 {}살입니다." .format(age)) #나는 20살입니다.
# print("나는 %d살입니다." %age) #나는 20살입니다.

# like = "파이썬"
# print("나는 {}을 좋아합니다.".format(like)) #나는 파이썬을 좋아합니다.

# grade = "A"
# score = 96.50
# print("java 언어의 점수는 {} 등급입니다 ".format(grade)) #java 언어의 점수는 A 등급입니다 
# print("java 언어의 점수는 {} 입니다 " .format(score) )  #java 언어의 점수는 96.50 입니다

# fruit1 = "수박"
# fruit2 = "참외"
# print("나는 좋아하는 과일은 {} 과 {} 입니다".format(fruit1,fruit2))
# #나는 좋아하는 과일은 수박 과 참외 입니다
# print("나는 좋아하는 과일은 {1} 과 {0} 입니다".format(fruit1,fruit2))
# #나는 좋아하는 과일은 참외 과 수박 입니다

# age = 20
# print(f"나는 {age}살입니다.") #나는 20살입니다.

# like = "파이썬"
# print(f"나는 {like}을 좋아합니다.") #나는 파이썬을 좋아합니다.

# grade = "A"
# score = 96.50
# print(f"java 언어의 점수는 {grade} 등급입니다 ") #java 언어의 점수는 A 등급입니다 
# print(f"java 언어의 점수는 {score} 입니다 ")  #java 언어의 점수는 96.50 입니다

# fruit1 = "수박"
# fruit2 = "참외"
# print(f"나는 좋아하는 과일은 {fruit1} 과 {fruit2} 입니다")
# #나는 좋아하는 과일은 수박 과 참외 입니다
# print("나는 좋아하는 과일은 {1} 과 {0} 입니다".format(fruit1,fruit2))
# #나는 좋아하는 과일은 참외 과 수박 입니다


#탈출문자 \n \t \b \r \' \"
print("파이썬\n자바")
print("파이썬\t자바")
print("파이썬\b자바")
print("파이썬\r자바")
print("파이썬 \"자바\" .")
print("파이썬 \'자바\' .")
print("D:\공유폴더\JAVA_test")