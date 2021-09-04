# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]")
define ss = Character("Sensei")
define tu = Character("[tutorname]")

# The game starts here.

transform midright:
    xalign 0.75

transform midleft:
    xalign 0.25

label start:
    $ totalrightanswers = 0
    $ thistestrightanswers = 0
    $ tutorname = "pocky sensei"
    $ mcname = renpy.input("What is your name?").strip()
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "Hi, I'm [mcname], and I'm a Junior student at Thomas Jefferson High School."

    "The school year has just begun and I've already failed all three assignments in japanese."

    scene bg classroom 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ss

    # These display lines of dialogue.

    ss "[mcname], you have been failing at Japanese, this can't go on."

    ss "I can't teach you well enough so I have found you a tutor."
 
    show ss at offscreenright with moveoutright

    with Pause(1.0) 

    show ss at offscreenright
    show tu happy at offscreenleft
    with None
    
    show ss at midright
    show tu happy at midleft
    with ease

    ss "[mcname], this is [tutorname]."
    
    tu "Nice to meet you [mcname]. Let's begin your training."

    show ss at offscreenright
    show tu happy at center
    with ease

    menu intro_response:
        "Nice to meet you too, let's start!":
            mc "Nice to meet you too, let's start!"
        "Alright!":
            mc "Alright!"
        "よろしくおねがいします":
            mc "よろしくおねがいします"
        "UwU":
            mc "UwU"
            show tu angry
            tu "no"


    scene bg classroom 2 with dissolve
    show tu happy at center

    menu test_1_question_1:
        "What verb would best complete this sentence?　すしを"
        "ねます":
            mc "ねます"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        "つくります":
            mc "つくります"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        "食べます（たべます）":
            mc "食べます"
            tu "Yes! That's correct, good job!"
            $ thistestrightanswers += 1
        "飲みます（のみます）":
            mc "飲みます"
            tu "Sorry that’s wrong, the correct answer was 食べます"
        
    menu test_1_question_2:
        "Which hiragana matches the kanji：「新しい」　くるまですれ。"
        "あたらしい":
            mc "あたらしい"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あだらしい":
            mc "あだらしい"
            tu "Sorry that’s wrong, the right answer was あたらしい"
        "あらたしい":
            mc "あらたしい" 
            tu "Sorry that’s wrong, the right answer was あたらしい"
        "あらだしい":
            mc "あらだしい" 
            tu "Sorry that’s wrong, the right answer was あたらしい"

    menu test_1_question_3:
        "What is the reading of this kanji in the sentence: あしたは「雨」ですか。"
        "ゆき":
            mc "ゆき"
            tu "Sorry that’s wrong, the right answer was あめ"
        "はれ":
            mc "はれ"
            tu "Sorry that’s wrong, the right answer was あめ"
        "くもり":
            mc "くもり"
            tu "Sorry that’s wrong, the right answer was あめ"
        "あめ":
            mc "あめ"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1

    menu test_1_question_4:
        "Which kanji represents the hiragana：「そと」で　まちましょう。"
        "外":
            mc "外"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "言":
            mc "言"
            tu "Sorry that’s wrong, the right answer was 外"
        "中":
            mc "中"
            tu "Sorry that’s wrong, the right answer was 外"
        "頃":
            mc "頃"
            tu "Sorry that’s wrong, the right answer was 外"
    
    menu test_1_question_5:
        "Which hiragana matches the kanji：しゃしんは　はこ　の「中」に　あります。"
        "そば":
            mc "そば"
            tu "Sorry that’s wrong, the right answer was なか"
        "そと":
            mc "そと"
            tu "Sorry that’s wrong, the right answer was なか"
        "なか":
            mc "なか"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "よこ":
            mc "よこ"
            tu "Sorry that’s wrong, the right answer was なか"

    menu test_1_question_6:
        "Figure out the correct sentence ending：しつもんが"
        "あります。":
            mc "あります。"
            tu "Perfect! Keep it up!"
            $ thistestrightanswers += 1
        "います。":
            mc "います。"
            tu "Sorry that’s wrong, the right answer was あります。"


    menu test_1_question_7:
        "Figure out which hiragana best suits the sentence：ここは　（＿＿＿＿）です。　べんきょできません。"
        "くらい":
            mc "くらい"
            tu "Sorry that’s wrong, the right answer was うるさい"
        "さむい":
            mc "さむい"
            tu "Sorry that’s wrong, the right answer was うるさい"
        "うるさい":
            mc "うるさい"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あぶない":
            mc "あぶない"
            tu "Sorry that’s wrong, the right answer was うるさい"

    menu test_1_question_8:
        "Which particle should fill in the blank? これ「＿＿」えんぴつです。"
        "に":
            mc "に"
            tu "Sorry, that's wrong, the right answer was は"
        "を":
            mc "を"
            tu "Sorry, that's wrong, the right answer was は"
        "は":
            mc "は"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "や":
            mc "や"
            tu "Sorry, that's wrong, the right answer was は"

    menu test_1_question_9:
        "Figure out which hiragana best suits the sentence：あそこで　タクシーに「＿＿＿＿＿」。"
        "のりました":
            mc "のりました"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "あがりました":
            mc "あがりました"
            tu "Sorry that’s wrong, the right answer was のりました"
        "つきました":
            mc "つきました"
            tu "Sorry that’s wrong, the right answer was のりました"
        "はいりました":
            mc "はいりました"
            tu "Sorry that’s wrong, the right answer was のりました"

    menu test_1_question_10:
        "Which particle should fill in the blank? 弟　（おとうと）は　へや　「＿」そうじを　しました。"
        "が":
            mc "が"
            tu "Sorry, that's wrong, the right answer was に"
        "を":
            mc "を"
            tu "Sorry, that's wrong, the right answer was に"
        "に":
            mc "に"
            tu "Yes! Great job!"
            $ thistestrightanswers += 1
        "の":
            mc "の"
            tu "Sorry, that's wrong, the right answer was に"

    $ totalrightanswers += thistestrightanswers

    if thistestrightanswers >= 7:
        tu "Good job! It seems like you've learned a lot." 
        tu "I'll see you tomorrow!"
    else:
        tu "You failed..."
        tu "Unfortunately the session is over so you'll have to try again tomorrow."

    scene bg bedroom e evening
    "I enjoyed that, let's see if I can improve some more..."

    scene bg bedroom e night
    with fade
    "Wow, I spent so much time studying, I guess I should go to sleep."



    # This ends the game.

    return
