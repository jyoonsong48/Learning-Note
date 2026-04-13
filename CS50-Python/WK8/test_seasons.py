import pytest
from unittest.mock import patch
from datetime import date
from seasons import main
from io import StringIO

def test_date_input():
    with patch("seasons.date") as mock_date:
        mock_date.today.return_value = date(2000, 1, 1)
        mock_date.fromisoformat.side_effect = date.fromisoformat
        # valid date는 main()이 아닌 직접 계산으로 테스트
    with pytest.raises(SystemExit):
        with patch("builtins.input", return_value="20200402"):
            main()
    with pytest.raises(SystemExit):
        with patch("builtins.input", return_value="2 April, 2020"):
            main()

def test_output():
    with patch("seasons.date") as mock_date:
        mock_date.today.return_value = date(2000, 1, 1)
        mock_date.fromisoformat.side_effect = date.fromisoformat
        with patch("builtins.input", return_value="1999-01-01"):
            from io import StringIO
            import sys
            captured = StringIO()
            sys.stdout = captured
            main()
            sys.stdout = sys.__stdout__
            assert captured.getvalue().strip() == "Five hundred twenty-five thousand, six hundred minutes"
