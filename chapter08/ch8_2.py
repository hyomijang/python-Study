# 파일 입출력 데이타베이스 -> 파일에 저장 가져오고, 저장하고,삭제하고 , 수정하기
#파일에서 "W" : 저장 # 읽어오기 : "r" 추가하기 : "A"
# 
# score.txt utf - 8 방식으로 입력하고 , 새로쓴다 
# file_handle = open("score.txt", "w"  , encoding="utf8")
# print("국어 : 100 ", file=file_handle)
# print("영어 : 90 ", file=file_handle)
# print("수학 : 90 ", file=file_handle)
# file_handle.close()

# #score.txt 추가기능을 설정해서 객체를 생성해야된다.
# file_handle = open("score.txt","a",encoding="utf-8")
# print("자바 : 100 ", file=file_handle)
# print("파이썬 : 90 ", file=file_handle)
# file_handle.close()


#score.txt 추가기능을 설정해서 객체를 생성해야된다.
# file_handle = open("score.txt","a",encoding="utf-8")
# #write() /n 기능이 없다. 마지막 /n 기능을 입력해야한다.
# file_handle.write("HTML : 100 \n")
# file_handle.write("CSS : 70 \n")
# file_handle.close()

#파일에서 # 읽어오기 : "r" 
# file_handle = open("score.txt","r",encoding="utf-8")
# print(file_handle.read())   #파일 내부 모든 내용을 읽는다.
# file_handle.close()

# file_handle = open("score.txt","r",encoding="utf-8")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# print(file_handle.readline(), end="")
# file_handle.close()

# file_handle = open("score.txt","r",encoding="utf-8")
# exit_flag = False
# while not exit_flag :
#   line = file_handle.readline()
#   #EOF 이면 line false
#   if line : 
#     print(line, end="")
#   else:
#     exit_flag = True
   
# file_handle.close()

file_handle = open("score.txt","r",encoding="utf-8")
list = file_handle.readlines()
file_handle.close()
#print(list, type(list))   
for data in list : 
  print(data,end="")