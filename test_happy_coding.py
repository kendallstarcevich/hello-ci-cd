from main import happy_coding


def test_happy_coding(capsys):
    """Call happy_coding() and assert it prints the expected message.
    Copilot wrote this test function."""
    happy_coding()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Happy coding!"