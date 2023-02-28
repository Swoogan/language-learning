#!/bin/env python

import xml.etree.ElementTree as ET
import xml.sax.saxutils as saxutils
import sys
from typing import List


def extract_paragraphs(file_path: str) -> List[str]:
    tree = ET.parse(file_path)
    root = tree.getroot()

    paragraphs = []
    for p in root.iter("{http://www.w3.org/ns/ttml}p"):
        if p.text:
            paragraphs.append(saxutils.unescape(p.text))

    return paragraphs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    paragraphs = extract_paragraphs(file_path)
    for p in paragraphs:
        print(p)
