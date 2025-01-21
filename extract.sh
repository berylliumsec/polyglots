OFFSET=90   # Use the real offset you found
# Extract data directly into a shell variable
EMBEDDED_DATA="$(dd if=embedded_data.png bs=1 skip=$OFFSET 2>/dev/null)"
echo $EMBEDDED_DATA
