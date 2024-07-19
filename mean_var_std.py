import numpy as np

def calculate(digits_list):
    
    if len(digits_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(digits_list).reshape(3, 3)
    
    mean = [[float(x) for x in arr.mean(axis=0)], 
            [float(x) for x in arr.mean(axis=1)], 
            float(arr.mean())]
    variance = [[float(x) for x in arr.var(axis=0, ddof=1)], 
                [float(x) for x in arr.var(axis=1, ddof=1)], 
                float(arr.var(ddof=1))]
    std_dev = [[float(x) for x in arr.std(axis=0, ddof=1)], 
              [float(x) for x in arr.std(axis=1, ddof=1)], 
              float(arr.std(ddof=1))]
    max_vals = [[int(x) for x in arr.max(axis=0)], 
               [int(x) for x in arr.max(axis=1)], 
               int(arr.max())]
    min_vals = [[int(x) for x in arr.min(axis=0)], 
               [int(x) for x in arr.min(axis=1)], 
               int(arr.min())]
    sums = [[int(x) for x in arr.sum(axis=0)], 
           [int(x) for x in arr.sum(axis=1)], 
           int(arr.sum())]
    
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_vals,
        'min': min_vals,
        'sum': sums
    }