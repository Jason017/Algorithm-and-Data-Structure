class AirplaneSeatReservation:
    def solution(N, S):
        taken = S.split()
        seats = {}
        letters = ['B','C','D','E','F','G','H','J']

        if S is None or len(S) == 0: return 2*N

        def get(letters, taken):
            for i in letters:
                if i in taken:
                    return True
            return False

        for x in taken:
            if x not in seats:
                seats[x] = [1,1,1]
            if get(letters[:4], x) and seats[x][0]:
                seats[x][0] -= 1
            if get(letters[2:6], x) and seats[x][1]:
                seats[x][1] -= 1
            if get(letters[4:], x) and seats[x][2]:
                seats[x][2] -= 1

        All = [sum(i) for i in seats.values()]
        a = All.count(1) + All.count(2)
        b = All.count(3)

        return a + (N-len(seats.keys())+b)*2