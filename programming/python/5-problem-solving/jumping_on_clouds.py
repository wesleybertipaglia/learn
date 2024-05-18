def jumping_on_clouds(c):
    n = len(c)
    jumps = 0
    i = 0
    
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    
    return jumps