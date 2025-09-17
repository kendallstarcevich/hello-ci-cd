import importlib.util
import pathlib


def _load_main_module():
    """Load the project's main.py directly by path to avoid import ambiguities in CI."""
    proj_root = pathlib.Path(__file__).parent
    main_path = proj_root / "main.py"
    spec = importlib.util.spec_from_file_location("main", str(main_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_happy_coding(capsys):
    """Call happy_coding() and assert it prints the expected message."""
    main = _load_main_module()
    main.happy_coding()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Happy coding!"