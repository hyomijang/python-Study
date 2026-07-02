#외장함수

#glovb == wnd dir 기능이다.
import glob

#print(glob.glob("chapter2"))

#os : 운영체제에 관련된 정보를 확인 
import os
# print(os.getcwd())

# #현재 디렉토리에서 디텍토리를 생성하고, 삭제를 진행할 수있다

# if os.path.exists("sample_text"):
#   print("찾을 수 있습니다")
#   os.rmdir("sample")
# else:
#   print("찾을 수 없습니다")
#   os.mkdir("sample")

# 현재 작업하는 폴더안의 리스트를 볼 수 있는지 점검
# print(os.listdir())

# 외장 함수 time
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 외장 함수 datetime
import datetime
print("오늘의 날짜는",datetime.date.today())
today = datetime.date.today()
# 현재 날짜에소 100일이 지난 날짜를
td = datetime.timedelta(days=100) 
print(td + today)