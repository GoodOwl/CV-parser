import re

def extract_name(text):
    # Assuming the name is of length 2 or 3 words with capitalization
    words = re.findall(r'\b[A-Z][a-z]*\b', text)
    if len(words) >= 2 and len(words) <= 3:
        return ' '.join(words)
    return None

def extract_skills(text):
    # Search for a block of text starting with "Skills:" or "Technologies:"
    match = re.search(r'(?:Skills:|Technologies:)(.*?)(?=\b\w+:|$)', text, re.DOTALL)
    if match:
        skills_block = match.group(1)
        # Split the block into individual skills (assuming they are comma-separated)
        skills = [skill.strip() for skill in skills_block.split(',')]
        return skills
    return None
