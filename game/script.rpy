# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]")
define ss = Character("Sensei")
define tu = Character("[tutorname]")

# The game starts here.

label start:
    $ rightanswers = 0
    $ tutorname = "tutor"
    $ mcname = renpy.input("What is your name?").strip()
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "Hi, I'm [mcname], and I'm a Junior student at Thomas Jefferson High School."

    "I've never been good at Japanese, and now bla bla bla bla."

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sensei angry

    # These display lines of dialogue.

    ss "[mcname], You are bad at japanese."

    ss "I have found you a tutor. somethign someone else sombedaodsflkj."
 
    show tutor happy
    show sensei happy

    tu "Hi I'm [tutorname]"
    # This ends the game.

    return
