import unittest
import game_functions
import matchup_functions
import card_deck

class TestCardGame(unittest.TestCase):
    def test_card_score(self):
        card_1 = {'name': 'Giant', 'group': 'Attack', 'strength': 8}
        card_2 = {'name': 'Fairy', 'group': 'Defence', 'strength': 5}
        card_3 = {'name': 'Hydra', 'group': 'Attack', 'strength': 6}
        card_4 = {'name': 'Fairy', 'group': 'Defence', 'strength': 5}
        player_cards_1 = game_functions.card_score(card_1,card_2)
        player_cards_2 = game_functions.card_score(card_1, card_3)
        player_cards_3 = game_functions.card_score(card_2, card_4)

        self.assertEqual(len(player_cards_1),5)
        self.assertEqual(player_cards_1['card 1']['name'], 'Giant')
        self.assertEqual(player_cards_1['card 1']['group'], 'Attack')
        self.assertEqual(player_cards_1['card 1']['strength'], 8)
        self.assertEqual(player_cards_1['card 2']['name'], 'Fairy')
        self.assertEqual(player_cards_1['card 2']['group'], 'Defence')
        self.assertEqual(player_cards_1['card 2']['strength'], 5)
        self.assertEqual(player_cards_1['combination'], 'one each')
        self.assertEqual(player_cards_1['combination'], 'one each')
        self.assertEqual(player_cards_1['attacking score'], 8)
        self.assertEqual(player_cards_1['defending score'], 5)
        self.assertEqual(player_cards_2['attacking score'], 14)
        self.assertEqual(player_cards_2['defending score'], 0)
        self.assertEqual(player_cards_3['attacking score'], 0)
        self.assertEqual(player_cards_3['defending score'], 10)
    
    def test_combinations(self):
        card_1 = {'name': 'Giant', 'group': 'Attack', 'strength': 8}
        card_2 = {'name': 'Fairy', 'group': 'Defence', 'strength': 5}
        card_3 = {'name': 'Hydra', 'group': 'Attack', 'strength': 6}
        card_4 = {'name': 'Fairy', 'group': 'Defence', 'strength': 5}
        test_cards_1 = game_functions.combinations(card_1, card_2)
        test_cards_2 = game_functions.combinations(card_2,card_1)
        test_cards_3 = game_functions.combinations(card_1, card_3)
        test_cards_4 = game_functions.combinations(card_2, card_4)
        self.assertEqual(test_cards_1, 'one each')
        self.assertEqual(test_cards_2, 'one each')
        self.assertEqual(test_cards_3, 'two attack')
        self.assertEqual(test_cards_4, 'two defence')
 
    def test_create_deck(self):
        deck = card_deck.create_deck()
        cards = [{'name': 'Cat', 'group': 'Attack', 'strength': 1}, {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, {'name': 'Liger', 'group': 'Attack', 'strength': 3}, {'name': 'Sea serpent', 'group': 'Attack', 'strength': 4}, {'name': 'Gargoyle', 'group': 'Attack', 'strength': 5}, {'name': 'Hydra', 'group': 'Attack', 'strength': 6}, {'name': 'Vampire', 'group': 'Attack', 'strength': 7}, {'name': 'Giant', 'group': 'Attack', 'strength': 8}, {'name': 'Werewolf', 'group': 'Attack', 'strength': 9}, {'name': 'Dragon', 'group': 'Attack', 'strength': 10}, {'name': 'Dog', 'group': 'Defence', 'strength': 1}, {'name': 'Owl', 'group': 'Defence', 'strength': 2}, {'name': 'Gnome', 'group': 'Defence', 'strength': 3}, {'name': 'Mermaid', 'group': 'Defence', 'strength': 4}, {'name': 'Fairy', 'group': 'Defence', 'strength': 5}, {'name': 'Centaur', 'group': 'Defence', 'strength': 6}, {'name': 'Hippogriff', 'group': 'Defence', 'strength': 7}, {'name': 'Sphinx', 'group': 'Defence', 'strength': 8}, {'name': 'Gryphon', 'group': 'Defence', 'strength': 9}, {'name': 'Unicorn', 'group': 'Defence', 'strength': 10}]
        self.assertEqual(deck,cards)

    def test_both_attack(self):
        attack_cards_1 = {'card 1': {'name': 'Gargoyle', 'group': 'Attack', 'strength': 5}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 7, 'defending score': 0, 'player': 'Player 1'}
        attack_cards_2 = {'card 1': {'name': 'Giant', 'group': 'Attack', 'strength': 8}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 10, 'defending score': 0, 'player': 'Player 2'}
        att_result = matchup_functions.both_attack(attack_cards_1,attack_cards_2)
        self.assertEqual(att_result,'player 2 wins')

    def test_both_defence(self):
        defence_cards_1  = {'card 1': {'name': 'Sphinx', 'group': 'Defence', 'strength': 8}, 'card 2': {'name': 'Unicorn', 'group': 'Defence', 'strength': 10}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 18, 'player': 'Player 1'}
        defence_cards_2 = {'card 1': {'name': 'Mermaid', 'group': 'Defence', 'strength': 4}, 'card 2': {'name': 'Owl', 'group': 'Defence', 'strength': 2}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 6, 'player': 'Player 1'}
        def_result = matchup_functions.both_defence(defence_cards_1,defence_cards_2)
        self.assertEqual(def_result,'draw')

    def test_two_attack_vs_two_defence(self):
        attack_cards_1 = {'card 1': {'name': 'Gargoyle', 'group': 'Attack', 'strength': 5}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 7, 'defending score': 0, 'player': 'Player 1'}
        attack_cards_2 = {'card 1': {'name': 'Giant', 'group': 'Attack', 'strength': 8}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 10, 'defending score': 0, 'player': 'Player 2'}
        defence_cards_1  = {'card 1': {'name': 'Sphinx', 'group': 'Defence', 'strength': 8}, 'card 2': {'name': 'Unicorn', 'group': 'Defence', 'strength': 10}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 18, 'player': 'Player 1'}
        defence_cards_2 = {'card 1': {'name': 'Mermaid', 'group': 'Defence', 'strength': 4}, 'card 2': {'name': 'Owl', 'group': 'Defence', 'strength': 2}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 6, 'player': 'Player 1'}
        att_def_result_1 = matchup_functions.two_attack_vs_two_defence(attack_cards_1, defence_cards_2)
        att_def_result_2 = matchup_functions.two_attack_vs_two_defence(attack_cards_2, defence_cards_1)
        self.assertEqual(att_def_result_1, 'player 1 wins')
        self.assertEqual(att_def_result_2, 'player 2 wins')

    def test_one_vs_one(self):
        one_each_1 = {'card 1': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'card 2': {'name': 'Centaur', 'group': 'Defence', 'strength': 6}, 'combination': 'one each', 'attacking score': 2, 'defending score': 6, 'player': 'Player 1'}
        one_each_2  = {'card 1': {'name': 'Giant', 'group': 'Attack', 'strength': 8}, 'card 2': {'name': 'Dog', 'group': 'Defence', 'strength': 1}, 'combination': 'one each', 'attacking score': 8, 'defending score': 1, 'player': 'Player 2'}
        test_one_each_1 = matchup_functions.one_vs_one(one_each_1, one_each_2)
        self.assertEqual(test_one_each_1, 'player 2 wins')

    def test_two_attack_vs_one(self):
        attack_cards_1 = {'card 1': {'name': 'Gargoyle', 'group': 'Attack', 'strength': 5}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 7, 'defending score': 0, 'player': 'Player 1'}
        attack_cards_2 = {'card 1': {'name': 'Giant', 'group': 'Attack', 'strength': 8}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 10, 'defending score': 0, 'player': 'Player 2'}
        one_each_1 = {'card 1': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'card 2': {'name': 'Centaur', 'group': 'Defence', 'strength': 6}, 'combination': 'one each', 'attacking score': 2, 'defending score': 6, 'player': 'Player 1'}
        test_two_attack_vs_one_1 = matchup_functions.two_attack_vs_one(attack_cards_1, one_each_1)
        self.assertEqual(test_two_attack_vs_one_1, 'player 2 wins')
        test_two_attack_vs_one_3 = matchup_functions.two_attack_vs_one(one_each_1, attack_cards_2)
        self.assertEqual(test_two_attack_vs_one_3, 'player 2 wins')

    def test_two_defence_vs_one(self):
        defence_cards_1  = {'card 1': {'name': 'Sphinx', 'group': 'Defence', 'strength': 8}, 'card 2': {'name': 'Unicorn', 'group': 'Defence', 'strength': 10}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 18, 'player': 'Player 1'}
        defence_cards_2 = {'card 1': {'name': 'Mermaid', 'group': 'Defence', 'strength': 4}, 'card 2': {'name': 'Owl', 'group': 'Defence', 'strength': 2}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 6, 'player': 'Player 1'}
        one_each_1 = {'card 1': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'card 2': {'name': 'Centaur', 'group': 'Defence', 'strength': 6}, 'combination': 'one each', 'attacking score': 2, 'defending score': 6, 'player': 'Player 1'}
        one_each_2  = {'card 1': {'name': 'Giant', 'group': 'Attack', 'strength': 8}, 'card 2': {'name': 'Dog', 'group': 'Defence', 'strength': 1}, 'combination': 'one each', 'attacking score': 8, 'defending score': 1, 'player': 'Player 2'}
        test_two_defence_vs_one_1 = matchup_functions.two_defence_vs_one(defence_cards_1, one_each_1)
        self.assertEqual(test_two_defence_vs_one_1, 'player 1 wins')
        test_two_defence_vs_one_3 = matchup_functions.two_defence_vs_one(one_each_2, defence_cards_2)
        self.assertEqual(test_two_defence_vs_one_3, 'player 1 wins')

    def test_has_11(self):
        defence_11_1 = {'card 1': {'name': 'Mermaid', 'group': 'Defence', 'strength': 4}, 'card 2': {'name': 'Hippogriff', 'group': 'Defence', 'strength': 7}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 11}
        defence_11_2 = {'card 1': {'name': 'Unicorn', 'group': 'Defence', 'strength': 10}, 'card 2': {'name': 'Dog', 'group': 'Defence', 'strength': 1}, 'combination': 'two defence', 'attacking score': 0, 'defending score': 11}
        attack_11_1 = {'card 1': {'name': 'Gargoyle', 'group': 'Attack', 'strength': 5}, 'card 2': {'name': 'Hydra', 'group': 'Attack', 'strength': 6}, 'combination': 'two attack', 'attacking score': 11, 'defending score': 0, 'player': 'Player 1'}
        attack_11_2 = {'card 1': {'name': 'Giant', 'group': 'Attack', 'strength': 8}, 'card 2': {'name': 'Liger', 'group': 'Attack', 'strength': 3}, 'combination': 'two attack', 'attacking score': 11, 'defending score': 0, 'player': 'Player 2'}
        attack_cards_1 = {'card 1': {'name': 'Gargoyle', 'group': 'Attack', 'strength': 5}, 'card 2': {'name': 'Eagle', 'group': 'Attack', 'strength': 2}, 'combination': 'two attack', 'attacking score': 7, 'defending score': 0, 'player': 'Player 1'}
        test_11_2 = matchup_functions.has_11(attack_11_1, attack_cards_1)
        self.assertEqual(test_11_2,'player 1 wins')
        test_11_2 = matchup_functions.has_11(defence_11_1, attack_cards_1)
        self.assertEqual(test_11_2,'player 1 wins')
        test_11_1 = matchup_functions.has_11(defence_11_1, defence_11_2)
        self.assertEqual(test_11_1,'player 2 wins')
        test_11_2 = matchup_functions.has_11(attack_11_1, defence_11_2)
        self.assertEqual(test_11_2,'player 2 wins')
        test_11_2 = matchup_functions.has_11(attack_11_1, attack_11_2)
        self.assertEqual(test_11_2,'player 2 wins')




if __name__ == '__main__':
    unittest.main()