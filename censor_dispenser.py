# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_choice(text, censor_phrase):
    text_censored = text.replace(censor_phrase, "⬛" * len(censor_phrase))
    return text_censored

#print(censor_choice(email_one, "learning algorithms"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censor_list(text, lst):
    for word in lst:
        text = text.replace(word, "⬛" * len(word))
    return(text)

#print(censor_list(email_two, proprietary_terms))