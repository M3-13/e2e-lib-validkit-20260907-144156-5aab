VERDICT: CHANGES_REQUESTED

## Befund 1 (medium) — AC-13 verletzt: `normalize_phone` begrenzt Eingabe nicht vor dem regulären Ausdruck

**Betroffene Datei:** `validkit/phone.py`

**Problem:**  
Der reguläre Ausdruck `_NON_DIGITS.sub("", text)` wird auf die gesamte, ungeprüfte Eingabe `text` angewendet, bevor irgendeine Längenprüfung stattfindet. Die Prüfung `if len(digits) + len(national) > 15` erfolgt erst **nach** dem Regex-Sub. AC-13 verlangt ausdrücklich, dass Eingaben für reguläre Ausdrücke **vor dem Matchen** auf eine typgerechte Maximallänge begrenzt werden. Ein extrem langer Eingabestring (z. B. mehrere Megabyte Sonderzeichen) kann so unnötig CPU- und Speicherressourcen binden, bevor die Funktion einen `ValueError` auslöst. Der verwendete Regex `\D` ist zwar linear und nicht anfällig für exponentielles Backtracking, das Risiko ist also begrenzt — die Vorgabe aus AC-13 wird aber nicht erfüllt.

**Konkreter Fix:**  
Vor dem Aufruf von `_NON_DIGITS.sub` eine Längenprüfung der gesamten Eingabe durchführen. Zusätzlich kann die Ziffernanzahl vorab gezählt werden, um die spätere Prüfung früh zu erzwingen.

Beispiel:

```python
MAX_PHONE_TEXT_LENGTH = 64  # großzügig genug für alle realistischen Formate

def normalize_phone(text: str, country_code: int | str) -> str:
    if not isinstance(text, str):
        raise TypeError("normalize_phone: text must be a string")

    if len(text) > MAX_PHONE_TEXT_LENGTH:
        raise ValueError("normalize_phone: phone number input exceeds the maximum length")

    # optional: Ziffernanzahl vorab zählen, um die Prüfung vor dem Regex zu ermöglichen
    digit_count = sum(c.isdigit() for c in text)

    if isinstance(country_code, int):
        digits = str(country_code)
    elif isinstance(country_code, str):
        code = country_code.strip()
        if code.startswith("+"):
            code = code[1:]
        digits = COUNTRY_CODES.get(code.upper(), code)
    else:
        raise TypeError("normalize_phone: country_code must be an int or str")

    if not digits.isdigit():
        raise ValueError("normalize_phone: invalid country code")

    if digit_count + len(digits) > 15:
        raise ValueError("normalize_phone: phone number exceeds 15 digits")

    national = _NON_DIGITS.sub("", text)
    if not national:
        raise ValueError("normalize_phone: phone number contains no digits")

    if national.startswith("0"):
        national = national[1:]
    if not national:
        raise ValueError("normalize_phone: phone number has no national number")

    return "+" + digits + national
```

Damit wird der reguläre Ausdruck erst nach den Längenprüfungen ausgeführt und AC-13 ist erfüllt. Die Fehlermeldungen bleiben frei von Eingabewerten (AC-16).

## Notes (non-blocking)

- Die Scanner `bandit` und `semgrep` wurden als `[skipped]` gemeldet und sind nicht gelaufen. Für dieses Projekt (nur Standardbibliothek, keine externen Abhängigkeiten, kein Netzwerk) ist das Risiko gering, aber es fehlen automatisierte SAST-/Dependency-Befunde.
- In `validkit/clamp.py` und `validkit/phone.py` wird die PEP-604-Syntax `int | float` bzw. `int | str` verwendet. Diese ist erst ab Python 3.10 lauffähig, während die Spec Python 3.9+ angibt. Dies ist kein Security-Kriterium, aber ein möglicher Kompatibilitätshinweis.