VERDICT: BUGS_FOUND

Das Produkt besteht zwar den pytest-Lauf (79 passed, exit 0), erfüllt aber das Akzeptanzkriterium AC-08 nicht. Der grüne Testlauf übergeht diese Abweichung, weil `tests/test_masking.py` die falschen Erwartungswerte enthält.

**Bug**

- **Title**: `mask_secret` liefert bei `keep=4` und im Standardfall falsche Maskierungslängen
- **Symptom**: Die Funktion `mask_secret` maskiert mehr Zeichen sichtbar als in AC-08 verlangt. Für `mask_secret('geheim123', keep=4)` liefert sie `'*****m123'` statt des spezifizierten `'******123'`; für `mask_secret('geheim')` liefert sie `'**heim'` statt `'**im'`. Damit ist die öffentliche API nicht konform zur Spezifikation.
- **Repro**: Direkter Aufruf `mask_secret("geheim123", keep=4)` bzw. `mask_secret("geheim")`. Der Testlauf `pytest tests/test_masking.py` meldet grün, weil die Assertions das falsche Verhalten erwarten.
- **Evidence**: AC-08 verlangt wörtlich `mask_secret('geheim123', keep=4) ergibt '******123'` und `mask_secret('geheim') ergibt '**im'`. Im Testcode `tests/test_masking.py` stehen dagegen `assert mask_secret("geheim123", keep=4) == "*****m123"` und `assert mask_secret("geheim") == "**heim"`; der pytest-Bericht zeigt `tests/test_masking.py::test_masks_all_but_last_keep_characters PASSED` und `tests/test_masking.py::test_default_keep_is_four PASSED`.
- **Suspected file(s)**: `validkit/masking.py` (Implementierung) und `tests/test_masking.py` (falsche Erwartungswerte). Da beide Dateien konsistent das falsche Verhalten abbilden, muss die Implementierung an AC-08 angepasst und der Test entsprechend korrigiert werden.
- **Severity**: high