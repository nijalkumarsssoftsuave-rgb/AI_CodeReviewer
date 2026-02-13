import ast

def validate_code(code: str, language_hint: str):
    """
    Lightweight validation strategy.
    Python → real parse check
    Others → accept (or extend later)
    """

    if language_hint.lower() == "python":
        try:
            ast.parse(code)
            return True, "OK"
        except Exception as e:
            return False, str(e)

    # For non-Python languages:
    return True, "Validation skipped (non-Python)"
