VERDICT: CHANGES_REQUESTED

## EU Cyber Resilience Act (CRA) – Sicherheit durch Technikgestaltung

### AC-13: Reguläre Verarbeitung in `normalize_phone` erfolgt vor der Längenbegrenzung
Schweregrad: mittel

Befund: In `validkit/phone.py` wird der vollständige Eingabetext mit `_NON_DIGITS.sub("", text)` durch einen regulären Ausdruck verarbeitet, bevor die typspezifische Maximallänge geprüft wird. AC-13 verlangt, dass Eingaben für reguläre Ausdrücke vor dem Matchen auf eine typgerechte Maximallänge begrenzt werden; Überschreitungen müssen zu `ValueError` führen. Das Muster `\D` ist zwar linear und zeigt kein exponentielles Backtracking, die Reihenfolge verletzt aber das Kriterium und lässt unbegrenzt lange Eingaben in die reguläre Verarbeitung laufen.

Abhilfe:
- In `validkit/phone.py` die regexbasierte Filterung ersetzen, z. B. durch:
  `national = "".join(ch for ch in text if ch.isascii() and ch in "0123456789")`
  und den `re`-Import sowie `_NON_DIGITS` entfernen. Die bestehende Prüfung `len(digits) + len(national) > 15` bleibt danach erhalten und greift vor jeder weiteren Verarbeitung.
- Alternativ vor `_NON_DIGITS.sub(...)` eine dokumentierte Rohstring-Obergrenze einführen, z. B. `MAX_PHONE_INPUT_LENGTH = 64`, und Überschreitungen mit `ValueError` ablehnen.
- In `tests/test_phone.py` einen Test ergänzen, der eine sehr lange Eingabe, etwa `"1" * 10000`, mit `pytest.raises(ValueError)` prüft und sicherstellt, dass die Fehlermeldung keinen Eingabewert enthält.

## Datenschutz-Grundverordnung (DSGVO)

Kein Befund. AC-16 ist erfüllt: Die Fehlermeldungen aller neun Funktionen benennen ausschließlich Funktion und Fehlerursache und geben keine übergebenen Werte wie E-Mail-Adressen, Telefonnummern, IBAN oder Geheimtexte aus. Es sind keine Protokollierung, keine Persistenz und keine Übermittlung personenbezogener Daten sichtbar.

## EU AI Act

Nicht anwendbar: Die Bibliothek enthält keine KI-Funktion.

## Pflichttexte, Einwilligungsbanner, Barrierefreiheit

Nicht anwendbar: reine Python-Bibliothek ohne Endnutzer-UI, ohne Netzwerk und ohne Web-Oberfläche.

## Hinweise (nicht blockierend)

- Die Bibliothek verarbeitet personenbezogene Daten wie E-Mail-Adressen, Telefonnummern, IBAN und Geheimtexte ausschließlich flüchtig im Arbeitsspeicher der aufrufenden Anwendung. Rechtsgrundlage und Betroffenenrechte sind vom jeweiligen Integrator sicherzustellen.
- Für die CRA-Marktreife empfiehlt es sich, die Sicherheitseigenschaften wie Eingabelängengrenzen, lineare beziehungsweise regexfreie Muster und den Verzicht auf `eval`, `exec` und `pickle.loads` in `README.md` oder einer `SECURITY.md` zu dokumentieren und einen Meldeweg für Sicherheitsprobleme zu benennen. Dies wird von keinem Akzeptanzkriterium gefordert und trägt daher nicht das Urteil.
- AC-12 konnte nicht abschließend geprüft werden, weil der Inhalt der `README.md` im bereitgestellten Prüfstand nicht wiedergegeben ist; daraus wird kein Rechtsbefund abgeleitet.