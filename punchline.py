import json
from nltk.stem.snowball import SnowballStemmer
import string

stemmer = SnowballStemmer('english')
punctuations = str.maketrans('', '', string.punctuation)

def process_word(word):
    # Remove punctuation and stem the word.
    word = word.translate(punctuations)
    word = stemmer.stem(word)
    return word

# this is assuming you have the file already
# each line should be a json object for each reddit post
with open('dadjokes.json', 'r') as f:
    for line in f.readlines():
        line = json.loads(line.strip())

        # Skip non-self posts.
        # I'm not gonna visit some other website to get the joke.
        if not line['is_self']:
            continue
        
        # High tech joke processing.
        joke = (line['title'] + ' ' + line['selftext']).replace('\n', ' ').lower()

        # Even higher tech joke processing.
        words = joke.split(' ')
        words = [process_word(word) for word in words]
        words = [word.strip() for word in words if word]

        # Really short jokes are not funny.
        # Also, self posts that contain links? Not funny.
        if len(words) < 5 or any('http' in word for word in words):
            continue
        
        # The mods have removed the post, so I trust them to know what's not funny.
        if words[-1] == 'remov' or words[-1] == 'delet':
            continue
        
        # The punchline is the last four words of the joke.
        # Trust me, I'm a professional.
        punchline = '_'.join(words[-4:]).strip()

        # sort -n | uniq -c | sort -rn
        print(punchline)