def count_positive_pairs(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

print(count_positive_pairs(2, -5, -3)) 
print(count_positive_pairs(7, 2, -9)) 
