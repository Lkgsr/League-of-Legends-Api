from league_of_legends_api.Tools.leaugue_request import LeagueRequest
from multiprocessing.dummy import Pool
import random


class Base:

    def __init__(self, api_keys, region="euw1", **kwargs):
        self.request = LeagueRequest(region)
        self.keys = api_keys

    def _get_random_key(self):
        return random.choice(self.keys)

    def _get_key_by_id(self, _id):
        for key in self.keys:
            if key.id == _id:
                return key
        print(f'Key with id {_id} no valid, using random key')
        return self._get_random_key()


class ChampionMasteryV4(Base):
    """Champion mastery V4"""

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def get_champion_masteries_by_summoner_id(self, summoner_id, api_key_id):
        """All champion Masterypoints by summoner ID"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}',
                                         key), key

    def get_champion_mastery_by_summoner_id_and_champion_id(self, summoner_id, champion_id, api_key_id):
        """champion mastery points by summoner id and champion ID"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/'
                                         f'by-champion/{champion_id}', key), key

    def get_summoner_mastery_score_by_summoner_id(self, summoner_id, api_key_id):
        """champion Mastery Score by Summoner ID"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/champion-mastery/v4/scores/by-summoner/{summoner_id}', key), key


class SummonerV4(Base):
    """Summoner"""

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def get_summoner_by_account_id(self, account_id, api_key_id):
        """Get a summoner by account ID"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/summoner/v4/summoners/by-account/{account_id}', key), key

    def get_summoner_by_name(self, summoner_name):
        """Get summoner by summoner name"""
        key = self._get_random_key()
        return self.request.send_request(f'/lol/summoner/v4/summoners/by-name/{summoner_name}', key), key

    def get_summoner_by_id(self, summoner_id, api_key_id):
        """Get summoner by summoner ID"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/summoner/v4/summoners/{summoner_id}', key), key

    def get_summoner_by_puuid(self, puuid, api_key_id):
        """Get summoner by summoner PUUID"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/summoner/v4/summoners/by-puuid/{puuid}', key), key


class ChampionV3(Base):
    """ChampionV3"""

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def get_champion_rotation(self):
        """Gives you the free champs to play"""
        key = self._get_random_key()
        return self.request.send_request('/lol/platform/v3/champion-rotations', key)


class LolStatusV3(Base):
    """LoL Status V3"""

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def get_shared_data(self):
        """Gives you the current Status of all League Services
        Requests to this API are not counted against the application Rate Limits."""
        key = self._get_random_key()
        return self.request.send_request('/lol/status/v3/shard-data', key)


