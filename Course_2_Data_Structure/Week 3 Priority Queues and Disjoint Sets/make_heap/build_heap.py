# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])
#        print(self._data)

#    def SiftDown(self,i):
#        left = True
#        right = True
#        while (i <= len(self._data)//2-1) and (left or right):
#            ind_min = i
#            l = 2 * i + 1
#            if l < len(self._data) and self._data[l] < self._data[ind_min]:
#                ind_min = l
#            else:
#                left = False
#            r = 2 * i + 2
##            print(l,r)
#            if r < len(self._data) and self._data[r] < self._data[ind_min]:
#                ind_min = r
#            else:
#                right = False
#            if ind_min != i:
#                self._swaps.append((i, ind_min))
#                self._data[i], self._data[ind_min] = self._data[ind_min], self._data[i]
#                i = ind_min

    def SiftDown(self,i):
        ind_min = i
        l = 2 * i + 1
        if l < len(self._data) and self._data[l] < self._data[ind_min]:
            ind_min = l
        r = 2 * i + 2
        #            print(l,r)
        if r < len(self._data) and self._data[r] < self._data[ind_min]:
            ind_min = r
        if ind_min != i:
            self._swaps.append((i, ind_min))
            self._data[i], self._data[ind_min] = self._data[ind_min], self._data[i]
            self.SiftDown(ind_min)



    def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
#    for i in range(len(self._data)):
#      for j in range(i + 1, len(self._data)):
#        if self._data[i] > self._data[j]:
#          self._swaps.append((i, j))
#          self._data[i], self._data[j] = self._data[j], self._data[i]
        for i in range(len(self._data)//2-1,-1,-1):
#            print(list(range(len(self._data)//2-1,-1,-1)),i)
            self.SiftDown(i)
  


    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
