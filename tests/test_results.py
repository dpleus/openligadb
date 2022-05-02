from openligadb.api import Connection
from openligadb.result import Result


def test_df_matches():
    adapter = Connection("www.openligadb.de/api/")
    response = adapter._get("getmatchdata", "bl1", 2016)
    df = Result.df_matches(response)

    assert len(response) == len(df)


def test_df_goals():
    adapter = Connection("www.openligadb.de/api/")
    response = adapter._get("getmatchdata", "bl1", 2016)
    df = Result.df_goals(response)

    assert len(df) > 0