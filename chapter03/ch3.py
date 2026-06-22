# 연산자 (+,-,/,%,**,//)
# print(3 + 2)
# print(3 - 2)
# print(3 * 2)
# print(3 / 2)
# print(3 % 2)
# print("*"*20)
# print(3 // 2) # 1
# print(3 ** 2) # 9

# 관계연산자 ( < > <= >= == != and(&) or(|) 5<a<10)
# num = 5
# print(2 < num < 10)      # true
# print(not(2 < num < 10)) # false

# print(num >2 and num <10)       # true
# print(not(num >2 & num <10))    # false
# print(not(num and num <10))    # false

# print(num >2 or num <10)    # false
# print(num >2 | num <10)    # false

# # 수식연산자
# print (( 5 + 4 )* 2)

# # 복합대입연산자
# num = 10
# num = num + 10
# num += 10

# num = num * 10
# num *= 10

# num = num / 10
# num /= 10

# num = num // 10
# num //= 10

# num = num ** 10
# num **= 10

# num = num % 10
# num %= 10
# print("num = "+str(num)+"")

# 숫자처리 함수 abs pow max min round
# print(abs(-5))
# print(pow(2,3))
# print(2**3)
# print(max(3,5,7,20,2,6,75))
# print(min(3,5,7,20,2,6,75))
# print(round(3.141592))  # 3
# print(round(3.541592))  # 4
# print(round(3.541592,2))  # 3.54 소숫점 2자리까지 표현해준다.

# 모듈 가져와서 작업
# from math import * #math 모듈에서 모든 함수를 가져와서 사용하겠다.
# result = floor(4.9999)
# print(result)

# result = ceil(4.9999)
# print(result)

# result = sqrt(16)
# print(result)

# 랜덤함수 모듈
from random import * # random 모듈에서 사용되어지는 모든함수 가져오겠다.
# # 120 ~ 179

# for i  in range(1,11) :
#   print(random()) # 0.0 <=random() < 1.0


# # 120~179 (random()*(큰값 - 작은값 -1 )+작은값 )
# for i  in range(1,11) :
#   print(int(random()*(179 - 120 +1)+120)) 

# range(1,41) : 1부터 ~40까지  
# randrange(1,41) 1~40까지 랜덤출력

for i  in range(1,11) :
  print(randrange(1,101))

