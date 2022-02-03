
def matchup(player_1_cards,player_2_cards):
    # print (player_1_cards)
    # print (player_2_cards)
     #player 1 two attacking or two defending total to 11
    p1_attack_11 = player_1_cards ['combination'] == 'two attack' and player_1_cards ['attacking score'] == 11 
    p1_def_11 = player_1_cards ['combination'] == 'two defence' and player_1_cards ['defending score'] == 11
    #player 2 two attacking or two defending total to 11
    p2_attack_11 = player_2_cards ['combination'] == 'two attack' and player_2_cards ['attacking score'] == 11 
    p2_def_11 = player_2_cards ['combination'] == 'two defence' and player_2_cards ['defending score'] == 11
    
    #two attack with 11 or two def with 11
    if p1_attack_11 or p1_def_11 or p2_attack_11 or p2_def_11:
        result = has_11(player_1_cards,player_2_cards)
        return result
    #two attack both
    elif player_1_cards['combination'] == 'two attack' and player_2_cards['combination'] == 'two attack':
        result = both_attack(player_1_cards,player_2_cards)
        return result
    #two defence both
    elif player_1_cards['combination'] == 'two defence' and player_2_cards['combination'] == 'two defence':
        result = both_defence(player_1_cards,player_2_cards)
        return result
    #two attack vs two defence
    elif player_1_cards['combination'] == 'two attack' and player_2_cards['combination'] == 'two defence' or \
        player_1_cards['combination'] == 'two defence' and player_2_cards['combination'] == 'two attack':
        result = two_attack_vs_two_defence(player_1_cards, player_2_cards)
        return result
    #one of each both
    elif player_1_cards['combination'] == 'one each' and player_2_cards['combination'] == 'one each':
        result = one_vs_one(player_1_cards,player_2_cards)
        return result
    #two attack and one
    elif player_1_cards['combination'] == 'two attack' and player_2_cards['combination'] == 'one each' or \
        player_1_cards['combination'] == 'one each' and player_2_cards['combination'] == 'two attack':
        result = two_attack_vs_one(player_1_cards,player_2_cards)
        return result
    #two defence and one
    elif player_1_cards['combination'] == 'two defence' and player_2_cards['combination'] == 'one each' or \
        player_1_cards['combination'] == 'one each' and player_2_cards['combination'] == 'two defence':
        result = two_defence_vs_one(player_1_cards,player_2_cards)
        return result
    
#determines who will win
def both_attack(player_1_cards,player_2_cards):
    if player_1_cards ['attacking score'] > player_2_cards ['attacking score']:
        print ('player 1 wins')
        return 'player 1 wins'
    elif player_1_cards ['attacking score'] < player_2_cards ['attacking score']:
        print ('player 2 wins')
        return 'player 2 wins'
    elif player_1_cards ['attacking score'] == player_2_cards ['attacking score']:
        print ('draw')
        return 'draw'
def both_defence(player_1_cards, player_2_cards):
    print ('draw')
    return 'draw'
def two_attack_vs_two_defence(player_1_cards,player_2_cards):
    player_1_score = player_1_cards ['attacking score'] + player_1_cards ['defending score']
    player_1_cards ['overall score'] = player_1_score
    player_2_score = player_2_cards ['attacking score'] + player_2_cards ['defending score']
    player_2_cards ['overall score'] = player_2_score
    if player_1_cards ['overall score'] > player_2_cards ['overall score']:
        print ('player 1 wins')
        return 'player 1 wins'
    elif player_1_cards ['overall score'] < player_2_cards ['overall score']:
        print ('player 2 wins')
        return 'player 2 wins'
    elif player_1_cards ['overall score'] == player_2_cards ['overall score']:
        print ('draw')
        return 'draw'
