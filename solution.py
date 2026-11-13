import string

# Omvänt alfabet och omvända siffror. Varje tecken mappas på sin
# spegelbild: första tecknet byts mot sista, andra mot näst sista osv.
reversed_alphabet = string.ascii_lowercase[::-1]
reversed_digits = string.digits[::-1]

# Översättningstabell för str.translate. Stora bokstäver, å/ä/ö och
# skiljetecken finns inte i tabellen och lämnas därför oförändrade.
TABLE = str.maketrans(
    string.ascii_lowercase + string.digits,
    reversed_alphabet + reversed_digits,
)


def solution(note):
    """Dekryptera en lapp krypterad med Atbash-ciphern.

    Atbash är ett substitutionscipher där alfabetet speglas: a blir z,
    b blir y, c blir x osv. Siffrorna speglas på samma sätt (0 blir 9,
    1 blir 8 osv). Eftersom speglingen är sin egen invers används samma
    regel för både kryptering och dekryptering. Endast små bokstäver (a-z)
    och siffror ändras; stora bokstäver och övriga tecken lämnas som de är.

    Args:
        note: Den krypterade lappen (sträng).

    Returns:
        Den dekrypterade texten (sträng).
    """
    return note.translate(TABLE)


# Tester från skelettet
def test_abba():
    assert solution('abba') == 'zyyz'


def test_known_sentence():
    assert solution('Aoo blfi yzhv ziv yvolmt gl fh!') == 'All your base are belong to us!'


def test_ransom_note():
    assert solution('Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!') == 'Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!'


# Egna tester
def test_digits_are_mirrored():
    assert solution("0123456789") == "9876543210", "siffror ska speglas"


def test_uppercase_unchanged():
    assert solution("ABC XYZ") == "ABC XYZ", "stora bokstäver ska vara oförändrade"


def test_swedish_letters_and_punctuation_unchanged():
    assert solution("åäö, !?:") == "åäö, !?:", "övriga tecken ska vara oförändrade"


def test_roundtrip():
    text = "Hello World 2026!"
    assert solution(solution(text)) == text, "dubbel Atbash ger originalet"


if __name__ == "__main__":
    print(solution(
        "Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm "
        "uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!"
    ))