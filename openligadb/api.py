import logging

import pandas as pd
import requests
import requests.packages

from openligadb.result import Result


class Connection:
    """
    Class to create run queries against API.
    """
    def __init__(self, hostname: str = "www.openligadb.de/api/", ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructs rest adapter.

        :param hostname: URL of website
        :param ssl_verify: Set to True per default, set to False if there are SSL Issues
        :param logger: (optional)
        """
        self.url = "https://{}".format(hostname)
        self._logger = logger or logging.getLogger(__name__)

        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _get(self, method: str, *params) -> dict:
        """
        Private method to retrieve data from API.

        :param method: Specifies endpoint/method, e.g. gettable, getmatches
        :param params: Parameters that further specify endpoint, e.g. league, season

        """
        parameters = "/".join(([str(p) for p in filter(None, params)]))
        full_url = "{}/{}/{}".format(self.url, method, parameters)  # make this flexible
        headers = {}

        try:
            response = requests.get(url=full_url, verify=self._ssl_verify, headers=headers)
        except requests.exceptions.RequestException as e:
            self._logger.debug(msg=(str(e)))

        try:
            data_out = response.json()
        except:
            self._logger.error(msg="Bad JSON in response")
            raise ValueError("Bad JSON response.")

        log_response = f"url={full_url}, params={parameters}, status_code={response.status_code}, message={response.reason}"
        self._logger.debug(msg=log_response)

        if 200 <= response.status_code <= 299 and len(data_out) > 0:
            return data_out
        else:
            self._logger.debug(msg="Response is empty.")
            raise Exception("Response is empty. Please check the parameters.")

    def get_table(self, league: str, season: str) -> pd.DataFrame:
        """ Gets table (for the latest round) as a pandas DataFrame.

        :param league: League shortcut as provided by OpenLigaDB.
        :param season: Season specified by start year, e.g. 2020/2021 -> 2020
        :return: DataFrame that contains table.

        """
        table_raw = self._get("getbltable", league, season)
        table_df = pd.DataFrame.from_dict(table_raw)
        return table_df

    def get_matches(self, league: str, season: str, round: str = None) -> pd.DataFrame:
        """ Gets all matches for a specific season.

        :param league: League shortcut as provided by OpenLigaDB.
        :param season: Season specified by start year, e.g. 2020/2021 -> 2020
        :return: DataFrame that contains time, home and away teams, home and away goals.
        """

        matches_raw = self._get("getmatchdata", league, season, round)
        return Result.df_matches(matches_raw)

    def get_goals(self, league: str, season: str, round: str = None) -> pd.DataFrame:
        """ Gets all matches for a specific season.

        :param league: League shortcut as provided by OpenLigaDB.
        :param season: Season specified by start year, e.g. 2020/2021 -> 2020
        :return: DataFrame that contains time, home and away teams, home and away goals.
        """

        matches_raw = self._get("getmatchdata", league, season, round)
        return Result.df_goals(matches_raw)
