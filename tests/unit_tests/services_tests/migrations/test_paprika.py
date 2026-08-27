import pytest

from mealie.services.migrations.paprika import split_ingredients


@pytest.mark.parametrize(
    ("ingredients", "expected"),
    [
        ("1 cup flour\n2 eggs", ["1 cup flour", "2 eggs"]),
        ("1 cup flour\n2 eggs\n", ["1 cup flour", "2 eggs"]),
        ("1 cup flour\n2 eggs\n\n", ["1 cup flour", "2 eggs"]),
        ("1 cup flour\r\n2 eggs\r\n", ["1 cup flour", "2 eggs"]),
        ("", []),
    ],
)
def test_split_ingredients(ingredients: str, expected: list[str]) -> None:
    assert split_ingredients(ingredients) == expected
