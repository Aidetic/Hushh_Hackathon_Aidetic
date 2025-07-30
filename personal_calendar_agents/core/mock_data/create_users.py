import os

usernames = [
    "vishsharma509522@gmail.com",
    "biditamukherjee11@gmail.com",
    "pandeygag78934@gmail.com",
    "naynaaggarwal6@gmail.com",
    "arvindsarda84@gmail.com"
]

passwords = [
    "helloiamvishal",
    "helloiambidita",
    "helloiamgagan",
    "helloiamnayna",
    "helloiamarvind"
]

preferences_list = [
    # Vishal Sharma
    """full_name: Vishal Sharma

likes:
  - Gadgets, smartwatches, headphones, and new tech
  - Football, cricket, gym
  - Cooking easy recipes
  - Board games (Codenames, Chess, Uno)
  - Road trips with friends
  - Trying out microbreweries

gift_preferences:
  - Latest earphones, tech gadgets, personalized mugs, sports gear

party_preferences:
  - Small gatherings at home or terrace
  - Live music, open-mic, karaoke nights
  - Loves organizing surprise parties for friends
  - Prefers pizzas, finger foods, and mocktails

travel_preferences:
  - Adventure trips, mountain trekking, camping, driving outstation
  - Budget trips with friends, hill stations, or beach getaways
  - Loves making detailed travel itineraries

academic/career_interests:
  - Data science, hackathons, coding events, open-source projects
  - Enjoys helping friends with coding and math assignments

social_style:
  - Extrovert, likes being in the center of group chats, often plans outings

quirks:
  - Always gifts tech or books, never misses a friend's birthday
  - Gets competitive at games night
""",
    # Bidita Mukerjee
    """full_name: Bidita Mukerjee

likes:
  - Painting, classical music, poetry
  - Gardening and taking care of indoor plants
  - Scented candles, soft toys, handmade gifts

gift_preferences:
  - Handwritten notes, art supplies, scented candles, plushies

party_preferences:
  - Prefers cozy house parties, DIY decorations, movie marathons
  - Loves dessert tables (cakes, brownies, cupcakes)
  - Enjoys karaoke and charades

travel_preferences:
  - Prefers heritage sites, museums, art galleries
  - Weekend trips to quiet places, yoga retreats

academic/career_interests:
  - Literature, psychology, enjoys book clubs and creative writing events

social_style:
  - Ambivert, enjoys deep conversations with small groups

quirks:
  - Will make cards for every occasion, dislikes last-minute plans
""",
    # Gagan Pandey
    """full_name: Gagan Pandey

likes:
  - All kinds of sports (especially cricket and football)
  - Gaming (console and PC), FIFA, fantasy leagues
  - Eating out (fast food, burgers, biryani)
  - Stand-up comedy, live matches

gift_preferences:
  - Sports merchandise, jerseys, gaming accessories, tickets to matches

party_preferences:
  - Loves large parties, game nights, watching matches with friends
  - Prefers venues with big screens for match streaming
  - Enjoys BBQ, biryani, wings, and beer

travel_preferences:
  - Spontaneous weekend getaways
  - Adventure sports (rafting, rock climbing, cycling trips)
  - Road trips and exploring new cafes

academic/career_interests:
  - Management, marketing, sports analytics, event organizing

social_style:
  - Extrovert, often the entertainer and prankster of the group

quirks:
  - Always brings board games, tries to turn every event into a competition
""",
    # Nayna Aggarwal
    """full_name: Nayna Aggarwal

likes:
  - Reading novels, collecting bookmarks, journaling
  - Plants, home decor, aromatherapy
  - Baking cookies and cupcakes
  - K-dramas, Bollywood music

gift_preferences:
  - Books, custom jewelry, scented diffusers, plants

party_preferences:
  - Small tea parties or themed brunches
  - Loves making personalized playlists for friends
  - Prefers homemade food, salad bars, fruit punches

travel_preferences:
  - Beach vacations, spa retreats, shopping destinations
  - Enjoys solo travel and city explorations

academic/career_interests:
  - Psychology, counseling, creative writing

social_style:
  - Mostly introvert, but opens up with close friends

quirks:
  - Forgets birthdays but always brings the best homemade desserts
""",
    # Arvind Sarda
    """full_name: Arvind Sarda

likes:
  - Jazz music, vinyl record collecting
  - Cooking new cuisines, especially Italian
  - Photography, road cycling

gift_preferences:
  - Gourmet chocolates, wine, kitchen gadgets, coffee blends

party_preferences:
  - Enjoys wine-and-cheese nights, rooftop parties, and brunches
  - Likes planning themed events (retro, 80s, travel-inspired)

travel_preferences:
  - Wine trails, cultural tours, mountain biking holidays
  - Interested in international travel, prefers Airbnb stays

academic/career_interests:
  - Finance, entrepreneurship, culinary arts

social_style:
  - Calm, reserved in big groups but great conversationalist one-on-one

quirks:
  - Takes over the BBQ at every party, always suggests photo sessions
"""
]

base_dir = f"{os.getenv('DATABASE')}/agents/personal"
for i, username in enumerate(usernames):
    userpath = os.path.join(base_dir, username)
    os.makedirs(userpath, exist_ok=True)
    # Write password
    passpath = os.path.join(userpath, "pass.txt")
    with open(passpath, "w") as f:
        f.write(passwords[i])
    # Write preferences
    prefpath = os.path.join(userpath, "preferences.txt")
    with open(prefpath, "w") as f:
        f.write(preferences_list[i])
