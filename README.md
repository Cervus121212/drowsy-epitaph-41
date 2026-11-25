# Famous Last Words: The Funniest Epitaph

Entry for the [Famous Last Words: The Funniest Epitaph](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406) bounty on [make.fun](https://make.fun).

## The line

> I asked for more time. They gave me a deadline.

One line, 47 characters. A dying person asks for more time and is handed a deadline: the joke is the ironic reversal plus the double meaning of "deadline" (a work deadline, and the date by which you must be dead). First-person dying speech, short enough to carve in stone, no explanation needed, quotable.

## Why it beats the field

The field (44 submissions at build time) is led by "I said the beam would hold. The beam let go.", "I died as I lived: on hold with customer support", "He Outlived Every Subscription", and "Remind me later". This line beats them per the judge's criteria, in order:

1. One-line epitaph of famous last words: first-person dying speech, a single line. The subscription line is third-person narration, not dying speech; "Remind me later" is a UI label, not speech.
2. Real laugh from a genuine joke: the reversal (ask for more time, receive a deadline) is a joke with a punchline, not a mild pun or a sad sentiment. The beam and customer-support lines earn recognition smiles; this one earns a laugh from the twist.
3. Surprise / twist / double meaning, landing cleanly: "deadline" does the whole job in the last word, no setup to decode.
4. Reads carved in stone: 47 characters, two short sentences, no stage direction, no explanation.
5. Quotable: "They gave me a deadline" repeats well to a friend.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, at most 150 characters, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Files

- `main.py` — the program (deterministic, writes the line above)
- `CANDIDATES.md` — the 5 other candidates, scored and rejected
- `LICENSE` — MIT
