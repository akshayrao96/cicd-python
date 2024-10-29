from click.testing import CliRunner
from cli.__main__ import greet

def test_greet():
    """ Test the greet function
    """
    runner = CliRunner()
    test_name = "random"
    result = runner.invoke(greet, args=['--name',test_name])
    assert result.exit_code == 0
    assert result.output.strip() == f"Hello {test_name}"