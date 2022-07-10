import unittest

from double_elimination import Tournament as DoubleEliminationTournament

class GrandFinalsTest(unittest.TestCase):

    def test_grand_finals(self) -> None:
        tournament = DoubleEliminationTournament[str](
            competitors_list=['A','B','C','D'],
            options={ 'with_grand_finals': True }
        )

        # Competitor 'A' wins the whole upper bracket.
        
        # Round 1: A vs D, B vs C
        matches = tournament.get_active_matches()


        A_match = tournament.get_active_matches_for_competitor('A')[0]
        tournament.add_win(A_match,'A')

        B_match = tournament.get_active_matches_for_competitor('B')[0]
        tournament.add_win(B_match, 'B')

        # Round 2: (upper) A vs B, (lower) C vs D
        matches = tournament.get_active_matches()

        A_match = tournament.get_active_matches_for_competitor('A')[0]
        tournament.add_win(A_match, 'A')

        C_match = tournament.get_active_matches_for_competitor('C')[0]
        tournament.add_win(C_match, 'C')

        # Round 3 (lower-only) B vs C
        # There should only be one match (the active finals match)
        # at this point.
        matches = tournament.get_active_matches()
        self.assertEqual(len(matches), 1)
        C_match = tournament.get_active_matches_for_competitor('C')[0]
        tournament.add_win(C_match, 'C')

        # Round 4 (finals): A vs C
        matches = tournament.get_active_matches()
        # There should only be one match (the active finals match)
        # at this point.
        self.assertEqual(len(matches), 1)
        match = matches[0]
        # C (from the loser's bracket) beats A from the winner's bracket.
        tournament.add_win(match,'C')

        # There should now be a grand-finals match. The tournament
        # should not be over yet.
        self.assertIsNone(tournament.get_winners())

        matches = tournament.get_active_matches()
        # There should only be one match (the active grand-finals match)
        # at this point.
        self.assertEqual(len(matches), 1)
        match = matches[0]
        # In the grand-finals, 'A' beats 'C'
        tournament.add_win(match, 'A')
        # Now that the grand-finals are complete, 'A' should be the winner
        # of the whole tournament, and there should be 0 active matches.
        self.assertEqual(tournament.get_winners(), ['A'])
        self.assertEqual(tournament.get_active_matches(),[])

if __name__ == '__main__':
    unittest.main()