# 다중상속을 진행한다 (모호성을 해결하는 방법을 구현한다.)

# 일반유닛 (지상 공격력이 없는 유닛)
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"유닛이름: {self.name} / 체력: {self.hp} / 이동속도: {self.speed}")

  def move(self, location):
    print(f"{self.name} 지상유닛이 {location} 방향으로 가고 있습니다.") 


# 공격력이 있는 유닛(상속)
class AttackUnit(Unit):
  #생성자
  def __init__(self, name, hp, speed , damage):
   # 다중상속때 문제가 생김 
   # super().__init__(name, hp, speed)
   # 부모를 책임짐
   Unit.__init__(self, name, hp , speed)
   self.damage = damage

  #멤버함수
  def attack (self,location):
          print(f"{self.name}이 현재체력:{self.hp} 이동속도:{self.speed}{location}:방향으로 {self.damage}공격력으로 공격중입니다.")

      # 상대방의 공격력: damage
  def damaged(self,damage):
    print(f"{self.name}이  공격받았습니다.")
    self.hp = self.hp - damage
    if(self.hp <= 0):
     print(f"{self.name} 유닛은 파괴되었습니다.")
    else:
      print(f"{self.name} 유닛의 남은체력: {self.hp}")

#비행기능이 있는 유닛(상속)
class FlyUnit:
  def __init__(self, flying_speed):
   self.flying_speed = flying_speed

    # 멤버함수
  def fly(self , name, location):   
    print(f"{self.name}유닛이 {self.flying_speed}속도로 {location}방향을 향해  날아가고 있습니다.")

# 다중상속 (지상공격유닛, 공중유무 유닛)
class FlyableAttackUnit(AttackUnit,FlyUnit):
   #(self, name, hp, speed, damage)
   #(self, name, hp, speed, damage)
  def __init__(self, name, hp, speed, damage ,flying_speed):
      AttackUnit.__init__( self ,name, hp, speed, damage)
      FlyUnit.__init__(self, flying_speed)

  def move(self, location):
     print(f"{self.name} 지상유닛이 {location} 방향으로 가고 있습니다.")  

# 공격기능을 가진 interceptor 객체생성
intercetor = FlyableAttackUnit("요격기" , 300 , 0 , 80 , 200 )
intercetor.attack("2시방향")
intercetor.damaged(2)
intercetor.fly(50,50)