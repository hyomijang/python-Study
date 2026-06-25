# 반복문

# 반복문1
# list = [1,3,5,7,9]
# for no in list :
#   print("{}".format(no),end="")

# 반복문2
# for no in list [1,3,5,7,9]:
#   print("{}".format(no),end="")
# print("")

# # 반복문3
# for no in range(1,10,2):
#   print("{}".format(no),end="")
# print("")

# # 반복문4
# orders = ["햄버거", "짜장면", "짬뽕"]
# for data in  orders:
#   print("{}".format(data),end="")
#   print("")

# # 반복문4
# students = [1,2,3,4,5]
# print(students)
# #students = [11,12,13,14,15] #변경
# students = [ no + 10 for no in students ]
# print(students)

# # 반복문5
# menu = ["햄버거", "짜장면", "짬뽕"]
# print(menu)
# menu1 = [ len(data) for data in menu]
# print(menu)
# print(menu1)
# print("")

# like_subject = ["java","Python","html","spring Boot"]
# like_subject1 = [ subject.upper() for subject in like_subject]
# print(like_subject1)

# # 반복문6
# count = 0
# exitFlag = False
# while not exitFlag :
#   count += 1
#   print("count = {}".format(count) )
#   if count >= 100:
#     exitFlag = True

# 반복문7

data_list = [1,2,3,4,5]
no = int(input("[1,2,3,4,5] 선택입력>>"))

# for i in data_list :
#   if no == i :
#     print("있습니다")
#     break
#   else:
#     print("없습니다.")

if no in data_list :
 print("있습니다")
else:
  print("없습니다.")