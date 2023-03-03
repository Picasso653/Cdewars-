def is_valid_IP(strng):
    octets = strng.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        try:
            int_octet = int(octet)
            if int_octet < 0 or int_octet > 255 or str(int_octet) != octet:
                return False
        except ValueError:
            return False
    return True
