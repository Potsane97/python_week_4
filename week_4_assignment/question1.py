# File Read & Write Challenge 🖋️

# Read from input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Modify content (uppercase + word count)
word_count = len(content.split())
processed_text = content.upper()

# Write to output.txt
with open("output.txt", "w") as f:
    f.write(processed_text)
    f.write("\n\nWord Count: " + str(word_count))

print("✅ File processed and saved as output.txt")