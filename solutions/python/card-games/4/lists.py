"""Functions for tracking poker hands and assorted card tasks."""

def get_rounds(number):
    kocak = []
    for ronde in range (3):
        kocak.append(number+ronde)
    return kocak

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    rerata = sum(hand)/len(hand)
    median = hand[len(hand)//2]
    return ((hand[0] + hand[-1])/2) == rerata or median == rerata

"""aneh lukh"""
def average_even_is_average_odd(hand):
    totalgenap = 0
    totalganjil = 0
    if len(hand) % 2 != 0:
        averagegenap = len(hand)//2 + 1
        averageganjil = len(hand)//2
    else:
        averagegenap = averageganjil = len(hand)/2
    for genap in hand[::2]:
        totalgenap += genap
    for ganjil in hand[1::2]:
        totalganjil += ganjil
    return totalgenap/averagegenap == totalganjil/averageganjil
    
def maybe_double_last(hand):
    if hand[-1] == 11:
        return hand[:-1] + [22]
    return hand
