def validate_pin(pin):
    if pin.isnumeric():
        return len(pin) == 4 or len(pin) == 6
    else: return False