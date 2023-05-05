# Read the file
with open('MaasaiStories.txt', 'r') as file:
    content = file.read()

# Remove dashes
content = content.replace('-', '')

# Write the modified content back to the file
with open('MaasaiStories_modified.txt', 'w') as file:
    file.write(content)

print("Dashes removed and saved to 'MaasaiStories_modified.txt'.")