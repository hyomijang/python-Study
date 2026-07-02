# 내부 모듈을 가져와서 사용하기

# import theater_module

# #일반인 영화예매 3명
# theater_module.price(3)
# theater_module.price_morning(3)
# theater_module.price_solider(3)

# 가져온 모듈 별칭
# import theater_module as tm
# tm.price(3)
# tm.price_morning(3)
# tm.price_solider(3)

# 가져온 모듈 별칭없이 바로 사용
# from theater_module import *
# price(3)
# price_morning(3)
# price_solider(3)

# # 가져온 모듈 별칭없이 바로 price 지정사용
# from theater_module import price #(price_morning,price_solider 불러오는 명령어 한정 사용가능)
# price(3)

# 가져온 모듈 별칭없이 바로 price 지정사용(+별칭)
from theater_module import price as tm
tm(3)
