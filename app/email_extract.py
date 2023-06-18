import re

def extract_email(email_content):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_pattern_compile = re.compile(pattern)
    email_extracted_result = email_pattern_compile.search(email_content)
    email_extracted = email_extracted_result.group()

    print(email_extracted_result)

    return email_extracted

email_content = "hi what are you doing? aarshps@gmail.com has all the time! aarshps2@gmail.com"
email_extracted = extract_email(email_content)

print(email_extracted)
