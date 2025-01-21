#!/usr/bin/env python3
"""
binary_polyglot.py

This script demonstrates how to create a simple 10x10 PNG file with the Python
Imaging Library and then append arbitrary binary bytes at the end, identified
by a unique marker (#--BINARY--#).

Usage:
    python3 binary_polyglot.py
    # Produces a file named 'binary_polyglot.png'.
    # This file can be viewed as a normal PNG image
    # AND it contains raw binary data after the marker.
"""

import os
import io
from PIL import Image

# 1. Create a simple PNG in memory (10x10 blue image).
img = Image.new("RGB", (10, 10), color="blue")
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format="PNG")
png_data = img_byte_arr.getvalue()

# 2. Define a marker that we'll use to locate the embedded data.
#    We put "\n" before it so it doesn't accidentally form a valid chunk in the PNG data,
#    but the main reason is just to have a textual pivot point we can 'grep' for.
marker = b"\n#--BINARY--#\n"

# 3. Here is an example of arbitrary bytes.
#    This can include null bytes, high-ASCII bytes, control codes, etc.
#    We'll illustrate that by mixing text, binary, and escape sequences.
#    '\x00'   = Null byte
#    '\xFE'   = 254 in decimal
#    '\xFF'   = 255 in decimal
#    '\n'     = newline
binary_data = b"\x00\x01\x02\x03\xFE\xFF\x00\x10"

# Combine the PNG data + marker + arbitrary binary data
polyglot_data = png_data + marker + binary_data

# 4. Write out the combined file
polyglot_path = "binary_polyglot.png"
with open(polyglot_path, "wb") as f:
    f.write(polyglot_data)

# 5. (Optional) Make it executable if you want to treat it like a script
os.chmod(polyglot_path, 0o755)

print(f"[+] Created '{polyglot_path}' with {len(polyglot_data)} bytes total.")
print("[+] You can open it in an image viewer to see the 10x10 blue square.")
print("[+] You can also locate '#--BINARY--#' to extract the raw binary bytes.")


