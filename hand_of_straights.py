
def solution(hand, groupSize):
    card_counts = {}
    hand.sort()
    for card in hand:
        if card not in card_counts:
            card_counts[card] = 1
        else:
            card_counts[card] += 1

    while card_counts:
        first_card = next(iter(card_counts))

        x = first_card
        while x < first_card + groupSize:
            if x not in card_counts:
                return False

            count = card_counts[x]
            if count == 1:
                del card_counts[x]
            else:
                card_counts[x] -= 1
            x += 1

    return True