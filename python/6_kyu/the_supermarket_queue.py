def queue_time(customers, n):
    if customers == []:  return 0
    if len(customers) <= n: return max(customers)
    if n == 1: return sum(customers)
    tills = [0] * n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
    return max(tills)

        