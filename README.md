# Simple League of Legends Wrapper in Python
It creates a small sqlite Database where it can saves multiple Api-Keys.
Every Request returns the response from the server and the Api-Key object.
This makes it possible to save the Data like the encryptedAccountId with the
right Api-Key-ID and for further request where you use the encryptedAccountId you provide the corresponding
Api-Key-ID.
## installation
``pip install ApiLeagueOfLegends``

## usage
save you Api-Keys to the local database
```python
from league_of_legends_api.Database.database import Database
keys = ['RGAPI-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', 'RGAPI-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', 'RGAPI-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX']
db = Database()
db.save_keys_to_database(keys)
```
use the saved keys
````python
from league_of_legends_api.Database.database import Database
from league_of_legends_api.Api.leaugue_api import SummonerV4
db = Database()
keys = db.load_keys_in()
summoner = SummonerV4(keys, region='euw1')
response, key = summoner.get_summoner_by_name("SaItySurprise")
print(response, key)
````
``{'id': str, 'accountId': str, 'puuid': str, 'name': 'SaItySurprise', 'profileIconId': 3552, 'revisionDate': 1556578547000, 'summonerLevel': 154, 'api_key_id': 4} ApiKey: key:RGAPI-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX, id: 4``