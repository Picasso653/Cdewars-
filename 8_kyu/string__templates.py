def build_string(*args):
    return "I like {0}!".format(", ".join(args))
#     return f"I like {(', '.join(args))}!"