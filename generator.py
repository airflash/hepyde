import random

icons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
icons = [0, 1, 2, 3, 4, 5, 6, 7]

REELS = 5
STRIPE = 3


def getRandomCombination():
	reels = []
	for i in range(REELS):
		stripe = []
		for j in range(STRIPE):
			stripe.append(random.choice (icons))
		reels.append(stripe)
	return reels

def printFormatted(comb):
	print(comb[0][0], comb[1][0], comb[2][0], comb[3][0], comb[4][0])
	print(comb[0][1], comb[1][1], comb[2][1], comb[3][1], comb[4][1])
	print(comb[0][2], comb[1][2], comb[2][2], comb[3][2], comb[4][2])
