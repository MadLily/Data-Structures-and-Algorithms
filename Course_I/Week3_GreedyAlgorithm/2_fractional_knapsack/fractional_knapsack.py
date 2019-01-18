# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_value = [ values[i]/weights[i] for i in range(len(values))]
    def argsort(seq):
        return sorted(range(len(seq)), key=seq.__getitem__)
    rank = argsort(unit_value)
    rank.reverse()
    i = 0
    while capacity >= 0 and i < len(unit_value) :
        take = min(capacity, weights[rank[i]])
        value += take * unit_value[rank[i]]
        i += 1 
        capacity -= take
        
    # write your code herew

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

    
def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)