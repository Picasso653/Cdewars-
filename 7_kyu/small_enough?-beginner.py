def small_enough(array, limit):
    return True if [i for i in array if i <= limit] == array else False