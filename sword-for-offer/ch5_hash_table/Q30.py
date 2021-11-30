from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_to_location = {}
        self.num = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_to_location.keys():
            return False
        self.num_to_location[val] = len(self.num)
        self.num.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.num_to_location.keys():
            location = self.num_to_location.get(val)
            self.num_to_location[self.num[-1]] = location
            self.num_to_location.pop(val)
            self.num[location] = self.num[-1]
            self.num.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = randint(0, len(self.num) - 1)
        return self.num[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomSet = RandomizedSet()
randomSet.insert(1)
randomSet.remove(2)
randomSet.insert(2)
randomSet.getRandom()
randomSet.remove(1)
randomSet.insert(2)
randomSet.getRandom()
