import markovify

# the format it's expecting
# is just 1 joke per line, plaintext
with open("data/all_jokes.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(50):
    print(text_model.make_sentence())