"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 참석률을 높이기 위해
댓글 이벤트를 진행하기로 하였습니다. 댓글 작성자들 중에 추첨을 통해 1명은
치킨, 3명은 커피 쿠폰을 받게 됩니다. 추첨 프로그램을 작성하시오.
조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용
(출력 예제)
--당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 –
(활용예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
"""
# data_list = []
# for i in range(1,21):
#   data_list.append(i)
# print(data_list)

#data_list2 = range(1,21)
#data_list3  = list(range(1,21))
#print(data_list3,type(data_list3))

from random import *
# #participant = range(0,20)
# participant = list(range(0,20))
# lucky_one = choice(participant)
# selected_users = sample(participant, 3)
# print(f"--당첨자 발표 -- \n 치킨 당첨자 :{str(lucky_one)}\n 커피 당첨자 :{str(selected_users)} \n-- 축하합니다 \n")
# #for coffe in participant : 


participant = list(range(1,21))
shuffle(participant)
lucky_one = sample(participant, 1)
selected_users = sample(participant, 3)
print(f"--당첨자 발표 -- \n 치킨 당첨자 :{str(lucky_one)}\n 커피 당첨자 :{str(selected_users)} \n-- 축하합니다 \n")



data_list = list(range(1,24))
shuffle(data_list)
print("치킨 당첨자 :{} ".format(data_list[0]))
print("커피 당첨자 :{} ".format(data_list[1:4]))