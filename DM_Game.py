import random

def actionRoll(roll):
	response = ""
	if roll == 1:
		response = "CRIT FAIL... Sorry, bud."
		print(response)
	if roll == 20:
		response = "CRITICAL HIT! You win games forever!!!"
		print(response)
	if roll > 1 & roll < 11:
		response = "Not quite... Not great, but.... You know."
		print(response)
	if roll < 20 & roll > 10:
		response = "Well hot dog, you do 10 points of whatever damage applies to whatever you said earlier!"
		print(response)
	return response

print("Hello, adventurer. You come upon a bridge with a troll, who asks riddles three. What do you do?")
userinput = raw_input("Please answer in '__ the __' format: ")

print("You attempt to " + userinput)
result = random.randint(1, 20)
print("Dice Result: " + str(result))
actionRoll(result)
