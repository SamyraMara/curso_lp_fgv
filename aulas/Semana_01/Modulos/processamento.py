PI = 3.14159

def normalize_stddev(value, mean=0.0, stddev=1.0):
    return (value - mean) / stddev

def normalize_minmax(value, data_min, data_max, min_val=0.0, max_val=1.0):
    normalized_value = (value - data_min) / (data_max - data_min)
    return normalized_value * (max_val - min_val) + min_val


print("oi")
print("colé mano bráu")

__name__ == "__main__"