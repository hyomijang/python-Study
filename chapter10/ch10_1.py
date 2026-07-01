# 예외처리

# 두수를 입력받아서 나눗셈해서 결과값을 출력하는 프로그램 작성

# exitFlag = False
# while not exitFlag:
#   try: 
#     num1 = int(input("number1 을 입력해주시오>>"))
#     num2 = int(input("number2 을 입력해주시오>>"))
#       # print(f"{num1} / {num2} = {num1 / num2}")
#     print("{} / {} = {:.2f}".format(num1,num2,num1/num2))
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력하였습니다.")
#     exitFlag = True
# print("프로그램 종료")

# while True:
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>")) 
#     print(" {0} / {1} = {2:.2f}".format(num1, num2, num1 / num2))
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#     continue
#   except Exception as e:
#     print(e)
#     continue
#   finally : 
#     print("finally")
#   break

# print("프로그램 종료")

# 오류를 사용자가 조건에 따라서 발생시킴
# while True:
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>")) 
#     # 조건을 설정 (두수는 0보다 크고 10보다 작거나 같아야만 실행)
#     if (0 < num1 <=10 )& ( 0 < num2 <=10)  : 
#       print(" {0} / {1} = {2:.2f}".format(num1, num2, num1 / num2))
#     else:
#       raise  ValueError
  

#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#     continue
#   except Exception as e:
#     print(e)
#     continue
#   finally : 
#     print("finally")
#   break

# print("프로그램 종료")

