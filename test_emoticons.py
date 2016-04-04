import emoticons

def test_extract():
    msg = "(smiley) hey! (smiley2) hello(smiley_3)world (morethanfifteencharacters) (fifteencharactr) (lolol lolol) ((sam)) yeah) (yeah"
    emoticons_list = emoticons.extract(msg)
    assert 5 == len(emoticons_list)
    assert "smiley" in emoticons_list
    assert "smiley2" in emoticons_list
    assert "smiley_3" in emoticons_list
    assert "fifteencharactr" in emoticons_list
    assert "sam" in emoticons_list

def test_extract_goofy():
    msg = "yeah) (yeah (sam)"
    emoticons_list = emoticons.extract(msg)
    assert 1 == len(emoticons_list)
    assert "sam" in emoticons_list