class LeagueV4(Base):

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def get_grandmaster_leagues_by_queue_id(self, queue):
        """Returns List of Grandmaster Players by queue.
        :param queue: 'RANKED_SOLO_5x5', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT'
        :return: LeagueListDTO """
        key = self._get_random_key()
        return self.request.send_request(f'/lol/league/v4/grandmasterleagues/by-queue/{queue}', key), key

    def get_master_leagues_by_queue_id(self, queue):
        """Returns List of Master Players by queue.
        :param queue: 'RANKED_SOLO_5x5', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT'
        :return: LeagueListDTO """
        key = self._get_random_key()
        return self.request.send_request(f'/lol/league/v4/masterleagues/by-queue/{queue}', key), key

    def get_challenger_leagues_by_queue_id(self, queue):
        """Returns List of Challenger Players by queue.
        :param queue: 'RANKED_SOLO_5x5', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT'
        :return: LeagueListDTO """
        key = self._get_random_key()
        return self.request.send_request(f'/lol/league/v4/challengerleagues/by-queue/{queue}', key), key

    def get_league_entries_by_summoner_id(self, summoner_id, api_key_id):
        """Returns a list of all Leagues for the Summoner ID
        :return: Set[LeagueEntryDTO]"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/league/v4/entries/by-summoner/{summoner_id}', key), key

    def get_league_entries_by_queue_tier_division(self, queue, tier, division, page=1):
        """Returns a list of all Summoners in the given league
        :param queue: 'RANKED_SOLO_5x5', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT'
        :param tier: 'IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND'
        :param division: 'IV', 'III', 'II', 'I'
        :param page: 1 or higher, Starts with given page
        :return: Set[LeagueEntryDTO] """
        key = self._get_random_key()
        return self.request.send_request(f'/lol/league/v4/entries/{queue}/{tier}/{division}?page={page}', key), key

    def get_leagues_by_league_id(self, league_id):
        """
        Warning: Consistently looking up league ids that don't exist will result in a blacklist.
        :param league_id:
        :return: LeagueListDTO
        """
        key = self._get_random_key()
        return self.request.send_request(f'/lol/league/v4/leagues/{league_id}', key), key


class MatchV4(Base):

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def run_pool_request_match(self, list_of_match_ids):
        """Run Max 100 ids at the same time"""
        with Pool(100) as p:
            pm = p.imap_unordered(self.get_matches_by_match_id, list_of_match_ids)
            return [i for i in pm if i]

    def run_pool_request_timeline(self, list_of_match_ids):
        """Run Max 100 ids at the same time"""
        with Pool(100) as p:
            pm = p.imap_unordered(self.get_match_timeline_by_match_id, list_of_match_ids)
            return [i for i in pm if i]

    def get_matches_by_match_id(self, match_id):
        """"""
        key = self._get_random_key()
        return self.request.send_request(f'/lol/match/v4/matches/{match_id}', key), key

    def get_match_timeline_by_match_id(self, match_id):
        """Not all matches have timeline data"""
        key = self._get_random_key()
        return self.request.send_request(f'/lol/match/v4/timelines/by-match/{match_id}', key), key

    def get_match_list_by_account_id(self, account_id, api_key_id, **kwargs):
        """
        :param account_id:
        :param api_key_id:
        :param kwargs: champion, queue, season, endTime, beginTime, endIndex, beginIndex
        :return: MatchlistDto
        """
        optional = ''
        if kwargs:
            optional = '?' + '&'.join(['%s=%s' % (key, value) for (key, value) in kwargs.items()])
            print(optional)
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/match/v4/matchlists/by-account/{account_id}{optional}', key), key

    def get_matches_by_tournament_code(self, tournament_code):
        """"""
        key = self._get_random_key()
        return self.request.send_request(f'/lol/match/v4/matches/by-tournament-code/{tournament_code}/ids', key), key

    def get_match_by_match_id_tournament_code(self, match_id, tournament_code):
        """"""
        key = self._get_random_key()
        return self.request.send_request(f'/lol/match/v4/matches/{match_id}/by-tournament-code/{tournament_code}',
                                         key), key


class SpectatorV4(Base):

    def __init__(self, api_keys, **kwargs):
        Base.__init__(self, api_keys, **kwargs)

    def get_active_game_by_summoner_id(self, summoner_id, api_key_id):
        """"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f'/lol/spectator/v4/active-games/by-summoner/{summoner_id}', key), key

    def get_featured_games(self):
        """"""
        key = self._get_random_key()
        return self.request.send_request('/lol/spectator/v4/featured-games', key), key


class ThirdPartyCodeV4(Base):

    def __init__(self, api_keys, **kwargs):
        Base.__init__(api_keys, **kwargs)

    def get_third_party_code_by_summoner_id(self, summoner_id, api_key_id):
        """"""
        key = self._get_key_by_id(api_key_id)
        return self.request.send_request(f' /lol/platform/v4/third-party-code/by-summoner/{summoner_id}', key), key


class LeagueStaticDataDragon:

    @staticmethod
    def get_all_champions_static(language='de_DE', version=None):
        """All Champions if version is None it takes the newest one"""
        if version is None:
            response = LeagueRequest.send_json_request('https://ddragon.leagueoflegends.com/realms/na.json')
            version = response['n']['champion']
        return LeagueRequest.send_json_request(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json')

    @staticmethod
    def get_all_items_static(language='de_DE', version=None):
        """All Items if version is None it takes the newest one"""
        if version is None:
            response = LeagueRequest.send_json_request('https://ddragon.leagueoflegends.com/realms/na.json').json()
            version = response['n']['item']
        return LeagueRequest.send_json_request(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/item.json')
