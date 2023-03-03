def most_frequent_item_count(collection):
    if collection==[]:
        return 0
    else:
        unique_numbers =[]
        most_number = []
        for i in collection:
            if i not in unique_numbers:
                unique_numbers.append(i)
        for j in unique_numbers:
            mumber = collection.count(j)
            most_number.append(collection.count(j))
        return max(most_number)
            