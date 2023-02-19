class Person:
  Heght = 140
  age = 11
  name = "Oleh"
  weight = 43
  is_male = True
  hobby = "ice skiing"
  
  def __init__(self, surname):
    self.surname = surname


me = Person("Ignatyhc:")
you = Person("Test")
print(me.age)
# print(me.surname)


def do_my_thing(self):
  print("I love", self.hobby)

  
  # make class
me = Person("Ignatyhc:")

hobby = "ice skiing"
me.do_my_thing()

my_friend = Person("Zahar")

my_friend.hobby = "Play roblox"