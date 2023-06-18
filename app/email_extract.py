import re

def extract_email(email_content):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_pattern_compile = re.compile(pattern)
    emails_extracted = email_pattern_compile.findall(email_content)

    return emails_extracted

email_content = "hi what are you doing? aarshps@gmail.com has all the time! aarshps2@gmail.com"
emails_extracted = extract_email(email_content)

print(emails_extracted)
