import random
playerIn = True
dealerIn = True
# Deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []
# Deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
# Calculate the total of each hand
def determineTotal(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
        while ace_11s and total > 21:
            total -= 10
            ace_11s -= 1
# Check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
# Game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"You have {playerHand}, for a total of {determineTotal(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if determineTotal(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if determineTotal(playerHand) >= 21:
        break
    elif determineTotal(dealerHand) >= 21:
        break

if determineTotal(playerHand) == 21:
    print(f"\n You have {playerHand} for a total of {playerHand} and the dealer has {dealerHand} for a total of{determineTotal(dealerHand)}")
    print("Blackjack! You win!")
elif determineTotal(dealerHand) == 21:
    print(f"\n You have {playerHand} for a total of {determineTotal(playerHand)} and the dealer has {dealerHand} for a total of{determineTotal(dealerHand)}")
    print("Blackjack! Dealer wins!")
elif determineTotal(playerHand) > 21:
    print(f"\n You have {playerHand} for a total of {determineTotal(playerHand)} and the dealer has {dealerHand} for a total of{determineTotal(dealerHand)}")
    print("You bust! Dealer wins!")
elif determineTotal(dealerHand) > 21:
    print(f"\n You have {playerHand} for a total of {determineTotal(playerHand)} and the dealer has {dealerHand} for a total of{determineTotal(dealerHand)}")
    print("Dealer busts! You win!")
elif 21 - determineTotal(dealerHand) < 21 - determineTotal(playerHand):
    print(f"\n You have {playerHand} for a total of {determineTotal(playerHand)} and the dealer has {dealerHand} for a total of{determineTotal(dealerHand)}")
    print("Dealer wins!")
elif 21 - determineTotal(dealerHand) > 21 - determineTotal(playerHand):
    print(f"\n You have {playerHand} for a total of {determineTotal(playerHand)} and the dealer has {dealerHand} for a total of{determineTotal(dealerHand)}")
    print("You win!")

