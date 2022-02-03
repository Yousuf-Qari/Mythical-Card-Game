import card_deck
import matchup_functions
import game_functions
import random

def main():
    print('\nWelcome to Magical Animals\n')
    keep_playing = True
    player_1_wins = 0
    player_2_wins = 0
    draws = 0
    file_name = str(input('Please name a file to track your matchup record: '))
    try:    
        while keep_playing:     
            print ('\nThe current score is:')
            game_functions.write_and_read_csv(player_1_wins, player_2_wins, draws, file_name)
            deck = card_deck.create_deck()
            card_1 = (random.choice(deck))
            card_2 = (random.choice(deck))
            card_3 = (random.choice(deck))
            card_4 = (random.choice(deck))
            
            player_1_cards = game_functions.card_score(card_1, card_2)
            player_2_cards = game_functions.card_score(card_3,card_4)
            #player numbers
            player_1_cards['player'] = 'Player 1'
            player_2_cards['player'] = 'Player 2'
            #p1 attributes
            p1_card_1_name = player_1_cards['card 1']['name']
            p1_card_1_score = player_1_cards['card 1']['strength']
            p1_card_2_name = player_1_cards['card 2']['name']
            p1_card_2_score = player_1_cards['card 2']['strength']
            #p2 attibutes
            p2_card_1_name = player_2_cards['card 1']['name']
            p2_card_1_score = player_2_cards['card 1']['strength']
            p2_card_2_name = player_2_cards['card 2']['name']
            p2_card_2_score = player_2_cards['card 2']['strength']

            print ('\nPlayer 1 has been dealt a ' + p1_card_1_name + '(' + str(p1_card_1_score) + ')'\
                + ' and a ' + p1_card_2_name+ '(' + str(p1_card_2_score) + ')')
            print ('Attacking score: ' + str(player_1_cards['attacking score']))
            print ('Defending score: ' + str(player_1_cards['defending score']))

            print ('\nPlayer 2 has been dealt a ' + p2_card_1_name + '(' + str(p2_card_1_score) + ')'\
                + ' and a ' + p2_card_2_name+ '(' + str(p2_card_2_score) + ')')
            print ('Attacking score: ' + str(player_2_cards['attacking score']))
            print ('Defending score: ' + str(player_2_cards['defending score']))
            
            # print (player_1_cards)
            # print (player_2_cards)
            #trade cards
            player_1_cards = game_functions.trade_request(player_1_cards)
            player_2_cards = game_functions.trade_request(player_2_cards)

            player_1_traded = player_1_cards['trade ?'] == 'yes'
            player_2_traded = player_2_cards['trade ?'] == 'yes'
            if player_1_traded or player_2_traded:
                #p1 attributes
                p1_card_1_name = player_1_cards['card 1']['name']
                p1_card_1_score = player_1_cards['card 1']['strength']
                p1_card_2_name = player_1_cards['card 2']['name']
                p1_card_2_score = player_1_cards['card 2']['strength']
                #p2 attibutes
                p2_card_1_name = player_2_cards['card 1']['name']
                p2_card_1_score = player_2_cards['card 1']['strength']
                p2_card_2_name = player_2_cards['card 2']['name']
                p2_card_2_score = player_2_cards['card 2']['strength']

                print ('\nPlayer 1 has been dealt a ' + p1_card_1_name + '(' + str(p1_card_1_score) + ')'\
                    + ' and a ' + p1_card_2_name+ '(' + str(p1_card_2_score) + ')')
                print ('Attacking score: ' + str(player_1_cards['attacking score']))
                print ('Defending score: ' + str(player_1_cards['defending score']))

                print ('\nPlayer 2 has been dealt a ' + p2_card_1_name + '(' + str(p2_card_1_score) + ')'\
                    + ' and a ' + p2_card_2_name+ '(' + str(p2_card_2_score) + ')')
                print ('Attacking score: ' + str(player_2_cards['attacking score']))
                print ('Defending score: ' + str(player_2_cards['defending score']))
                print('')
            else:
                print('')

            # print(player_1_cards)
            # print(player_2_cards)

            result = matchup_functions.matchup(player_1_cards,player_2_cards)

            if result == 'player 1 wins':
                player_1_wins += 1
            elif result == 'player 2 wins':
                player_2_wins += 1
            elif result == 'draw':
                draws += 1

            #do they want to keep playing?
            continue_playing_question = str(input('\nDo you want to keep playing?(yes/no)\n'))
            continue_playing_question = continue_playing_question.lower()
            if 'yes' in continue_playing_question:
                keep_playing = True
            if 'no' in continue_playing_question:
                print ('The final scores are:')
                game_functions.write_and_read_csv(player_1_wins, player_2_wins, draws, file_name)
                print ('Thank you for playing.')
                keep_playing = False    
    except PermissionError:
        print("Cannot open file for writing")
        
        
        
            
if __name__ == '__main__':
    main()