def key_get(my_dict):
	# 키 존재 여부 확인

	user_input = input("과일 이름: ")

	v = my_dict.get(user_input)

	if v == None:
		print("False")
	else:
		print("True")
	print()

def value_get(my_dict):
	# 값으로 키 찾기

	user_input = int(input("값 입력: "))

	value = [k for k, v in my_dict.items() if v == user_input]

	if value:
		print(value)
		print()
	else:
		print(None)
		print()

def delete_dict(my_dict):
	my_dict_copy = my_dict.copy()

	user_input = input("값 입력: ")

	del my_dict[user_input]
	my_dict_copy.pop(user_input, None)

	print(my_dict)
	print(my_dict_copy)
	print()

def update_dict(my_dict):
	dict1 = {}

	fru_user_input = input("과일: ")
	int_user_input = int(input("수량: "))

	if fru_user_input in my_dict:
		dict1[fru_user_input] = int_user_input
		my_dict.update(dict1)
		print(my_dict)
		print()
	else:
		dict1[fru_user_input] = int_user_input
		my_dict.update(dict1)
		print(my_dict)
		print()

def dif_dict(dict1, dict2):
	dict1_only = {key: dict1[key] for key in dict1.keys() - dict2.keys()}
	dict2_only = {key: dict2[key] for key in dict2.keys() - dict1.keys()}

	print(f"dict1에만 존재: {dict1_only}")
	print(f"dict2에만 존재: {dict2_only}")

def sort_key(my_dict):
	print(dict(sorted(my_dict.items())))

def sort_value(my_dict):
	print(dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)))

def main():
	my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
	dict1 = {'a': 1, 'b': 2, 'c': 3}
	dict2 = {'b': 2, 'd': 4}

	#key_get(my_dict)
	value_get(my_dict)
	#delete_dict(my_dict)
	#update_dict(my_dict)
	#dif_dict(dict1, dict2)
	#sort_key(my_dict)
	#sort_value(my_dict)

if __name__ == "__main__":
	main()