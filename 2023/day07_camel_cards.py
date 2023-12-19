'''
Advent of code day 07: https://adventofcode.com/2023/day/7
'''
import functools

filename = './inputs/day07_camel_cards.in'

def foo(s):
    hand, bet = s.split()
    return (hand, int(bet))


def hand_strength(hand):
    cards = '23456789TJQKA'      # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    inventory = [0] * len(cards)

    for i in range(len(cards)):
        inventory[i] = hand.count(cards[i])

    if inventory.count(5) == 1:             
        return 7        #   Five of a kind
    elif inventory.count(4) == 1:
        return 6        #   Four of a kind
    elif inventory.count(3) == 1 and inventory.count(2) == 1: 
        return 5        #   Full house
    elif inventory.count(3) == 1 and inventory.count(1) == 2:
        return 4        #   Three of a kind
    elif inventory.count(2) == 2 and inventory.count(1) == 1:
        return 3        #   Two pair
    elif inventory.count(2) == 1 and inventory.count(1) == 3:
        return 2        #   One pair
    elif inventory.count(1) == 5: 
        return 1        #   High card


def cmp_hands_part_one(a, b):
    card_strength = '23456789TJQKA'  #   weakest to strongest card

    hand_a_strength = hand_strength(a[0])
    hand_b_strength = hand_strength(b[0])

    if hand_a_strength == hand_b_strength:
        for i in range(5):
            if card_strength.find(a[0][i]) > card_strength.find(b[0][i]): return 1
            if card_strength.find(a[0][i]) < card_strength.find(b[0][i]): return -1
    
    return 1 if hand_a_strength > hand_b_strength else -1


def cmp_hands_part_two(a, b):
    card_strength = 'J23456789TQKA'  #   weakest to strongest card

    #   Transform the "J" to another card and see which hand is the strongest
    hand_a_strength = 0
    hand_b_strength = 0
    for s in card_strength:
        #   J replaces another card
        hand_a_strength = max(hand_a_strength, hand_strength(a[0].replace('J', s)))
        hand_b_strength = max(hand_b_strength, hand_strength(b[0].replace('J', s)))

    if hand_a_strength == hand_b_strength:
        for i in range(5):
            if card_strength.find(a[0][i]) > card_strength.find(b[0][i]): return 1
            if card_strength.find(a[0][i]) < card_strength.find(b[0][i]): return -1
    
    return 1 if hand_a_strength > hand_b_strength else -1


def winnings(hands):
    total_winning = 0
    for i in range(len(hands)):
        total_winning += hands[i][1] * (i + 1)

    return total_winning


def part_one(hands):
    sorted_hands = sorted(hands, key=functools.cmp_to_key(cmp_hands_part_one))
    print(winnings(sorted_hands))


def part_two(hands):
    sorted_hands = sorted(hands, key=functools.cmp_to_key(cmp_hands_part_two))
    print(winnings(sorted_hands))


if __name__ == '__main__':
    with open(filename, 'r') as f:
        lines = f.readlines()

    hands = list(map(foo, lines))
    part_one(hands)
    part_two(hands)