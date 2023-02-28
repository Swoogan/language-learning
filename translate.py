#!/bin/env python

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python translate.py <native-lang> <target-lang>")
        sys.exit(1)

    nl_file = sys.argv[1]
    tl_file = sys.argv[2]
    out_file = f"{nl_file}.out"

    with open(nl_file, "r") as nl, open(tl_file, "r") as tl, open(out_file, "w") as out:
        for en, fr in zip(nl, tl):
            print(en, end="")
            user_trans = input("Enter your translation: ")
            print(fr)

            out.write(en)
            out.write(fr)
            out.write(user_trans)
            out.write("\n\n")
