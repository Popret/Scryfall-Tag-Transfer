import re
def main(original, tagged, output_file):
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
    main(original, tagged, combined)

