def hex_to_rgb(hex_color):
    # ?
    
    r = int(hex_color[:2], 10)
    g = int(hex_color[2:4], 10)
    b = int(hex_color[4:], 10)
    print(r,g,b)
    return r, g, b
