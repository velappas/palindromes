# Assignment/Palindromes
# Victoria Lappas

import sys

# Define findPalindromes(string) receives a formatted string as a parameter and then 
# searches this string for any palindromes. There are two cases for palindromes: an 
# even length string and an odd length string. Once this function determines a 
# palindrome, it adds it to a list along with the starting position and length. 
def findPalindromes(string):
	# strings containing one character are not considered palindromes
	if len(string) == 1:
		noPalindromesFound()
		
	list = []
	i = 1
	while(i < len(string)):
		#case 1: even length
		iterator = 0
		palindrome = ""
		while(((i + iterator) < len(string)) and ((i - iterator - 1) >= 0) and string[i + iterator] == string[i - iterator - 1]):
			palindrome = string[i-1-iterator] + palindrome + string[i + iterator]
			list.append([palindrome, (i-1-iterator), len(palindrome)])
			iterator = iterator + 1
		
		#case 2: odd length
		iterator = 1
		palindrome = string[i]
		while(((i + iterator) < len(string)) and ((i-iterator) >= 0) and string[i+iterator] == string[i-iterator]):
			palindrome = string[i-iterator] + palindrome + string[i + iterator]
			list.append([palindrome, (i-iterator), len(palindrome)])
			iterator = iterator + 1
		i = i + 1
		
	return list


# Define printSolution(matrix) receives a matrix as a parameter and then prints 
# this matrix to the console. The matrix is formatted here to suit the requirements 
# of the problem. It is primarily sorted by the length (decreasing) and then sorted
# in increasing order of the palindrome's position as per the example result provided.
def printSolution(matrix):
	matrix.sort(key=lambda x:(x[2] * -1 , x[1]))
	for x in range(len(matrix)):
		print(matrix[x][0] + "," + str(matrix[x][1]) + "," + str(matrix[x][2]))


# Define noPalindromesFound() is called when there are no palindromes found in the 
# input and will end the program. 
def noPalindromesFound():
	print("There were no palindromes found. ")
	exit(0)


# Define formatString() receives the arguments passed in by the command line 
# and formats them into a string. Spaces are removed and all characters 
# are converted into upper case for consistency.
def formatString():
	args = len(sys.argv)
	i = 1
	string = ""
	while(i < args):
		string += sys.argv[i].upper()
		i = i + 1
	return string
	
	
# Define checkArguments() checks to ensure at least one string was entered by the user.
# If no arguments are found, the user is notified and the program exits. 
def checkArguments():
	if len(sys.argv) == 1:
		print("Please enter at least 1 string to be analyzed.")
		exit(-1) 
	
	
def main():
	checkArguments()
	inputString = formatString()
	palindromeList = findPalindromes(inputString)
	
	if(palindromeList != []):
		printSolution(palindromeList)
	else:
		noPalindromesFound()

		
main()

