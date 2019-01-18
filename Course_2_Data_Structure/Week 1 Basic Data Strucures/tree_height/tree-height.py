# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.child = [[] for i in range(self.n)]
        self.root = -1
        self.level = [1] * self.n

    def compute_height(self):
        # Replace this code with a faster implementation
        for i in range(self.n):
            if self.parent[i] == -1:
                self.root = i
            else:
                self.child[self.parent[i]].append(i)
        q = self.child[self.root]
        maxHeight = 0
        while len(q)!=0:
            now = q.pop(0)
            self.level[now] = self.level[self.parent[now]] + 1
            if len(self.child[now] )>0:
                q.extend(self.child[now])
        maxHeight = max(self.level)
        return maxHeight





def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
