def past(h, m, s):
    hrs = h * 3600000
    mins = m * 60000
    sec = s * 1000
    return (hrs + mins + sec)