paytable = {
	0: [10, 5, 3],
	1: [15, 10, 5],
	2: [20, 15, 10],
	3: [50, 30, 15],
	4: [80, 50, 30],
	5: [100, 75, 50],
	6: [150, 120, 100],
	7: [300, 200, 150],
	8: [500, 300, 100],
	9: [750, 500, 300],
	10: [1000, 700, 500],
	11: []
}

lines = [
		[1,1,1,1,1], 
		[0,0,0,0,0], 
		[2,2,2,2,2], 

		[0,1,2,1,0], 
		[2,1,0,1,2], 

		[1,0,0,0,1], 
		[1,2,2,2,1], 

		[0,2,2,2,0], 
		[2,0,0,0,2],

		[0,2,0,2,0], 
		[2,0,2,0,2],

		[0,1,1,1,0], 
		[2,1,1,1,2],

		[0,0,1,0,0], 
		[2,2,1,2,2],

		[0,0,2,0,0], 
		[2,2,0,2,2],

		[0,0,1,2,2], 
		[2,2,1,0,0],

		[0,1,0,1,0], 
		[2,1,2,1,2],

		[0,2,2,2,0], 
		[2,0,0,0,2],

		[1,2,0,2,1], 
		[1,0,2,0,1]
		]

def calculateWin(combination):
	rezult = []
	total = 0
	for lineId, line in enumerate(lines):
		lineRez = {}
		chain = 1
		for i, index in enumerate(line):
			if i == 0:
				startValue = combination[i][index]	# 1 reel
				#print ('start value: ', startValue)
			else:
				if combination[i][index] == startValue:
					chain += 1
				if combination[i][index] != startValue:
					break

		win = 0
		if 5-chain < len(paytable[startValue]):
			win = paytable[startValue][5-chain]
		
		if win > 0:
			lineRez['win'] = win
			lineRez['lineId'] = lineId
			rezult.append(lineRez)
			total += win

	return rezult

def getTotal(wins):
	total = 0
	for win in wins:
		total += win['win']
	return total

def getPaytable():
	return paytable

def getLines():
	return lines