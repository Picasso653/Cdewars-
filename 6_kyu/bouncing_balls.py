def bouncing_ball(h, bounce, window):
    if h>0 and 0<bounce<1 and window<h:
        x = 0
        while h>window:
            h *= bounce
            x += 2
        return x-1
    return -1