# Phthon 리스트  == 자바의 List<Object>
#append(추가) insert(삽입) pop(제거) [index] = (수정) 
# find,index(검색) count(카운트)
# subway = [10,20,30]
# subway.append(40)      # [10,20,30,40]
# subway.insert(1,100)   # [10, 100, 20, 30, 40]
# value  = subway.pop()  # value = 40 #subway = [10, 100, 20, 30]
# subway[0] = 200        # [200, 100, 20, 30]
# indexValue = subway.index(100) #1
# subway.append(100)     # [200, 100, 20, 30,100]
# countValue = subway.count(100) #2
# subway.clear()         # []
# print(countValue)
# print(indexValue)

# subway = ['감자','수박','참외']
# subway.append('오이')      # ['감자','수박','참외','오이']
# subway.insert(1,'토마토')  # ['감자','토마토','수박','참외','오이']
# value  = subway.pop()  # value = 40 #subway = ['감자','토마토','수박','참외']
# subway[0] = '돼지감자'       # ['돼지감자', '토마토', '수박', '참외']
# indexValue = subway.index('돼지감자') #1
# subway.append('돼지감자')     # ['돼지감자', '토마토', '수박', '참외', '돼지감자']
# countValue = subway.count('돼지감자') #2
# subway.clear()         # []
# print(subway)
# print(countValue)
# print(indexValue)

#정렬(sort()),  역정렬(reverse())
#리스트에서 값이 존재하는지 확인 (in)
#원본 정렬진행
#리스트 내부 전체합계산 : sum
subway = [10,20,90,30,40,60]
print( 60 in subway)
total = sum(subway)
subway.sort()        # [10, 20, 30, 40, 60, 90]
subway.sort(reverse=True)        # [90, 60, 40, 30, 20, 10]
subway.reverse()     # [90, 60, 40, 30, 20, 10]
print(subway)

#Deep copy (깊은복사)
# subway = [10,20,90,30,40,60]
# newSubway = sorted(subway)
# print(subway)
# print(newSubway)
# newSubway.reverse()
# print(newSubway)

# 리스트 합집합 || extend
# mixList1 = [10 , True , "감자", [1,2,3,4]]
# print(mixList1)
# mixList2 = [30 , False , "고구마"]
# print(mixList2)
# mixList1.extend(mixList2)
# print(mixList1)

