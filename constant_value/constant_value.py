def solve(s):
    def substring_value(sub):
        return sum(ord(c) - ord('a') + 1 for c in sub)
    
    consonants = 'bcdfghjklmnpqrstvwxyz'
    max_value = 0
    current_value = 0
    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    max_value = max(max_value, current_value)  
    return max_value


print(solve("zodiacs")) 
print(solve("strength")) 
