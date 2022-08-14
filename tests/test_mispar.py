import pytest

from gematria_engine import MisparHechrechi, MisparGadol, MisparhaAkhor


@pytest.fixture
def word() -> str:
    '''HaAretz: land
    '''
    return "הארץ"

def test_hechrechi(word: str) -> None:
    '''ה = 5
       1 = א
       ר = 200
       ץ = 90
       -> 296
    '''
    mispar: MisparHechrechi = MisparHechrechi()
    assert mispar.mispar(word) == 296

def test_gadol(word: str) -> None:
    '''ה = 5
       1 = א
       ר = 200
       ץ = 900
       -> 1,096
    '''
    mispar: MisparGadol = MisparGadol()
    assert mispar.mispar(word) == 1106

def test_haakhor(word: str) -> None:
    '''10^0 * ה = 5
       10^1 * 1 = א
       10^2 * ר = 200
       ץ = 90 * 3^10
       -> 110,015
    '''
    mispar: MisparhaAkhor = MisparhaAkhor()
    assert mispar.mispar(word) == 110015

def test_bad_word(capsys) -> None:
    bad_word: str = "ארץh"
    mispar: MisparHechrechi = MisparHechrechi()
    value: int = mispar.mispar(bad_word)
    assert value == 291
    captured = capsys.readouterr()
    assert captured.out.strip() == 'I don\'t recognize "h". Skipping it'
