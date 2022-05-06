from openligadb.api import Connection
api = Connection(hostname ="www.openligadb.de/api")
table = api.get_table("bl3", 2016)
matches = api.get_matches("bl3", 2016)
matches_3 = api.get_matches("bl3", 2020, 3)
goals = api.get_goals("bl3", 2016)
print("Hey")