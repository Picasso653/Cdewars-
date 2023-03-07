def title_case(title, minor_words=''):
    if title == '':
        return ''
    result = title.split(' ')[0].title() + ' '
    for i in title.split(' ')[1:]:
        if i.lower() in minor_words.lower().split(' '):
            result += i.lower()+ ' '
        else:
            result += i.title()+ ' '
    return result.strip()