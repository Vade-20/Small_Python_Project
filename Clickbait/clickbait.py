import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']

STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana",
             "Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
             "New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",  "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
             "South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

NOUNS = ['Athlete', 'Clown',  'Doctor', 'Parent','Child','Influencer'
    'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game','Youtuber','Demon',
     'Serial Killer', 'Telephone Psychic', 'Singer', 'Teacher','Angel',
    'Musician',  'Fish', 'Painter', 'Detective','Runner','Spoiled Child',
    'Writer', 'Firefighter', 'Astronaut', 'Old People', 'Photographer',
    'Chef', 'Police Officer', 'Actor', 'Baker', 'Surgeon', 'Magician',
    'Engineer', 'Pilot', 'Dancer', 'Librarian', 'Farmer', 'Sculptor',
    'Journalist', 'Vampire', 'Witch', 'Zookeeper', 'Cyclist','Author','Sinner']

WHEN = ['Yesterday', 'After 12 PM', 'On a Blue Moon', 'During a Solar Eclipse', 'In the Middle of the Night','Soon', 'This Year', 'Next Week'
    'At Dawn', 'During Rush Hour Traffic', 'On a Snowy Day', 'During a Thunderstorm', 'During a Full Moon','Later Today',
    'At Sunset', 'On a Sunny Day', 'During a Lunar Eclipse', 'In the Early Morning', 'At Midnight',  'RIGHT NOW',
    'During a Tornado Warning', 'During a Heatwave', 'During a Meteor Shower', 'At High Noon', 'On a Rainy Evening',
    'At Dusk', 'During a Hailstorm', 'On a Foggy Morning', 'During a Solar Flare', 'During a Blizzard',
    'At Tea Time', 'On a Windy Afternoon', 'During a Sandstorm', 'In the Wee Hours', 'At the Break of Day',
    'During a Volcanic Eruption', 'On a Starry Night', 'During a Hurricane', 'During a Total Eclipse', 
    'On a Cloudy Day', 'During a Tsunami', 'During a Supermoon', 'At Cocktail Hour', 'On a Beach Vacation',
    'During a Zombie Apocalypse', 'In the Age of Dinosaurs', 'On a Space Mission', 'During a Time Travel Adventure', 
    'During a World War', 'In a Parallel Universe', 'On a Future Mars Colony', 'During a Robot Uprising',]

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
    'Workplace', 'Donut Shop', 'Apocalypse Bunker', 'Library', 'Coffee Shop',
    'Beach', 'Park', 'Museum', 'Hospital', 'Airport', 'Cinema',
    'Restaurant', 'Zoo', 'Amusement Park', 'Mountain', 'Lake',
    'River', 'Forest', 'Gym', 'Shopping Mall', 'Bar',
    'Post Office', 'Gas Station', 'Farm', 'Skyscraper', 'Cave',
    'Space Station', 'Subway Station', 'Train Station', 'Circus Tent', 'Haunted Mansion',
    'Casino', 'Waterfall', 'Cemetery', 'Jungle', 'Desert',
    'Cruise Ship', 'Lighthouse', 'Volcano', 'Castle', 'Lunar Colony',
    'Underwater Cave', 'Art Gallery', 'Wild West Saloon', 'Treehouse', 'Glacier',
    'Secret Laboratory']

def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break  # Exit the loop once a valid number is entered.

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)
        headline = {1:generateAreMillenialsKillingHeadline,
                    2:generateWhatYouDontKnowHeadline,
                    3:generateBigCompaniesHateHerHeadline,
                    4:generateYouWontBelieveHeadline,
                    5:generateDontWantYouToKnowHeadline,
                    6:generateGiftIdeaHeadline,
                    7:generateReasonsWhyHeadline,
                    8:generateJobAutomatedHeadline}

        print(headline.get(clickbaitType)())
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


# Each of these functions returns a different type of headline:
def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()