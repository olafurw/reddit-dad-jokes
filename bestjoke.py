class Joke:
    def __init__(self, punchline, timestamp, rating):
        self.punchline = punchline
        self.timestamp = int(timestamp)
        self.rating = int(rating)

    def __str__(self):
        return f'{self.punchline} {self.timestamp} {self.rating}'

    def __repr__(self):
        return self.__str__()

jokes = {}

# format it's expecting each line is is "punchline timestamp rating", like:
# get_to_the_other_side 1580000000 100
with open('bestjoke.txt', 'r') as f:
    for line in f.readlines():
        section = line.strip().split(' ')
        if len(section) != 3:
            continue
        
        # punchline, timestamp, rating
        joke = Joke(section[0], section[1], section[2])

        if joke.punchline not in jokes:
            jokes[joke.punchline] = []
        
        # Group jokes by punchline.
        jokes[joke.punchline].append(joke)

for punchline, joke_list in jokes.items():
    joke_length = len(joke_list)

    # You haven't been posted enough times to be the best joke.
    if joke_length < 100:
        continue
    
    # The joke fell flat at least once, can't be the best joke.
    if any(joke.rating == 0 for joke in joke_list):
        continue

    # Remove top 10% of the jokes. Going viral doesn't make you the best joke.
    sorted_jokes = sorted(joke_list, key=lambda joke: joke.rating)
    sorted_jokes = sorted_jokes[:int(joke_length * 0.9)]

    # Calculate the average rating of the joke.
    average_rating = sum(joke.rating for joke in sorted_jokes) / len(sorted_jokes)
    average_rating = int(round(average_rating, 0))
    
    print(average_rating, punchline)

