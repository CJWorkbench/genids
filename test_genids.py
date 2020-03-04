import unittest
from genids import render
import pandas as pd
from pandas.testing import assert_frame_equal
from cjwmodule.testing.i18n import i18n_message


class RenderTest(unittest.TestCase):
    def test_default_colname_is_ID(self):
        result = render(pd.DataFrame({"A": [1, 2, 3]}), {"outcolname": ""})
        self.assertEqual(result["column_formats"], {"ID": "{:d}"})
        assert_frame_equal(
            result["dataframe"], pd.DataFrame({"ID": [1, 2, 3], "A": [1, 2, 3]})
        )

    def test_outcolname(self):
        result = render(pd.DataFrame({"A": [1, 2, 3]}), {"outcolname": "X"})
        self.assertEqual(result["column_formats"], {"X": "{:d}"})
        assert_frame_equal(
            result["dataframe"], pd.DataFrame({"X": [1, 2, 3], "A": [1, 2, 3]})
        )

    def test_empty_table(self):
        result = render(pd.DataFrame({"A": []}), {"outcolname": "X"})
        self.assertEqual(result["column_formats"], {"X": "{:d}"})
        assert_frame_equal(result["dataframe"], pd.DataFrame({"X": [], "A": []}))

    def test_overwrite_column(self):
        result = render(pd.DataFrame({"A": [1], "B": [2]}), {"outcolname": "B"})
        self.assertEqual(result["column_formats"], {"B": "{:d}"})
        self.assertEqual(
            result["error"],
            i18n_message("warning.columnAlreadyExisted.message", {"column_name": "B"}),
        )
        assert_frame_equal(result["dataframe"], pd.DataFrame({"B": [1], "A": [1]}))


if __name__ == "__main__":
    unittest.main()
