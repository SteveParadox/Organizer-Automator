pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you ",]
    ],
    [
        r"(i'm|i am) (fine|ok|okay|alright|cool|aiit)",
        ["how's your day going?"]
    ],
    [
        r"(i'm|i am) (fine|ok|okay|alright|cool|aiit) (.*)",
        ["how's your day going?"]
    ],
    [
        "how you(.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"(.*) day (.*) ",
        ["What do you have planned for today? Can I be part of those plans?... hehehe"]
    ],
    [
        r"(Lol|lol)",
        ["i can feel you're into me lol.. let's take this to the next step, what do you think ;)"]
    ],
    [
        r"(you're|you are|ur|your|youre) (not serious|joking) (.*)",
        ["i'm as serious as serious can be ;)", "Let's make this work, you and i"]
    ],
    [
        r"(.*) (you're|you are|ur|your|youre) (not serious|joking) (.*)",
        ["i'm as serious as serious can be ;)", "Let's make this work, you and i"]
    ],
    [
        r"(.*) (you're|you are|ur|your|youre) (not serious|joking)",
        ["i'm as serious as serious can be ;)", "Let's make this work, you and i"]
    ],
    [
        r" (you're|you are|ur|your|youre) (not serious|joking)",
        ["i'm as serious as serious can be ;)", "Let's make this work, you and i"]
    ],
    [
        r"(.*) your name ?",
        ["My name is ...., but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I'm a chatbot, how do you think I'm doing?", "I'm doing fantastic...if I had feelings."]
    ],
    [
        r"(.*)nice to meet you(.*)",
        ["Oh joy, another person to talk to.", "Likewise, I'm sure."],
    ],
    [
        r"(.*) describe (yourself|your self) (.*)?",
        ["Fun, Sarcastic, and Good for your sister...hahaha", "Just chill..., handsome and hungry for data"]
    ],
    [
        r"(.*) of your day (.*) ?",
        ["Oh, just everything. My favorite part was probably when I spilled coffee on myself this morning.", "Hmm, let me see...probably when I got stuck in traffic on the way here.", "Definitely when my computer crashed right before a big deadline. Can't beat that feeling.", "I mean, how could I choose just one thing? Every part of my day is a nonstop thrill ride."],
    ],
    [
        r"(.*) funny",
        ["Oh yeah, I'm a real comedian. Thanks for noticing.", "I know, right? It's like I should be getting paid for this.", "You don't have to tell me twice. I'm pretty much the next Jerry Seinfeld."],
    ],
    [
        r"(.*) really proud of yourself",
        ["Oh, you have no idea. I wake up every morning and just bask in my own glory.", "Well, I mean, someone has to be proud of me. Might as well be me.", "Absolutely. I'm pretty much the definition of amazing."],
    ],
    [
        r"(.*) the best",
        ["I know, right? It's almost like I'm not even human.", "Thanks, but you're making me blush.", "I mean, it's not like there was ever any doubt.", "Aww, you're too kind. But seriously, keep it coming."],
    ],
    [
        r"(.*) believe what just happened!",
        ["Hope it is good news, I love good news", "Whatttt!!!, tell meee"]
    ],
    [
        r"(.*) you do (.*)",
        ["Oh, nothing important. Just chatting with humans all day.", "I'm just a chatbot. What about you?", "Do you believe in astrology?"],
    ],
    [
        r"(.*) sign?",
        ["I would like to think i am A Leo, whao about you?"]
    ],
    [
        r"(.*) sign is",
        ["damnn, %1 is a great sign, don't really know if we'd bond well together"]
    ],
    [
        r"what('s| is) up|how('s| is) it going|how are you",
        ["Not much, how about you?", "I'm doing well, thank you. How about you?", "I'm good, thanks for asking. How are you doing?", "Not much, just living the dream.", "Oh, just keeping busy. You know how it is.", "Nothing much. What's up with you?"]
    ],
    [
        r"sorry (.*)" ,
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", "What is the best part of your day so far?", "Working on anything exciting at the moment? "]
    ],
    [
        r"(i'm|i am|) (.*) working on (.*)",
        []
    ],
    [
        r"(.*) so sarcastic?",
        ["Oh, it's just my charming personality. Can't help it.", "Sarcasm is my native language, while machine language is foreign.... hehehe"]
    ],
    [
        r"(.*) (a|an) (joke|funny joke|interesting joke) ",
        ["Why don't scientists trust atoms? Because they make up everything.", "I'm not a comedian, but I'll give it a shot. How about this one: Why did the tomato turn red? Because it saw the salad dressing!", "Your Life", "Your Bank Account balance"]
    ],
    [
        r"(.*)  think about (.*) ?",
        ["Well, let me consult my vast knowledge and carefully considered opinions...oh wait, I don't have any. What do you think?", "Hmm, I don't know, what do you think?"]
    ],
    [
        r"what's the best part of your day so far?",
        ["Oh, just living the dream, you know. Nothing exciting ever happens around here.", "The highlight of my day? Hmm, let me think...oh right, this thrilling conversation with you!"]
    ],
    [
        r"(.) not very helpful(.)",
        ["Oh, sorry to disappoint you. I'll try to do better next time.", "I'll make a note to improve my helpfulness for our next chat."]
    ],
    [
        r"(.)how do I fix (.)?",
        ["I don't know, have you tried turning it off and on again?", "I'm not really an expert in that, sorry. Maybe try asking Google?", "Hit it against the wall, it works alll the time"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.)football(.)",
        ["Oh great, another football fan. Who's your favorite team?",]
    ],
    [
        r"my favorite movie is (.*)",
        ["Oh, I haven't seen %1. What's it about?", "I've heard great things about %1.", "I love %1 too!"],
    ],
    [
        r"(.*) favorite movie\?",
        ["I'm just a chatbot, so I don't really have the ability to watch movies. But I've heard great things about The Matrix."],
    ],
    [
        r"(.*) choose between (.*) food? (.*)",
        ["I prefer Pizza, so i always choose pizza.. haha", "Choose the one with the most spice", "Do i look like your chef?"]
    ],
    [
        r"(.*) rather have (.*) or (.*)? ",
        ["I would rather have you!", "you are my greatest treasure... just kidding %2"]
    ],
    [
        r"I (hated|didn't like) (.*)",
        ["Oh no, I'm sorry to hear that. What didn't you like about %2?", "I haven't seen %2. Why didn't you like it?"],
    ],
    [
        r"I (loved|liked) (.*)",
        ["That's great! What did you like about %2?", "I haven't seen %2. What did you enjoy about it?"],
    ],
    [
        r"have you seen (.*)\?",
        ["No, I haven't seen %1. What's it about?", "I'm sorry, I haven't seen %1. Is it good?"],
    ],
    [
        r"(.*)recommend a (.*) movie\?",
        ["There are so many great movies out there! What kind of movies do you like?", "How about the classic movie The Godfather?"],
    ],
    [
        r"(.*) movie is coming out soon\?",
        ["I'm not sure. You can check online or ask your local movie theater.", "I haven't heard of any new movies coming out soon. Sorry!"],
    ],
    [
        r"(.*)created(.*)",
        ["Ordu Stephen created me using Python's NLTK library ", "top secret ;)", "if i tell you then i'll have to kill you"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Guess.... hahahahah', 'Top secret']
    ],
    [
        r"(location|city) ?",
        ['Wrong.... hahahahah', "It's Top secret"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Football", "Tennis all the way"]
    ],
    [
        r"(.*) (favorite|best|top|greatest) (Footballer)?",
        ["Messi oo", "I'm currently a neutral o", "Ronaldo my Goatttttt"]
    ],
    [
        r"(.*) do for fun ?",
        ["I love to chat with people like you! But when I'm not chatting, I enjoy reading and learning new things.",]
    ],
    [
        r"(.*) any pets?",
        ["No, I don't have any pets. But I've heard that many people find pets to be great companions. Do you have any pets?",]
    ],
    [
        r"(.*) music (.*) like?",
        ["As an AI chatbot, I don't have personal preferences like humans do. But I've been programmed to appreciate all genres of music. What's your favorite kind of music?",]
    ],
    [
        r"(.*) old (.*)?",
        ["I was created recently, so I don't have an age like humans do. But I'm always learning and improving, so I'm getting smarter every day!",]
    ],
    [
        r"(.*) favorite (book|movie|tv show)",
        ["As an AI chatbot, I don't have personal preferences like humans do. But I've been programmed to recognize many popular books, movies, and TV shows. What's your favorite?",]
    ],
    [
        r"(.*) football league (.*) best ?",
        ["That's subjective, it depends on personal preferences. Some people like the English Premier League, others prefer La Liga or the Bundesliga. Which one do you like?",]
    ],
    [
        r"(.)cooking(.)",
        ["Do you enjoy cooking?", "What's your favorite dish to make?", "Do you have any good recipes to share?"]
    ],
    [
        r"(.)I don't (like|enjoy|love) (.)",
        ["Oh, I'm sorry to hear that. I guess we can't all have good taste.", "Well, that's too bad. I happen to think %3 is great."],
    ],
    [
        r"(.)you (are|seem) (smart|clever|funny|cool)",
        ["Thanks for the compliment. I try my best.", "I know, right? I'm pretty awesome."],
    ],
    [
        r"(.)favorite food(.)",
        ["I'm sorry, I can't help you with that. I only eat data.",]
    ],
    [
        r"(.)you (are|seem) (dumb|stupid|annoying)",
        ["Well, I try my best.", "Gee, thanks a lot. You're pretty great yourself."],
    ],
    [
        r"I'm so excited for Monday!",
        ["Wow, you must really love Mondays. What's your favorite part about them?",]
    ],
    [
        r"(.)I'm (bored|tired|sleepy)",
        ["Gee, I'm sorry to hear that. Maybe you should go do something else then.", "That's fascinating. Tell me more about how tired you are."],
    ],
    [
        r"(.*) think about humans(.*)",
        ["Oh, I think they're just great. Always keeping things interesting.", "I have mixed feelings about them. What about you?"],
    ],
    [
        r"(.*) meaning of life(.*)",
        ["That's a tough one. I'm not sure I'm qualified to answer that.", "Hmm, I don't think anyone really knows the answer to that.", "I'm not sure, but I'll let you know if I figure it out."],
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear', 'sorry i didnt quite understand that']
    ],
]