import random
def get_random_word(words):
    return random.choice(words)
names = ["Panayot", "Unufri", "Kurti", "Nafarforii", "Sokol", "Elena", 'Gergana', "Silvia", "Mariana", "Eva"]
places = ["Sofia", "Polski trumbesh", "Pavlikeni", "Varna", "Pazardjik"]
verbs = ['plays with', "holds", "kisses", 'gets', "drinks", "drops"]
nouns = ["bottle", "world", "nuts", "fish","drawers"]
adverbs = ["quickly", "funny", "lovely", "swimmingly", "phemomenaly", "scary"]
details = ["at work", "in the car", "over the moon", 'under the lights']
print("Hello, please enjoy your first random sentence!")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    print("Click [Enter] to generate a new one if you feel like it!")







