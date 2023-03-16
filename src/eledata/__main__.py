#!/usr/bin/env python3

import argparse
import json
import sys
from typing import Union, Dict, List, Iterable, Any

from .reader import read
from .writer import write


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file", required=True, help="Input file")
    parser.add_argument("-o", "--output-file", help="Output file")
    parser.add_argument("-f", "--from-format", default=None, help="Input format")
    parser.add_argument("-t", "--to-format", default=None, help="Output format")
    args = parser.parse_args()

    if args.from_format is None:
        if args.input_file.endswith(".json"):
            args.from_format = "json"
        elif args.input_file.endswith(".eld"):
            args.from_format = "eld"
        else:
            raise ValueError("Unknown input format and no format specified.")

    if args.to_format is None:
        if args.from_format == "json":
            args.to_format = "eld"
        elif args.from_format == "eld":
            args.to_format = "json"
        else:
            raise ValueError("Unknown output format and no format specified.")

    with open(args.input_file, "r") as f:
        data = read(f, args.from_format)

    if args.output_file:
        with open(args.output_file, "w") as f:
            write(f, data, args.to_format)
    else:
        write(sys.stdout, data, args.to_format)

if __name__ == "__main__":
    main()