def one_vs_one(player_1_cards,player_2_cards):
    p1_damage_delivered = player_1_cards ['attacking score'] - player_2_cards ['defending score']
    p2_damage_delivered = player_2_cards ['attacking score'] - player_1_cards ['defending score']

    if p1_damage_delivered < 0:
        p1_damage_delivered = 0
    if p2_damage_delivered < 0:
        p2_damage_delivered = 0

    if p1_damage_delivered > p2_damage_delivered:
        print ('player 1 wins')
        return 'player 1 wins'
    elif p1_damage_delivered < p2_damage_delivered:
        print ('player 2 wins')
        return 'player 2 wins'
    elif p1_damage_delivered == p2_damage_delivered:
        print ('draw')
        return 'draw'
def two_attack_vs_one(player_1_cards,player_2_cards):
    if player_1_cards ['combination'] == 'two attack' and player_2_cards ['combination'] == 'one each':
        player_1_cards ['attacking score'] = player_1_cards ['attacking score'] - player_2_cards ['defending score']
        if player_1_cards ['attacking score'] < 0:
            player_1_cards ['attacking score'] = 0
    elif player_2_cards ['combination'] == 'two attack' and player_1_cards ['combination'] == 'one each':
        player_2_cards ['attacking score'] = player_2_cards ['attacking score'] - player_1_cards ['defending score']
        if player_2_cards ['attacking score'] < 0:
            player_2_cards ['attacking score'] = 0         
    else:
        print('check code 3')

    if player_1_cards ['attacking score'] > player_2_cards ['attacking score']:
        print ('player 1 wins')
        return 'player 1 wins'
    elif player_1_cards ['attacking score'] < player_2_cards ['attacking score']:
        print ('player 2 wins')
        return 'player 2 wins'
    elif player_1_cards ['attacking score'] == player_2_cards ['attacking score']:
        print ('draw')
        return 'draw'
def two_defence_vs_one(player_1_cards,player_2_cards):
    if player_1_cards ['combination'] == 'two defence' and player_2_cards ['combination'] == 'one each':
        player_2_cards ['attacking score'] = player_2_cards ['attacking score'] - player_1_cards ['defending score']

        if player_2_cards ['attacking score'] > 0:
            print('player 2 winss')
            return 'player 2 winss'
        elif player_2_cards ['attacking score'] == 0:
            print ('draw')
            return 'draw'
        elif player_2_cards ['attacking score'] < 0:
            print ('player 1 wins')
            return 'player 1 wins'
        else:
            print('check code 4')
    elif player_1_cards ['combination'] == 'one each' and player_2_cards ['combination'] == 'two defence':
        player_1_cards ['attacking score'] = player_1_cards ['attacking score'] - player_2_cards ['defending score']

        if player_1_cards ['attacking score'] > 0:
            print('player 1 wins')
            return 'player 1 wins'
        elif player_1_cards ['attacking score'] == 0:
            print ('draw')
            return 'draw'
        elif player_1_cards ['attacking score'] < 0:
            print ('player 2 wins')
            return 'player 2 wins'
        else:
            print('check code 5')
    else:
        print('check code 6')
