def xo(s):
    # Define the vriables involved
    numx = 0
    numo = 0
    # Create a loop 
    for i in s:
        if i.lower() == 'x':
            numx += 1
        elif i.lower() == 'o':
            numo += 1
    # Return answer...
    return numx == numo