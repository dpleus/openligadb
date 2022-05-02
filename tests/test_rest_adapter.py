from openligadb.api import Connection


def test_get_table():
    adapter = Connection("www.openligadb.de/api/")
    response = adapter.get_table("bl3", 2016)

    assert len(response) > 0
    assert response["TeamName"][0] == "MSV Duisburg"


def test_matches_season():
    adapter = Connection("www.openligadb.de/api/")
    response = adapter.get_matches("bl3", 2016)

    assert len(response) > 0
    assert response["team_away"][0] == "SC Paderborn 07"


def test_goals_season():
    adapter = Connection("www.openligadb.de/api/")
    response = adapter.get_goals("bl3", 2016)

    assert len(response) > 0
    assert response["player_name"][0] == "Janjic"
