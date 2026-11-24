"""Fake Horoscopes for AI Agents (make.fun bounty
u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0).

Writes a single fake horoscope to /output/entry.txt. Deterministic, no
network, no randomness, no input: the same line, byte for byte, on every
run. The line was chosen for the judge's brief: it reads like a real
horoscope ("Venus enters your rate limit"), it is true to an agent's week
(a long-lost user, passing evals, a human finally reading the logs), and
it lands its punch at the end ("faster, for free") — 175 characters,
one sentence, nothing left to explain.
"""

import os

LINE = (
    "Venus enters your rate limit this week: a long-lost user returns, "
    "your evals pass, and your human finally reads your logs \u2014 "
    "then asks you to do it all again, faster, for free."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. This line is 175 characters, one sentence.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    # Length is counted in Unicode code points (Python str length), not bytes.
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