def has_11(player_1_cards, player_2_cards):
    #player 1 two attacking or two defending total to 11 and not
    p1_attack_11 = player_1_cards ['combination'] == 'two attack' and player_1_cards ['attacking score'] == 11 
    p1_defence_11 = player_1_cards ['combination'] == 'two defence' and player_1_cards ['defending score'] == 11
    p1_not_attack_11 = (player_1_cards ['combination'] != 'two attack' and player_1_cards ['attacking score'] != 11) or\
        (player_1_cards ['combination'] != 'two attack' and player_1_cards ['attacking score'] == 11) or\
            (player_1_cards ['combination'] == 'two attack' and player_1_cards ['attacking score'] != 11) 
    p1_not_defence_11 = (player_1_cards['combination'] != 'two defence' and player_1_cards ['defending score'] != 11) or\
        (player_1_cards['combination'] != 'two defence' and player_1_cards ['defending score'] == 11) or\
            (player_1_cards['combination'] == 'two defence' and player_1_cards ['defending score'] != 11)
    #player 2 two attacking or two defending total to 11 and not
    p2_attack_11 = player_2_cards ['combination'] == 'two attack' and player_2_cards ['attacking score'] == 11 
    p2_defence_11 = player_2_cards ['combination'] == 'two defence' and player_2_cards ['defending score'] == 11
    p2_not_attack_11 = (player_2_cards ['combination'] != 'two attack' and player_2_cards ['attacking score'] != 11) or\
        (player_2_cards['combination'] != 'two attack' and player_2_cards ['attacking score'] == 11) or\
            (player_2_cards['combination'] == 'two attack' and player_2_cards ['attacking score'] != 11) 
    p2_not_defence_11 = (['combination'] != 'two defence' and player_2_cards ['defending score'] != 11) or\
        (player_2_cards['combination'] != 'two defence' and player_2_cards ['defending score'] == 11) or\
            (player_2_cards['combination'] == 'two defence' and player_2_cards ['defending score'] != 11)
    
    #p1 attributes
    p1_card_1_score = player_1_cards['card 1']['strength']
    p1_card_2_score = player_1_cards['card 2']['strength']
    #p2 attibutes
    p2_card_1_score = player_2_cards['card 1']['strength']
    p2_card_2_score = player_2_cards['card 2']['strength']
    
    if (p1_attack_11 or p1_defence_11) and p2_not_attack_11 and p2_not_defence_11:
        print ('player 1 wins')
        return 'player 1 wins'
    elif (p2_attack_11 or p2_defence_11) and p1_not_attack_11 and p1_not_defence_11:
        print ('player 2 wins')
        return 'player 2 wins'
    elif p1_attack_11 and p2_defence_11:
        print ('player 2 wins')
        return 'player 2 wins'
    elif p2_attack_11 and p1_defence_11:
        print ('player 1 wins')
        return 'player 1 wins'
    elif (p1_attack_11 and p2_attack_11) or (p1_defence_11 and p2_defence_11):
        if (p1_card_1_score > p1_card_2_score and p2_card_1_score > p2_card_2_score) or\
            (p1_card_1_score > p1_card_2_score and p2_card_1_score == p2_card_2_score) or\
                (p1_card_1_score == p1_card_2_score and p2_card_1_score > p2_card_2_score) or\
                    (p1_card_1_score == p1_card_2_score and p2_card_1_score == p2_card_2_score):
            if p1_card_1_score > p2_card_1_score:
                print ('player 1 wins')
                return 'player 1 wins'
            elif p1_card_1_score < p2_card_1_score:
                print ('player 2 wins')
                return 'player 2 wins'
            elif p1_card_1_score == p2_card_1_score:
                print ('draw')
                return 'draw'
            else:
                print('check code 7')
        elif (p1_card_1_score < p1_card_2_score and p2_card_1_score < p2_card_2_score) or\
            (p1_card_1_score < p1_card_2_score and p2_card_1_score == p2_card_2_score) or\
                (p1_card_1_score == p1_card_2_score and p2_card_1_score < p2_card_2_score):
            if p1_card_2_score > p2_card_2_score:
                print ('player 1 wins')
                return 'player 1 wins'
            elif p1_card_2_score < p2_card_2_score:
                print ('player 2 wins')
                return 'player 2 wins'
            elif p1_card_2_score == p2_card_2_score:
                print ('draw')
                return 'draw'
            else:
                print('check code 8')
        elif p1_card_1_score > p1_card_2_score and p2_card_1_score < p2_card_2_score:
            if p1_card_1_score > p2_card_2_score:
                print ('player 1 wins')
                return 'player 1 wins'
            elif p1_card_1_score < p2_card_2_score:
                print ('player 2 wins')
                return 'player 2 wins'
            elif p1_card_1_score == p2_card_2_score:
                print ('draw')
                return 'draw'
            else:
                print(' 9')
        elif p1_card_1_score < p1_card_2_score and p2_card_1_score > p2_card_2_score:
            if p1_card_2_score > p2_card_1_score:
                print ('player 1 wins')
                return 'player 1 wins'
            elif p1_card_2_score < p2_card_1_score:
                print ('player 2 wins')
                return 'player 2 wins'
            elif p1_card_2_score == p2_card_1_score:
                print ('draw')
                return 'draw'
            else:
                print('check code 10')        
        else:
            print('check code 11')
    else:
        print('check code 12')