def repeated_string(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)    
    remainder = n % len(s)    
    
    total_a_full_repeats = full_repeats * count_a_in_s
    count_a_in_remainder = s[:remainder].count('a')    
    return total_a_full_repeats + count_a_in_remainder