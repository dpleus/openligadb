import pandas as pd


class Result:
    """
    Class to process API responses to pandas DataFrames.
    """

    @classmethod
    def df_matches(cls, matches_raw):
        columns = ["time", "team_home", "team_away", "goals_home", "goals_away"]
        matches_dict = {column: [] for column in columns}

        for match in matches_raw:
            matches_dict["time"].append(match["MatchDateTime"])
            matches_dict["team_home"].append(match["Team1"]["TeamName"])
            matches_dict["team_away"].append(match["Team2"]["TeamName"])
            matches_dict["goals_home"].append(match["MatchResults"][0]["PointsTeam1"])
            matches_dict["goals_away"].append(match["MatchResults"][0]["PointsTeam2"])

        matches_df = pd.DataFrame.from_dict(matches_dict)

        return matches_df

    @classmethod
    def df_goals(cls, matches_raw):
        columns = ["match_time", "minute", "player_name", "team_player", "team_opponent", "score_player", "score_opponent"]
        goals_dict = {column: [] for column in columns}

        for match in matches_raw:
            old_goals_team1 = 0
            old_goals_team2 = 0
            for goal in match["Goals"]:
                if goal["ScoreTeam1"] > old_goals_team1 or goal["ScoreTeam2"] > old_goals_team2:
                    goals_dict["match_time"].append(match["MatchDateTime"])
                    goals_dict["minute"].append(goal["MatchMinute"])
                    goals_dict["player_name"].append(goal["GoalGetterName"])

                if goal["ScoreTeam1"] > old_goals_team1:
                    goals_dict["team_player"].append(match["Team1"]["TeamName"])
                    goals_dict["team_opponent"].append(match["Team2"]["TeamName"])
                    goals_dict["score_player"].append(goal["ScoreTeam1"])
                    goals_dict["score_opponent"].append(goal["ScoreTeam2"])
                    old_goals_team1 = goal["ScoreTeam1"]

                elif goal["ScoreTeam2"] > old_goals_team2:
                    goals_dict["team_player"].append(match["Team2"]["TeamName"])
                    goals_dict["team_opponent"].append(match["Team1"]["TeamName"])
                    goals_dict["score_player"].append(goal["ScoreTeam2"])
                    goals_dict["score_opponent"].append(goal["ScoreTeam1"])
                    old_goals_team2 = goal["ScoreTeam2"]

        goals_df = pd.DataFrame.from_dict(goals_dict)

        return goals_df
