#!/bin/bash

TMPFILE=$(mktemp)

echo -e "Parsing to json:\n"

python -m src.eledown.__main__ -i examples/first.eld -f eld | tee "$TMPFILE" | jq && (
	echo -e "\n\nParsing back to eledown:\n"
	python -m src.eledown.__main__ -f json -i "$TMPFILE" &&
	rm -f "$TMPFILE"
) || (
	echo "ERROR: TMPFILE preserved at $TMPFILE"
	exit 20
)

