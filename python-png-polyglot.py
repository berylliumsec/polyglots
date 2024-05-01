import io
import os
from PIL import Image

# Create a simple image
img = Image.new("RGB", (10, 10), color="blue")
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format="PNG")
png_data = img_byte_arr.getvalue()

# Define a marker and a Python script
marker = b"\n\n#--PYTHON--#\n"  # Ensure this is enough to start on a new line
python_script = b"""#!/usr/bin/env python3
print('Hello from your polyglot file!')
"""

# Combine the image, marker, and Python script
polyglot_data = png_data + marker + python_script

# Save to a file
polyglot_path = "executable_polyglot.png"
with open(polyglot_path, "wb") as polyglot_file:
    polyglot_file.write(polyglot_data)

# Set executable permissions
os.chmod(polyglot_path, 0o755)  # Makes the file executable
