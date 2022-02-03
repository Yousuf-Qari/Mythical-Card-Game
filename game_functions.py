import card_deck
import random
import csv

def write_and_read_csv(player_1_wins, player_2_wins, draws, file_name):
    try:
        with open (file_name, 'w', encoding='UTF8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',', quotechar = None, quoting = csv.QUOTE_NONE)
            writer.writerow(['Player 1 has ' + str(player_1_wins) + ' wins.'])
            writer.writerow(['Player 2 has ' + str(player_2_wins) + ' wins.'])
            writer.writerow(['There are ' + str(draws) + ' draws.'])         
        with open(file_name, 'r', newline= '') as csv_file:
            reader = csv.reader(csv_file,delimiter = ',', quotechar = None, quoting = csv.QUOTE_NONE)
            for row in reader:
                print(*row)
            print('')
        csv_file.close()
    except FileNotFoundError:
        print(file_name, 'is missing')
        
def trade_request(player_cards):
    trade_bool = True
    while trade_bool:
        trade_question = str(input('\n' + player_cards['player'] + ', trade or stick?\n'))
        trade_question = trade_question.lower()
        if 'trade' in trade_question:
            player_cards = trade_card(player_cards)
            player_cards ['trade ?'] = 'yes'
            trade_bool = False
            return player_cards
        elif 'stick' in trade_question:
            player_cards ['trade ?'] = 'no'
            trade_bool = False
            return player_cards
        else:
            print('Please include trade or stick in your answer.')

def trade_card(hand):
    card_1_name = (hand['card 1']['name'])
    card_2_name = (hand['card 2']['name'])
    option_bool = True
    while option_bool:
        card_to_replace = str(input('\nWhat card would you like to trade out?\
            \n1. ' + (card_1_name) +\
            '\n2. ' + (card_2_name) + '\n'))
        deck = card_deck.create_deck()
        new_card = (random.choice(deck))
        card_to_replace = card_to_replace.capitalize()
        option_1 = ('1' in card_to_replace) or (card_1_name in card_to_replace)
        option_2 = ('2' in card_to_replace) or (card_2_name in card_to_replace)
        if option_1:
            del hand['card 1']
            hand ['card 1'] = new_card
            del hand['attacking score']
            del hand['defending score']
            del hand['combination']
            card_1 = hand ['card 1']
            card_2 = hand ['card 2']
            # print (card_1, card_2)
            hand = card_score(card_1, card_2)
            option_bool = False
            return (hand) 
        elif option_2:
            del hand['card 2']
            hand ['card 2'] = new_card
            del hand['attacking score']
            del hand['defending score']
            del hand['combination']
            card_1 = hand ['card 1']
            card_2 = hand ['card 2']
            # print (card_1, card_2)
            hand = card_score(card_1, card_2)
            option_bool = False
            return (hand)
        else:
            print('Please choose between card 1 and card 2.')

def combinations(card_1, card_2):
    if card_1['group'] == 'Attack' and card_2['group'] == 'Attack':
        combination = 'two attack'
        return combination
    if card_1['group'] == 'Defence' and card_2['group'] == 'Defence':
        combination = 'two defence'
        return combination
    if card_1['group'] == 'Attack' and card_2['group'] == 'Defence':
        combination = 'one each'
        return combination
    if card_1['group'] == 'Defence' and card_2['group'] == 'Attack':
        combination = 'one each'
        return combination

def card_score(card_1,card_2):
    # print (card_1)
    # print (card_2)
    player_cards = [card_1,card_2]
    # print(player_cards)
    card_1_index = card_1['strength']
    card_2_index = card_2['strength']
    # score = card_1_index + card_2_index
    combination = combinations(card_1, card_2)
    hand_value = {'card 1':card_1, 'card 2': card_2, 'combination':combination}
    if combination == 'two attack':
        hand_value['attacking score'] = card_1_index + card_2_index
        hand_value['defending score'] = 0
    elif combination == 'two defence':
        hand_value['attacking score'] = 0
        hand_value['defending score'] = card_1_index + card_2_index
    elif combination == 'one each':
        for card in player_cards:
            if card['group'] == 'Attack':
                hand_value['attacking score'] = card['strength']
            elif card['group'] == 'Defence':
                hand_value['defending score'] = card['strength']
            else:
                print ('check code 1. this is impossible')
    else:
        print('check code 2. this is impossible')
    # print (hand_value)
    return hand_value

    # print (score)
