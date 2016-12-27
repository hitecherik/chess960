from random import randint
from sys import argv

def generatePosition():
	PIECES = ["N", "N", "B", "B", "R", "R", "Q", "K"]
	layout = []
	positionValid = False
	
	while not positionValid:
		layout = []
		pieces = PIECES[:]
		bishops = 0
		rooksAndKing = []
		
		for i in range(8):
			layout.append(pieces.pop(randint(0, len(pieces)-1)))
			
			if layout[-1] == "B":
				bishops += i % 2
			elif layout[-1] in ["R", "K"]:
				rooksAndKing.append(layout[-1])
		
		positionValid = (rooksAndKing[1] == "K" and bishops == 1)
	
	return layout


def main():
	try:
		for i in range(int(argv[-1])):
			print(" ".join(generatePosition()))
			print("-"*15)
	except ValueError:
		argv.append(1)
		main()


if __name__ == "__main__":
	main()