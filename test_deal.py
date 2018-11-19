import deal

def test_get_hand():
    d = deal.Deal('S')
    cards_in_hand =  d.get_hand( 'S')
    assert len(cards_in_hand) == 13