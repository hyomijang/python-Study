# 전역변수 , 지역변수

#카센터 데이터 총 갯수

#전역변수
car_total = 100
def rent(rent_count):
  #지역변수
  global car_total 
  car_total = 200
  if car_total > rent_count :
    car_total = car_total - rent_count 
    print("랜트 할 {}대 진행합니다.. 남은 차량 수는 {} 입니다".format(rent_count,car_total - rent_count))
  else :
    print("랜트가 가능한 차량이 없습니다.")

rent(10)
print(car_total)