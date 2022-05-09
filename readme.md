# Readme
## About The Project
This python package simplifies retrieving data from the [OpenLigaDB API](https://github.com/OpenLigaDB/OpenLigaDB-Samples).
Docs can be found [here](https://openligadb.readthedocs.io/en/latest/index.html).

## Getting Started
Clone this repository to your local machine.
```
git clone https://github.com/dpleus/openligadb.git
```

Afterwards go to the download folder an install the package.

```
pip install .
```

### How to use

In a first step you need to create a connection object.

```
from openligadb.api import Connection

connection = Connection()
```

In a second step you can access the data similar to the following examples:
* Table
```
connection.get_table("bl2", 2016)
```

* Matches
```
connection.get_matches("bl2", 2016)
```

* Goals
```
connection.get_goals("bl2", 2016)
```

The first parameter specifies the league. The league overview can be found [here](https://www.openligadb.de/Datenhaushalt/). The second parameter defines the season (starting year). A third parameter for the round is optional.

### Limitations
All data is maintained through OpenLigaDB. This package was tested on football data and there is no guarantee it works for other sports.

## License

Distributed under the MIT License. 
