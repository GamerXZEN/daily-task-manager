from json import loads

with open("questions.json", "r") as file:
	content = file.read()

data = loads(content)

for question in data:
	print(question["question_text"])
	for index, alternative in enumerate(question["alternatives"]):
		print(f"{index + 1}. {alternative}")
	user_choice = int(input("Enter your answer: "))
	question["user_choice"] = user_choice

print(data)
