from itertools import combinations
from typing import List


def combinationOfSum(nums: List[int], target: int) -> List[tuple]:
    '''
    Given an unsorted list of N numbers, write a program/function 
    that will return all combinations of these numbers that sum 
    up to a number Y.
    '''
    nums.sort()
    ans = set()
    i, j = 0, len(nums) - 1

    while j >= i + 1:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            ans.add((nums[i], nums[j]))
            i += 1
            j -= 1

    return list(ans)


def combinationOfSum2(nums: List[int], target: int) -> List[tuple]:
    def findCombinations(nums, target, N):
        return [i for i in combinations(nums, N) if sum(i) == target]
    ans = []
    nums.sort()
    for i in range(2, len(nums)+1):
        ans += findCombinations(nums, target, i)
    return list(set(ans))


nums = [1, 2, 3, 4, -3, -1, 0, 4, -6]
target = 3
print([i for i in combinationOfSum2(nums, target) if len(i) == 2])
print(combinationOfSum(nums, target))


def coinsValue(coins: List[int], V: int) -> int:
    '''
    Given some value V that is between 0 - 100 and predefined,
    and unique coins denominations of values A,B, and C, write
    a function that will return the minimum value of coins 
    needed to achieve a value of V.
    '''
    dp = [V+1]*(V+1)
    dp[0] = 0

    for i in range(V+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)

    return -1 if dp[V] > V else dp[V]


'''
Question5

Create/pick an ideal data structure to represent a contact list 
and describe its trade offs and why it was picked.
'''


class Contact:
    def __init__(self, name: str, phoneNumber: int, email: str) -> None:
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email


class ContactList:
    def __init__(self) -> None:
        self.table = {}
        self.nContacts = 0

    def add_contact(self, newContact: Contact, addBy: str) -> None:
        if addBy == 'name':
            self.table[newContact.name] = newContact
            self.nContacts += 1
        elif addBy == 'phone number':
            self.table[newContact.phoneNumber] = newContact
            self.nContacts += 1
        elif addBy == 'email':
            self.table[newContact.email] = newContact
            self.nContacts += 1

    def search_contact(self, input: str, searchBy: str) -> Contact:
        if searchBy == 'name' or searchBy == 'email':
            return self.table[input]
        elif searchBy == 'phone number':
            return self.table[int(input)]


'''
Question6: 

A site allows a user to customize their profile, in which they 
can set the shape of a logo to be between a circle, triangle, 
square, pentagon and hexagon, along with the logo being either 
red, green, blue, or any combination of them. In addition to 
this, it allows the user to have four rotational options for 
the logo (upright, turned left, turned right, or upside down). 
Create a data structure along with accompanying get/set 
functions that will store this information in the most space 
efficient way.
'''


class logo:
    def __init__(self, userID: int, shape: str, color: str, rotationalOption: str) -> None:
        self.userID = userID
        self.shape = shape
        self.color = color
        self.rotationalOption = rotationalOption

    def getShape(self) -> str:
        return self.shape
