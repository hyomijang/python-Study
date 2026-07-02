# 라이브러리 함수 기능만 있는 모듈

# 일반인이 영화를 관람했을때 요금을 계산하는 라이브러리
def price(count):
  price = 14000
  print(f"{count}명은 영화의 1인당 영화 가격은 {price} 전체금액은:{count * price}")

# 조조할인 (40%할인)
def price_morning(count):
  price = int(14000 * 0.6)
  print(f"{count}명은 영화의 1인당 조조영화 가격은 {price} 전체금액은:{count * price}")


# 군인할인 (60%할인)
def price_solider(count):
  price = int(14000 * 0.4)
  print(f"{count}명은 영화의 1인당 군인할인 영화 가격은 {price} 전체금액은:{count * price}")
