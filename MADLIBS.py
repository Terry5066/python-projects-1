# #string concatenation/ how to put string together
# #suppose we want to create a string that says"subscribe to_____"
# youtuber=""#some string variable

# a few ways to do this
# print("subscribe to "+youtuber)
# print("subscribe to{}".format(youtuber))
# print(f"subscribe to {youtuber}")

celeb=input("famous person:")
adj=input("adjectives:")
verb1=input("verb:")
verb2=input("verb:")

madlib=f"computer programming is so {adj}! It makes me so excited all\
the time because i love to {verb1}.Stay hydrated and\
{verb2}like you are {celeb}!"
print(madlib)
