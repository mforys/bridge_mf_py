import card


def test_card_ace_spade():
    c = card.Card(0)
    assert c.id == 0
    assert c.rep == ['S','A']


def test_card_two_club():
    c = card.Card(51)
    assert c.rep == ['C', '2']


def test_card_jack_spade():
    c = card.Card(3)
    assert c.rep == ['S', 'J']


def test_transfer_int_2_rep():
    c = card.Card(13)
    assert c.transfer_int_2_rep() == ['H','A']


def test_transfer_int_2_string():
    c = card.Card(13)
    assert c.transfer_int_2_string() == 'H A'


def test_transfer_int_2_string_king_heart():
    c = card.Card(14)
    assert c.transfer_int_2_string() == 'H K'

