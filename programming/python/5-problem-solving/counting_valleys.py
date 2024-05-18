def counting_valleys(path):
    valleys = 0
    altitude = 0
    
    for step in path:
        if step == "U":
            altitude += 1
        elif step == "D":
            altitude -= 1    
        if altitude == 0 and step == "U":
            valleys += 1
    return valleys