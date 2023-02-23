import random

seen_sets = set()
duplicated = False
duplicate_times = 0

for i in range(10000):
    for i in range(100):
        cards = sorted(random.sample(range(1, 13), 8))
        card_set = tuple(cards)
        if card_set in seen_sets:
            duplicated = True
        else:
            seen_sets.add(card_set)
            duplicated = False
    if duplicated == True:
        duplicate_times += 1

print(duplicate_times)

# 計算10000次中，重複兩組牌的機率
# prob_duplicate = "{0:.0%}".format(num_duplicates / 10000)

# print(prob_duplicate)

# print(seen_sets)