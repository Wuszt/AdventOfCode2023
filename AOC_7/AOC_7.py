from collections import Counter
def Calc(hands):
    ranks, crds = [], ['0', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for _ in range(7): ranks.append([])
    for hand in hands:
        jokers = hand[0].count('0')
        cards = {**{0: 0}, **dict(Counter(Counter(hand[0].replace('0', '')).values()))}
        for i in range(4, -1, -1):
            if i in cards:
                cards[i + jokers] = cards.get(i + jokers, 0) + 1

                cards[i] -= 1
                if cards[i] == 0: cards.pop(i)
                break

        if 5 in cards: ranks[6].append(hand)
        elif 4 in cards: ranks[5].append(hand)
        elif 3 in cards and 2 in cards: ranks[4].append(hand)
        elif 3 in cards: ranks[3].append(hand)
        elif 2 in cards and cards[2] == 2: ranks[2].append(hand)
        elif 2 in cards: ranks[1].append(hand)
        else: ranks[0].append(hand)

    def SortFunc(r):
        sum = 0
        for c in r[0]: sum = 100 * sum + crds.index(c)
        return sum

    result = 0
    multiplier = 1
    for rank in ranks:
        rank.sort(key=SortFunc)
        for r in rank:
            result += int(r[1]) * multiplier
            multiplier += 1
    print(result)

Calc([x.strip().split(' ') for x in open("input.txt", "r").readlines()])
Calc([[x[0].replace('J', '0'),x[1]] for x in [x.strip().split(' ') for x in open("input.txt", "r").readlines()]])