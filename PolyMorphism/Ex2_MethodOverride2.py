# ex1: Method Override in Multi level Inheritance

class GrandFather:
   def home(self):
       print("1 BHK")

   def money(self):
       print("1 Lakh")


class Father(GrandFather):
   def home(self):
       print("2 BHK")

   def money(self):
       print("2 Lakh")


class Son(Father):
   def home(self):
       print("3 BHK")

   def money(self):
       print("3 Lakh")


g=GrandFather()
g.home()
g.money()
print("------")
f=Father()
f.home()
f.money()
print("------")
s=Son()
s.home()
s.money()