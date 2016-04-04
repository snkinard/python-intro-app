import mentions


def test_extract():
    msg = "@sam or hello @sam's fiancee is your name @katie? Or is it @katherine or whatever? is your email snkinard@gmail.com? also here is this thing @ "
    mentions_list = mentions.extract(msg)
    assert 3 == len(mentions_list)
    assert "sam" in mentions_list
    assert "katie" in mentions_list
    assert "katherine" in mentions_list
