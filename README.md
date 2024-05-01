# Polyglots

Welcome to Polyglots

![Polyglots](/images/polyglot.png)

## Galaxy

- [Polyglots](#Polyglots)
- [Galaxy](#galaxy)
- [Acknowledgement](#acknowledgement)
- [Introduction to Polyglots ](#acknowledgement)
- [System dependencies](#system-dependencies)
- [Making a python-png polyglot](#acknowledgement)


## Acknowledgement

**First i would like to thank the All-Mighty God who is the source of all knowledge, without Him, this would not be possible.**

### Introduction to Polyglots

A polyglot file is a file format that can be interpreted in more than one way by different systems. In this blog post, we'll explore how to create a polyglot file that is both a valid PNG image and a functional Python script. We'll discuss how you can execute the Python script portion using the Unix dd command, bypassing the need for complex extraction tools.

### System Dependencies

- pillow

Pillow can be installed like so:

```bash
pip3 install pillow
```

### Making a python-png polyglot

**Generate the PNG Image**

First, we use the Python Imaging Library (PIL) to create a simple PNG image. Here, we're making a 10x10 pixel blue image.


```python

from PIL import Image
import io

img = Image.new("RGB", (10, 10), color="blue")
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format="PNG")
png_data = img_byte_arr.getvalue()
```

**Embed the Python Script**

After creating the image, we append a Python script to it. We start by adding a marker #--PYTHON--# to denote the beginning of the Python script. This helps in identifying where the script starts within the binary file.

```python
marker = b"\n\n#--PYTHON--#\n"
python_script = b"""#!/usr/bin/env python3
print('Hello from your polyglot file!')
"""
polyglot_data = png_data + marker + python_script
```

**Save the Polyglot File**

We then save this combined data to a file and ensure it has the correct permissions to be executed.

```
polyglot_path = "executable_polyglot.png"
with open(polyglot_path, "wb") as file:
    file.write(polyglot_data)
import os
os.chmod(polyglot_path, 0o755)
```

**Executing the Python Script**

To run the embedded script without manually extracting it, you can use the dd command in Unix-based systems. This command is powerful for handling and transferring fixed blocks of data.

**Why dd?**
The dd command is traditionally used for copying and converting raw data. It is extremely useful in our case to skip the initial part of the file that contains the PNG data.

**Execution Command**

Since we know the exact byte where the Python script starts after the #--PYTHON--# marker (offset 90 bytes in this example), we can instruct dd to skip directly to this point and pipe the result to Python for execution:

```bash
dd if=executable_polyglot.png bs=1 skip=90 | python3
```
**Conclusion**

This approach illustrates not only the versatility of combining different data types into a single file but also demonstrates practical command-line skills for extracting and executing parts of binary files. Understanding how to manipulate and utilize polyglot files can be a valuable skill in many IT and security-related fields.