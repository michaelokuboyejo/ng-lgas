import json
from logging import getLogger

log = getLogger('NG_LGA')


class NG_LGA:
    def __init__(self):
        try:
            self._ng_lgas_list = json.load(open('./ng_lgas/ng-lgas.json'))
        except FileNotFoundError:
            log.error('could not open data file')
            self._ng_lgas_list = []

    def get_state_codes(self) -> list:
        return sorted(set([lga['StateCode'] for lga in self._ng_lgas_list]))

    def get_by_state_code(self, state_code: str) -> list:
        return [lga for lga in self._ng_lgas_list if lga['StateCode'] == state_code.upper()]

    def get_all(self) -> list:
        return self._ng_lgas_list

    def get_by_state(self, state: str) -> list:
        return [lga for lga in self._ng_lgas_list if lga['State'] == state]

    def get_states(self) -> list:
        return sorted(set([lga['StateCode'] for lga in self._ng_lgas_list]))
