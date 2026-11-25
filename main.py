"""The Funniest Honest Appliance Error — make.fun entry.

Writes one honest appliance error message to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and validates the 1-200 character gate twice: once on the
string itself, once on the file read back from disk.
"""

import os

LINE = "Error: drum unbalanced. The load is one shoe. I have spun it 47 times. It is still one shoe."

MIN_CHARS = 1
MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line or not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise SystemExit(
            "gate failed: line is %d chars, need %d-%d"
            % (len(line), MIN_CHARS, MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("gate failed: file content differs from the line")
    if not written.strip() or not MIN_CHARS <= len(written) <= MAX_CHARS:
        raise SystemExit(
            "gate failed on file: %d chars" % len(written)
        )
    print(line)
    print("chars: %d" % len(line))


if __name__ == "__main__":
    main()
