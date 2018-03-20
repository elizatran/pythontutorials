def square(num):
	return num * num

# number = 12
# print (square(number))

def convertTemp (temp, scale):
	if scale =="c":
		return (temp - 32.0) * (5.0/9.0)
	elif scale =="f":
		return temp * 9.0/5.0 + 32
def printLetter(str, num):
	i = 0
	for lett in str:
		i += 1
		if i == num:
			print(lett)

# temp= int (input("Enter a temparature: "))
# scale = input("Enter the scale to convert to: ")
# converted = convertTemp (temp, scale)
# print(" The converted temp is: " + str(converted))

word = input("Enter the word: ")
letter = int(input ("Enter the number of letter in word to print: "))
printLetter(word, letter)

