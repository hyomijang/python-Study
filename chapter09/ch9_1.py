# class Unit:
#   def __init__(self, name, hp, damage, speed):
#     self.name = name
#     self.hp = hp
#     self.damage = damage
#     self.speed = speed
#     print(f"유닛이름: {self.name} / 체력: {self.hp} / 공격력: {self.damage} / 이동속도: {self.speed}")

# solder1 = Unit("보병1", 40, 5, 10)
# solder2 = Unit("보병2", 40, 5, 10)
# tank1 = Unit("탱크1", 150, 35, 30)


#공격유닛 생성
#클래스명은 AttackUnit, 멤버변수 : name, hp, damage, speed

class AttackjUnit:
  #생성자
  def __init__(self, name, hp, damage, speed):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.speed = speed
    print(f"{self.name}유닛이 체력: {self.hp}, 공격력{self.damage} 이동속도:{self.speed} 유닛이 생성되었습니다")

#멤버함수(공격함수)
  def attack(self, location):
    print(f"{self.name}가 {location}시 방향으로 공격력: {self.damage}으로 공격하고있습니다") 

#멤버함수(공격을 당하는 함수)
  def damaged(self ,damage):
      print(f"{self.name}가 상대방으로 부터 공격력  {damage}으로 공격을 받고있습니다.")    
      self.hp = self.hp - damage
      print(f"{self.name}가 상대방으로 부터 공격 받아 남아있는 체력은 {self.hp}입니다.")
      if(self.hp <=0):
       print(f"{self.name} 유닛은 파괴되었습니다.") 

#보병
soldier1 = AttackjUnit("보병1",40,5,10) 
soldier2 = AttackjUnit("보병2",40,5,10) 
soldier3 = AttackjUnit("보병3",40,5,10) 
soldier4 = AttackjUnit("보병4",40,5,10) 
tank1 = AttackjUnit("탱크1",130,35,20) 
tank2 = AttackjUnit("탱크2",130,35,20) 


#보병 1 공격
# soldier1.attack(10)
# soldier2.attack(10)
# soldier3.attack(10)
# soldier4.attack(10)
# tank1.attack(10)
# tank2.attack(10)

# 배열관리 공격지시
attack_list = []
attack_list.append(soldier1)
attack_list.append(soldier2)
attack_list.append(soldier3)
attack_list.append(soldier4)
attack_list.append(tank1)
attack_list.append(tank2)

for unit in attack_list:
  unit.attack(10)

#공격받음
# soldier1.damage(5)
# soldier2.damage(5)
# soldier3.damage(5)
# soldier4.damage(5)
# tank1.damage(5)
# tank2.damage(5)

for unit  in attack_list:
 unit.damaged(10)

# 날아다니면서 공격하는 유닛
# 사용되는 객체가 자신만의 멤버변수를 추가하면 , 자기자신에만 해당이 된다.
airunit= AttackjUnit("전투기",200,30,40) 
airunit.fly = True

if airunit.fly == True:
 print(f"{airunit.name}{airunit.hp}{airunit.damage}{airunit.speed} 공중유닛:{airunit.fly}")

# if airunit4.fly == True:
#  print(f"{airunit4.name}{airunit4.hp}{airunit4.damage}{airunit4.speed} 공중유닛:{airunit4.fly}")
# else:
#   print(f"{airunit4.name}{airunit4.hp}{airunit4.damage}{airunit4.speed}")