"""Turn a year into a Roman-numeral release tag.

Usage:
    python scripts/roman_tag.py 2026
    -> 2026=MMXXVI

Requires the `roman` package from PyPI (import roman, then roman.toRoman).
"""

import sys

import roman


def roman_tag(year: int) -> str:
    """Return the release tag string for ``year`` (e.g. 2026 -> 2026=MMXXVI)."""
    return f"{year}={roman.toRoman(year)}"


def main() -> None:
    year = int(sys.argv[1]) if len(sys.argv) > 1 else 2026
    print(roman_tag(year))


if __name__ == "__main__":
    main()
