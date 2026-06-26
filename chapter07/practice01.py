"""
Quiz) "리그 오브 레전드" 게임에서 세명의 팀원이 얻은 골드량을 매개변수로
받아, 팀의 평균 골드 획득량을 계산하는 함수 cal_average_gold를 정의하고 사
용해 보세요.
cal_average_gold(12000, 15000, 18000)
실행결과
15000.0
Quiz) "리그 오브 레전드" 게임에서 특정 챔피언의 킬(kill), 데스(death), 어시스
트(assist) 수치를 매개변수로 받아, KDA(Kill-Death-Assist) 비율을 계산하는 함수
cal_kda를 정의하고 사용해 보세요.
힌트) (Kill + Assist)/(Death)
cal_kda(10, 2, 7)
실행결과
8.5
"""

def cal_kda(*cal_average_gold) :
  for gold in cal_average_gold :
   sum(gold)/len(gold)
   print("{}".format(gold),end = "")

cal_kda(12000, 15000, 18000)
print(cal_kda)

def cal_average_gold(*no):
  avg = sum(no)/len(no)
  print(avg)
cal_average_gold(12000,15000,18000)