#module to create and shuffle a deck of cards for magical animals
    
import os
# print (os.getcwd())

def create_deck():
    deck = []
    attacking_cards = ['Cat', 'Eagle', 'Liger', 'Sea serpent',\
        'Gargoyle', 'Hydra','Vampire', 'Giant', 'Werewolf', \
            'Dragon']
    defending_cards = ['Dog', 'Owl', 'Gnome', 'Mermaid', \
        'Fairy', 'Centaur', 'Hippogriff', 'Sphinx', 'Gryphon', \
            'Unicorn']
    for attacker in attacking_cards:
        card = {}
        card['name'] = attacker
        card['group'] = 'Attack'
        index = attacking_cards.index(attacker)
        card['strength'] = index + 1
        deck.append(card)
    for defender in defending_cards:
        card = {}
        card['name'] = defender
        card['group'] = 'Defence'
        index = defending_cards.index(defender)
        card['strength'] = index + 1
        deck.append(card)
    # print (deck)
    return deck
 