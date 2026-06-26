# pickle


import pickle

# #pickle 파일저장
# #binary 파일로 저장할 떄는 encoding 방식이 필요치 않다.
# profile_handdle = open("profile.pickle","wb")

# profile_dic = {"이름 " : "asd" , "나이" : 94 ,"취미":["수면","음식탐방","영화"]}
# #우리가 프로그램에서 사용했던 , 맵구조 (dict)다시 사용하기 위해서 pickle 파일에 저장
# pickle.dump(profile_dic,profile_handdle)
# print(profile_dic,type(profile_dic))
# profile_handdle.close()

# pickle 파일을 다시 가져와서 프로그램 사용하기 위한 기능
# profile_handdle = open("profile.pickle","rb")
# list_dic = pickle.load(profile_handdle)
# profile_handdle.close()
# print(list_dic,type(list_dic))

# for key,value in list_dic.items():
#   print(key,value)


# 파일을 한번에 열고, 자동으로 닫기 : with (자바: try with resources) 
# with open("profile.pickle","rb") as profile_handdle:
#  list_dic =  pickle.load(profile_handdle)
#  for key,value in list_dic.items():
#   print(key,value)
#   if key == "취미":
#    for data in value :
#     print("{} = {}".format(key,data))

# print("with profile_handdle.close() 안해도 된다.")

# 일반파일을 with 처리하는 방식(닫는기능 자동으로 처리)
# with open("data.txt" , "w", encoding="utf - 8") as data_handdle:
#   data_handdle.write("파이썬 \n")
#   data_handdle.write("자바 \n")
#   data_handdle.write("스프링부트 \n")


with open("data.txt" , "r", encoding="utf - 8") as data_handdle:
 print( data_handdle.read(),end="")
