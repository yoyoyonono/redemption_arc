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
    $ rightanswers = 0
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

    show ss angry

    # These display lines of dialogue.

    ss "[mcname], you have been failing at Japanese, this can't go on."

    ss "I can't teach you well enough so I have found you a tutor."
 
    show ss angry at offscreenright with moveoutright

    with Pause(2.0) 

    show ss happy at offscreenright
    show tu happy at offscreenleft
    with None
    
    show ss happy at midright
    show tu happy at midleft
    with ease

    ss "[mcname], this is [tutorname]."
    
    tu "Nice to meet you [mcname]. Let's begin your training."

    show ss happy at offscreenright
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
    

    # This ends the game.

    return
