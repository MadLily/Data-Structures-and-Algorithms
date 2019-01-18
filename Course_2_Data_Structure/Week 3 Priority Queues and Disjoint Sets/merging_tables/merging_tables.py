# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    if table != parent[table]:
         parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans
    global rank
    global parent
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return ans
    else:
        if rank[realDestination] >= rank[realSource]:
            lines[realDestination] += lines[realSource]
            lines[realSource] = 0
            parent[realSource] = realDestination
            if rank[realDestination] == rank[realSource]:
                rank[realDestination] += 1
            ans = max(ans,lines[realDestination])

#            print(lines[realDestination],'hap',max(ans,lines[realDestination]))
        else:
            lines[realSource] += lines[realDestination]
            lines[realDestination] = 0
            parent[realDestination] = realSource
            ans = max(ans,lines[realSource])
#            print(lines[realSource],'lalala',max(ans,lines[realSource]))
    return ans

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ans  = merge(destination - 1, source - 1)
#    print (rank,parent)
#    ans = max(lines + [ans])
    print(ans)
    
