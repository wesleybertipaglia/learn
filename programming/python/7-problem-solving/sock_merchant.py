def sock_merchant(stock_list: list) -> int:
    color_count = {} # Red: 2, Blue: 1, Green: 1
    pairs = 0
    
    for sock in stock_list:
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1
    
    for count in color_count.values():
        pairs += count // 2
    
    return pairs