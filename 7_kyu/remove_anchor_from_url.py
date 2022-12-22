def remove_url_anchor(url):
    for i,j in enumerate(url):
        if j == "#":
            return url[:i]
    return url