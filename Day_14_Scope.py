class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        size = len(a)
        for i in range(0,size):
            for j in range(i+1, size):
                difference = abs(a[i]-a[j])
                self.maximumDifference = max(difference, self.maximumDifference)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)