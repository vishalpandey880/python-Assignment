#  class student:
  #  roll_number = 8 #class variable/attribute

#   def __init__(self,roll_number): #constructor
#     self.roll_number = roll_number
  
#   def learn(self): #class method 
#     return "learning..."
  
# def bunk(): #regular function
#   return "bunking..."

 #making object and assigning class variable

# Aareen = student(178)
# print(Aareen.roll_number)
# print(Aareen.learn())

# print(student.roll_number)

# class Faculty:
#   pass

# prasad = Faculty()
# prasad.skills = ["Python","Java","C++"]
# print(prasad.skills)

# gatik = Faculty()
# # print(gatik.skills)  #AttributeError: 'Faculty' object has no attribute 'skills'

# Faculty.skills = ["read"]
# print(gatik.skills)

# def teach():
#   return "teaching..."

# prasad = Faculty()
# prasad.teach = teach
# print(prasad.teach())

# #parent class
# class Person:

#   def __init__(self, fname, lname):
#     self.fname = fname
#     self.lname = lname
#   def print_full_name(self):
#     return self.fname + " " + self.lname
  
# #child class
# class user(Person):
#   def __init__(self, fname, lname):
#     # self.fname = fname
#     # self.lname = lname
#     super().__init__(fname, lname)
  
#   #from parent - overides parent function
#   def print_full_name(self):
#     return self.fname + " and " + self.lname 
  
#   #it's own method
#   def set_username(self):
#     return self.fname 

# #make object of user class
# Person_one = Person("John", "Cena") 
# print(Person_one.fname)
# print(Person_one.lname)

# #make object of user class
# user_one = user("John", "Cena") 
# print(user_one.fname) #john
# print(user_one.lname) #cena
# print(user_one.print_full_name()) #john cena  

# - - - - - - - - - - - - - - - -  - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - -

#user - username, password
#auth - login,reg,logout

user_input = input("Enter username: ")
password_input = input("Enter password: ")

class User:
  def __init__(self, username, password):
      self.username = username
      self.__password = password  #private attribute

      def get_password(self):
        return self.__password # public access

class Auth(User):

    def __init__(self, username, password):
      super().__init__(username, password)


    def get_password(self):
      return self._User__password

    def login(self, username, password):
      # if username == user_input and self.get_password() == password_input:
      if self.username == user_input and self.get_password() == password_input:       # return "Logged in successfully " + self.username + " " +  self.get_password() +  " " + user_input + " " + password_input 
        return "Logged in successfully "
      else:
        # return "Invalid " + self.username + " " +  self.get_password() +  " " + user_input + " " + password_input
          return "Invalid "
    
    def reg(self):
        pass

object = Auth('admin', 'admin123')
print(object.login(user_input, password_input))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# abstraction

# from abc import ABC, abstractmethod

# class Human(ABC):
  
#   @abstractmethod
#   def talk(self):
#     print("talking...")

# class Man(Human):
  # def talk(self):
  #   print("hmmm")
# def walk(self):
#     print("walking...")

# person = Man()
# person.walk()