# 클래스 Unit , (정적, 인스턴스)멤버변수 : 이름 ,체력, 공격력 , 이동스피드

class Unit :
  def __init__(self, name , hp , damage ,speed):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.speed = speed
    print(f"{self.name} 유닛이 생성되었습니다.")
    print(f"체력: {self.hp} 공격력: {self.damage} 이동속도:{self.speed}")


# 유닛객체를 생성한다. 
soldier1 = Unit("보병1", 40 , 5 , 5)
soldier2 = Unit("보병2", 40 , 5 , 5)
tank = Unit("탱크1", 150 , 20 , 10)


#해당된 객체에서 멤버변수가 필요하면 , 동적 할당할 수 있다.
#그러나 다른 객체에는 영향을 미치지 않는다.

# print(f"{tank.name} {tank.hp} {tank.damage} {tank.speed} {tank.fly}")
# print(f"{soldier1.name} {soldier1.hp} {soldier1.damage} {soldier1.speed} {soldier1.fly}")

class AttackUnit :
    def __init__(self, name , hp , damage ,speed):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력: {self.hp} 공격력: {self.damage} 이동속도:{self.speed}")

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

#fireSoldier.attack(5)
#fireSoldier.damaged(20)

#배열관리로 선언하기
attacklist = []
attacklist.append(soldier1)
attacklist.append(soldier2)
attacklist.append(tank)
attacklist.append(fireSoldier)

for unit1 in attacklist:
  unit1.attack(5)
        