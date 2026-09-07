# validkit

Eine kleine, eigenständige Python-Bibliothek mit neun unabhängigen, reinen
Prüf- und Normalisierungsfunktionen: E-Mail-Validierung, Luhn-Prüfung,
IBAN-Validierung, ISBN-13-Validierung, Telefonnummer-Normalisierung (E.164),
Akzent-Entfernung, Geheimtext-Maskierung, Slugify und Clamp. Es werden
ausschließlich Module der Standardbibliothek verwendet — keine CLI, keine UI,
kein Netzwerk.

## Tech-Stack

- **Sprache:** Python (3.9+)
- **Abhängigkeiten:** nur Standardbibliothek; `pytest` als Entwicklungsabhängigkeit
- **Testing:** pytest
- **Verpackung:** eigenständiges Python-Paket (`validkit/__init__.py`)

## Installation

```bash
python -m pip install pytest
```

## Tests ausführen

```bash
python -m pytest
```

## Verwendung

```python
from validkit import (
    clamp,
    is_valid_email,
    is_valid_iban,
    is_valid_isbn13,
    luhn_check,
    mask_secret,
    normalize_phone,
    slugify,
    strip_accents,
)
```

Jede Funktion hat genau ein Beispiel mit Eingabe und erwarteter Ausgabe:

| Funktion | Eingabe → Ausgabe |
| --- | --- |
| `is_valid_email(text)` | `is_valid_email('a.b@example.com')` → `True` |
| `luhn_check(digits)` | `luhn_check('79927398713')` → `True` |
| `is_valid_iban(text)` | `is_valid_iban('DE44 5001 0517 5407 3249 31')` → `True` |
| `is_valid_isbn13(text)` | `is_valid_isbn13('978-3-16-148410-0')` → `True` |
| `normalize_phone(text, country_code)` | `normalize_phone('030 1234 567', 49)` → `'+49301234567'` |
| `strip_accents(text)` | `strip_accents('München — café')` → `'Munchen — cafe'` |
| `mask_secret(text, keep=4)` | `mask_secret('geheim123', keep=4)` → `'*****m123'` |
| `slugify(text)` | `slugify('Héllo, Wörld!')` → `'hello-world'` |
| `clamp(value, low, high)` | `clamp(-3, 0, 10)` → `0` |

## Funktionen

- `is_valid_email(text: str) -> bool` — prüft eine E-Mail-Adresse.
- `luhn_check(digits: str) -> bool` — prüft eine Ziffernfolge mit dem Luhn-Algorithmus.
- `is_valid_iban(text: str) -> bool` — prüft eine IBAN (Modulo-97).
- `is_valid_isbn13(text: str) -> bool` — prüft eine ISBN-13.
- `normalize_phone(text: str, country_code) -> str` — normalisiert eine Telefonnummer nach E.164.
- `strip_accents(text: str) -> str` — entfernt Diakritika.
- `mask_secret(text: str, keep: int = 4) -> str` — maskiert einen Geheimtext.
- `slugify(text: str) -> str` — erzeugt einen URL-freundlichen Slug.
- `clamp(value, low, high) -> int | float` — begrenzt einen Wert auf ein Intervall.

## Fehlerkonvention

Alle Funktionen werfen bei falschem Typ einen `TypeError` und bei inhaltlich
ungültiger Eingabe einen `ValueError`. Fehlermeldungen nennen Funktion und
Ursache, niemals die übergebenen Eingabewerte.
