import bid

def test_can_start_bidding():
    assert bid.can_start_bidding(11) == False
    assert bid.can_start_bidding(12) == True
