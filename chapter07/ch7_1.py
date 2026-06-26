# 함수

# 함수선언
# def open_func():
#   print("드디어 함수 시작입니다.")

# open_func()

# # 함수선언(매개변수)
# def add_func(num1, num2):
#   print("덧셈을 계산하는 함수입니다.")
#   return num1 + num2 

# sum = add_func(10,20) 
# print(f"add_func(10,20) = {sum}") 

#함수 기본값 설정
# def profile(name, age, main_subject):
#   print(" 나의 이름은 : {} \n 나이는 : {} \n 메인언어는  : {}".format(name , age, main_subject))

# #profile("kdh","1","python")

# # 가변인자 *가변인자변수명
# def new_profile(name, age ,lang1, lang2, lang3):
#  print(name, age ,lang1, lang2, lang3)

# new_profile("asd",123,"c","c","b")

def new_profile2(name, age ,*language):
 print(name, age)
 print(language, type(language))
 for lang in language: #('c', 'c', 'b', 'd') <class 'tuple'>
  print("{}".format(lang),end = "")

new_profile2("asd",123,"c","c","b","d")
new_profile2("asd",123,"c")