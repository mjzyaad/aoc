import pprint 

filename = './inputs/day04_scratchcards.in'

def part_one():
    with open(filename, 'r') as f:
        answer = 0
        for line in f.readlines():
            line = line.strip()
            _, cards = line.split(':')
            
            str_winning_cards, str_guessed_cards = cards.split('|')
            winning_cards = set(map(int, str_winning_cards.split()))
            guessed_cards = set(map(int, str_guessed_cards.split()))

            common_cards = winning_cards.intersection(guessed_cards)
            
            if len(common_cards) > 0:
                points = 2 ** (len(common_cards) - 1)
                answer += points

        print('Answer to part 1 =', answer)


def part_two():
    with open(filename, 'r') as f:
        answer = 0
        card_number = 0
        lines = f.readlines()
        cards_inventory = [1] * (len(lines) + 1)
        cards_inventory[0] = 0

        for line in lines:
            line = line.strip()
            _, cards = line.split(':')
            
            card_number += 1
            str_winning_numbers, str_guessed_numbers = cards.split('|')
            winning_numbers = set(map(int, str_winning_numbers.split()))
            guessed_numbers = set(map(int, str_guessed_numbers.split()))

            common_numbers = winning_numbers.intersection(guessed_numbers)
            
            for i in range (1, len(common_numbers) + 1):
                if card_number + i < len(cards_inventory):
                    cards_inventory[card_number + i] += cards_inventory[card_number]     # add copies

        answer = sum(cards_inventory)
        print('Answer to part 2 =', answer)


if __name__ == '__main__':
    part_one()
    part_two()
