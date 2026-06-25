#자료구조의 변경

#set => list 변경
menu = {"햄버거","치킨","또띠야"} #{'또띠야', '햄버거', '치킨'} <class 'set'>
print(menu,type(menu))
menu =  list(menu)
print(menu,type(menu))  #['또띠야', '햄버거', '치킨'] <class 'list'>

#list => tuple
menu =  tuple(menu)
print(menu,type(menu))  #('햄버거', '치킨', '또띠야') <class 'tuple'>

#tuple = > set
menu2 = ('햄버거', '치킨', '또띠야','또띠야') #('햄버거', '치킨', '또띠야', '또띠야') 
print(menu2,type(menu2))  #{'치킨', '또띠야', '햄버거'} <class 'set'>
menu2 =  set(menu2)
print(menu2,type(menu2))  #{'치킨', '또띠야', '햄버거'} <class 'set'>