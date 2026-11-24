"""Third pride line: eleven years mopping one hospital floor."""

import os

LINE = "After eleven years mopping the same hospital floor, my uncle walked in wearing a nurse badge with his own name on it — and the whole ward stood up and clapped."


def emit() -> None:
    """Drop the pride line into /output/entry.txt with no trailing newline."""
    # The payoff sits in the final clause: the whole ward stands up.
    size = len(LINE)
    if size == 0 or size > 240:
        raise SystemExit("pride line must be 1-240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


emit()
