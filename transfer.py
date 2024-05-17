import re

def apply_replacements(content, replacements):
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    return content

def load_replacements(file_path):
    replacements = []
    with open(file_path, 'r') as file:
        for line in file:
            pattern, replacement = line.strip().split(' -> ')
            replacements.append((pattern, replacement))
    return replacements

def main(original, tagged, output_file):
    with open(original, 'r') as file:
        content = file.read()
    
    replacements = load_replacements(patterns_file)
    
    modified_content = apply_replacements(content, replacements)
    
    with open(output_file, 'w') as file:
        file.write(modified_content)
    
    print(f"Modified content has been written to {output_file}")

def new(original, tagged, output_file):
    matchname = re.compile(r'^\d ([^\(]*)\(.*$')
    matchnamesandtags = re.compile(r'^\d ([^\(]*)\([^#]*#(.*)$', re.MULTILINE)
    
    taggedcards = {} 
    with open(tagged, 'r') as tg:
        taggedcards = {name:tag for name, tag in matchnamesandtags.findall(tg.read())}
        print(taggedcards)
    with open(original, 'r') as og, open(output_file, 'w') as out:
        for line in og:
            cardname = matchname.match(line)
            if cardname:
                cardname = cardname.group(1)
                tag = ''
                if cardname in taggedcards:
                    tag = ' #' + taggedcards.get(cardname) + '\n'
                    line = line.rstrip() + tag
                out.write(line)
    print(taggedcards)

if __name__ == "__main__":
    original = 'deck1.txt'
    tagged = 'deck2.txt'
    combined = 'combined.txt'
    new(original, tagged, combined)

