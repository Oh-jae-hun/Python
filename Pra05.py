class Friend:
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone
	def get_name(self):
		return self.name
	def get_phone(self):
		return self.phone
	def set_phone(self, phone):
		self.phone = phone
	def show_info(self):
		print("이름 : ", self.name)
		print("전화번호 : ", self.phone)
  
friend_list = []
friend_list.append(Friend('허현욱', '010-9876-5432'))
friend_list.append(Friend('이선준', '010-7410-0258'))
friend_list.append(Friend('장지우', '010-9630-0258'))
friend_list.append(Friend('허진욱', '010-4321-1234'))
 
 
print(friend_list)                   