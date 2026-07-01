# 자바 상속(부모것은 내것, 자식은 반드시 super(),오버라이딩 다중상속안됨(모호성)
# 파이썬 상속(부모것은 내것, 자식은 반드시 부모.--init--(self, 매개변수),오버라이딩 다중상속안됨(모호성)
#super(self가 들어가지 않음),오버라이딩 다중상속됨 (모호성이 발생하지 않는다. 순서가 정해져있다.)

class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"유닛이름: {self.name} / 체력: {self.hp} / 이동속도: {self.speed}")


nuerse1 = Unit("간호사",40,5)
nuerse2 = Unit("간호사",40,5)

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
         print(f"{self.name}이 현재체력:{self.hp} {self.damage}공격력으로 공격받았습니다.")
         self.hp = self.hp - damage
         if(self.hp <= 0):
          print(f"{self.name} 유닛은 파괴되었습니다.")
         else:
            print(f"{self.name} 유닛의 남은체력: {self.hp}")

# 화염방사병 : 공격유닛
fireSoldier = AttackUnit("화염방사병",40,10,5)

fireSoldier.attack(5)
fireSoldier.damaged(20)
fireSoldier.damaged(20)


