class CheckerGame:
    def solution(B):
        x, y, n = 0, 0, len(B)

        for i in range(n):
            for j in range(n):
                if B[i][j] == 'O':
                    x = i
                    y = j

        kill = 0

        while x > 1:
            if 1 < y < n - 2:
                if B[x-1][y-1] == 'X' and B[x-2][y-2] == '.':
                    kill += 1
                    x -= 2
                    y -= 2
                elif B[x-1][y+1] == 'X' and B[x-2][y+2] == '.':
                    kill += 1
                    x -= 2
                    y += 2

        return kill

    B1 = [''] * 6
    B1[0] = '..X...'
    B1[1] = '......'
    B1[2] = '....X.'
    B1[3] = '.X....'
    B1[4] = '..X.X.'
    B1[5] = '...O..'

    B2 = [''] * 5
    B2[0] = 'X....'
    B2[1] = '.X...'
    B2[2] = '..O..'
    B2[3] = '...X.'
    B2[4] = '.....'

    print(solution(B1))
