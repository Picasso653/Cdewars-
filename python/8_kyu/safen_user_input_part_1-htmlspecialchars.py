def html_special_chars(data): 
    new = data.replace('&', '&amp;').replace('>', '&gt;').replace('"', '&quot;').replace('<', '&lt;')
    return new