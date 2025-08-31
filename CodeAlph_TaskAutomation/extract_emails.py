# Extract all email addresses from a .txt file

import re

input_file = "/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlph_TaskAutomation/data.txt"
output_file = "/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlph_TaskAutomation/emails.txt"

with open(input_file, "r") as f:
    text = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

with open(output_file, "w") as f:
    for email in emails:
        f.write(email + "\n")

print(f"Extracted {len(emails)} emails and saved to email.txt")