"""Functions to help play and score a game of blackjack."""
sepuluhcoy = "JQK10"

def value_of_card(card):
    if card == "A":
        return 1
    if card in sepuluhcoy:
        return 10
    return int(card)
        
def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_two) > value_of_card(card_one):
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two =="A":
        return 1
    if 21 - (value_of_card(card_one) + value_of_card(card_two)) >= 11:
        return 11
    if 21 - (value_of_card(card_one) + value_of_card(card_two)) < 11:
        return 1

def is_blackjack(card_one, card_two):
    if (card_one == "A" or card_two == "A") and (card_one in sepuluhcoy or card_two in sepuluhcoy):
        return True
    return (value_of_card(card_one) + value_of_card(card_two)) == 21
    
def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    return (9 <= value_of_card(card_one) + value_of_card(card_two) <= 11)