
def test_greet() -> None:
    """Tests greet() from the package."""
    output = greet("Tushar")
    assert output == "Hello Tushar!"
