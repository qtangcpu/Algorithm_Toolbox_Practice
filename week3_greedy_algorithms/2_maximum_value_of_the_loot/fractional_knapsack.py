# Uses python3
import sys

def get_optimal_value(n,capacity, weights, values):
    value = 0.
    '''
    df = pd.DataFrame(weights, columns=['weights'])
    df1 = pd.concat([df, pd.DataFrame(values, columns=['values'])], axis=1)
    df1['ratio'] = df1['values'] / df1['weights']
    df1 = df1.sort_values(by='ratio', ascending=False).reset_index(drop=True)
    total_Weight = df1.weights.sum()
    '''
    ratio = [i / j for i, j in zip(values, weights)]
    total_Weight = sum(weights)
    for i in range(n):
        if total_Weight <= 0 or capacity <= 0:
            return value
        pop_index = ratio.index(max(ratio))
        w = min(capacity, weights[pop_index])
        value = value + w * ratio.pop(pop_index)
        total_Weight = total_Weight - w
        capacity = capacity - w
        weights.pop(pop_index)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n,capacity, weights, values)
    print("{:.10f}".format(opt_value))

