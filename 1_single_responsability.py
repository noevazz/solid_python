print("""\
TASK: We want a program to save new users,
make sure you encrypt his password.
""")

print("----------- WITHOUT Single Responsability Principle -----------")
class User():
	def __init__(self, name, password):	
		self.__password = password[::-1] # this line is my really complex encryption algorithm xd
		self.name = name # basic setup for the user

	def get_pass(self):
		return self.__password

user1 = User("Noe", "MyNicePassword")
print(f"User: {user1.name}, Password: {user1.get_pass()}" )

# You will need to change the User class if you only want to modify the encryption algorithm
# Also you need to chage the class to modify things about the basic setup for the user


print("\n----------- WITH Single Responsability Principle ------------")
class Encrypt():
	def complex_algorithm(self, password):
		# doing a lot of modification here for my really complex encryption algorithm:
		return password[::-1].upper()

class UserSRP(Encrypt):
	def __init__(self, name, password):
		super().__init__()
		self.__password = super().complex_algorithm(password)
		self.name = name

	def get_pass(self):
		return self.__password

New_user_SRP = UserSRP("Andy", "ThisIsMyPasword")
print(f"User: {New_user_SRP.name}, Password: {New_user_SRP.get_pass()}" )

# Now you can make changes to the encryption algorithm in the class that is in charge of that
#    so you wont touch the USER_SRP class for this changes and viceversa
