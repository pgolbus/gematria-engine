import pytest

from gematria_engine import MisparHechrechi, MisparGadol, MisparhaAkhor


@pytest.fixture
def word() -> str:
    """HaAretz: land"""
    return "הארץ"


@pytest.fixture
def bad_word() -> str:
    """HaAretz: land"""
    return "haארץ"


def test_hechrechi(word: str) -> None:
    """ה = 5
    1 = א
    ר = 200
    ץ = 90
    -> 296
    """
    mispar: MisparHechrechi = MisparHechrechi()
    assert mispar.mispar(word) == 296


def test_gadol(word: str) -> None:
    """ה = 5
    1 = א
    ר = 200
    ץ = 900
    -> 1,096
    """
    mispar: MisparGadol = MisparGadol()
    assert mispar.mispar(word) == 1106


def test_haakhor(word: str) -> None:
    """10^0 * ה = 5
    10^1 * 1 = א
    10^2 * ר = 200
    ץ = 90 * 3^10
    -> 110,015
    """
    mispar: MisparhaAkhor = MisparhaAkhor()
    assert mispar.mispar(word) == 110015


def test_bad_word(bad_word) -> None:
    mispar: MisparHechrechi = MisparHechrechi()
    with pytest.raises(ValueError, match=f'I don\'t recognize "h" in {bad_word}'):
        mispar.mispar(bad_word)


def test_bad_word_strip(bad_word) -> None:
    """meh = h
    meh = a
    1 = א
    ר = 200
    ץ = 90
    -> 291
    """
    mispar: MisparHechrechi = MisparHechrechi(strip=True)
    assert mispar.mispar(bad_word) == 291


def test_bad_word_haakhor(bad_word) -> None:
    mispar: MisparhaAkhor = MisparhaAkhor()
    with pytest.raises(ValueError, match=f'I don\'t recognize "h" in {bad_word}'):
        mispar.mispar(bad_word)


def test_bad_word_strip_haakhor(bad_word) -> None:
    """meh = h
    meh = a
    10^0 * 1 = א
    10^1 * 200 = ר
    10^2 * ץ = 90
    -> 11,001
    """
    mispar: MisparhaAkhor = MisparhaAkhor(strip=True)
    assert mispar.mispar(bad_word) == 11001
