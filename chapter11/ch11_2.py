# 내부에서 package를 만드는 방법
#  package == 폴더와 유사하다 (여러개 모듈을 포함하고 있다.)


# travel 패키지속에 thailand 모듈 가져오기
# 조심해야 될 부분 (import 안에 해당되는 ㅋ클래스나 하브)
import  travel.thailand 

thailand_obj = travel.thailand.ThailandModule()
thailand_obj.detail_travel()

# 자바형식 import 기능과 같다
# from travel.vietnam import VietnamdModule

# import travel.vietnam

# vietnam_obj = VietnamdModule()
# vietnam_obj.detail_travel()

# 해당되는 패키지에 모두 모듈을 가져오는 방법
# from chapter11 import *

# t_obj = thailand.ThailandModule()
# vietnam_obj = vietnam.ViernamModule()

# 패키지 모듈위치
# import inspect
# import random

# # spect를 사용해서 random 패키지 위치 검사
# print(inspect)
# import inspect
# from travel import *
# print(imspect.getfile(thailand))

# t_obj2 = thailand.ThailandModule()


