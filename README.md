# Uppgift 1: Dekryptera ransomware-meddelandet

## Svar
Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!

## Vad programmet gör
Först tittade jag på exempeltesterna och såg att `abba` blir `zyyz`, alltså att varje bokstav byts mot den som står lika långt från andra änden av alfabetet. Det är Atbash-ciphern. Siffrorna fungerar likadant, så 0 blir 9, 1 blir 8 och så vidare.

I koden bygger jag en översättningstabell med `str.maketrans` och kör sedan `translate` på meddelandet. Det som inte finns i tabellen, som stora bokstäver, å, ä, ö och skiljetecken, ändras inte alls, vilket är precis vad uppgiften ville.

## Så kör du programmet
Gå in i mappen `uppgift-1/` och skriv:

- `uv run python solution.py` för att skriva ut det dekrypterade meddelandet
- `uv run pytest solution.py` för att köra testerna

## Antaganden
- Bara små bokstäver (a-z) och siffror (0-9) ska dekrypteras, som det står i uppgiften.
- Allt annat lämnas som det är.# PythonKurs-RANSOM-1
# PythonKurs-RANSOM-1
