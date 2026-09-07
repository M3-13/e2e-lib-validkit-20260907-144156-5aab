from pathlib import Path

VALIDKIT_DIR = Path(__file__).resolve().parent.parent / "validkit"

BANNED = ("eval(", "exec(", "pickle.loads")


def test_no_code_execution_constructs_in_validkit():
    offenders = []
    for source_file in VALIDKIT_DIR.rglob("*.py"):
        content = source_file.read_text(encoding="utf-8")
        for pattern in BANNED:
            if pattern in content:
                offenders.append(f"{pattern} in {source_file.name}")
    assert not offenders, f"Banned constructs found: {offenders}"
