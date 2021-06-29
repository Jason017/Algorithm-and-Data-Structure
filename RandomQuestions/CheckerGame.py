class CheckerGame:
	def solution(B):
		x, y, n = 0, 0, len(B)

		for i in range(n):
			for j in range(n):
				if B[i][j] == 'O':
					x = i
					y = j

		kill = 0

		while x > 2:
			if y < n - 2:
				if B[x-1][y-1] == 'X' and B[x-2][y-2] == '.':
					kill += 1
					x -= 2
					y -= 2
			elif y > 1:
				if B[x-1][y+1] == 'X' and B[x-2][y+2] == '.':
					kill += 1
					x -= 2
					y += 2
		return kill





	B = [''] * 6
	B[0] = '..X...'
	B[1] = '......'
	B[2] = '....X.'
	B[3] = '.X....'
	B[4] = '..X.X.'
	B[5] = '...O..'

	B1 = [''] * 5
	B1[0] = 'X....'
	B1[1] = '.X...'
	B1[2] = '..O..'
	B1[3] = '...X.'
	B1[4] = '.....'