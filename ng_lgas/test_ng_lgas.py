import unittest

from ng_lgas import NG_LGA

ng_lgas = NG_LGA()


class NGLGASTestCase(unittest.TestCase):
    def test_get_state_codes_is_not_empty(self):
        self.assertFalse(len(ng_lgas.get_state_codes()) == 0)

    def test_get_states_is_not_empty(self):
        self.assertFalse(len(ng_lgas.get_states()) == 0)

    def test_get_all_is_not_empty(self):
        self.assertFalse(len(ng_lgas.get_states()) == 0)

    def test_get_by_state_code(self):
        lgas_by_state_code = ng_lgas.get_by_state_code('LA')
        self.assertGreater(len(lgas_by_state_code), 0)

        lgas_by_state_code = ng_lgas.get_by_state_code('EMPTY')
        self.assertEqual(len(lgas_by_state_code), 0)

    def test_get_by_state(self):
        lgas_by_state_code = ng_lgas.get_by_state('Lagos')
        self.assertGreater(len(lgas_by_state_code), 0)

        lgas_by_state_code = ng_lgas.get_by_state('Alabama')
        self.assertEqual(len(lgas_by_state_code), 0)




if __name__ == '__main__':
    unittest.main()
