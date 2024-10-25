import random
from send_text import send_bulk_emails

def random_pairs(options):
    flattened_options = [name for sublist in options for name in sublist]
    pairs = []

    while len(flattened_options) >= 2:
        name1 = random.choice(flattened_options)
        name2 = random.choice(flattened_options)

        # Ensure they're not from the same sublist
        if any(name1 in sublist and name2 in sublist for sublist in options):
            continue
        
        pairs.append((name1, name2))
        flattened_options.remove(name1)
        flattened_options.remove(name2)

        # Remove the paired names from the original options list
        for sublist in options:
            if name1 in sublist:
                sublist.remove(name1)
            if name2 in sublist:
                sublist.remove(name2)

    return pairs

Laras = [('Josh', '7135779932', '@tmomail.net'), ("Hannah", '7135779932', '@tmomail.net')]
Cornelius = [('Chris', '7135779932', '@tmomail.net'), ('Raquel', '7135779932', '@tmomail.net')]
Tharpes = [('Aaron', '7135779932', '@tmomail.net'), ('Rachel', '7135779932', '@tmomail.net')]
Strobels = [('Tina', '7135779932', '@tmomail.net'), ('Jared', '7135779932', '@tmomail.net')]
options = [Laras, Cornelius, Tharpes, Strobels]

pairs = random_pairs(options)
for pair in pairs:
    nameA = pair[0][0] 
    nameB = pair[1][0]
    numberA = pair[0][1]+pair[0][2]
    numberB = pair[1][1]+pair[1][2]

    range = 2
    while range>0:

        subject = f"{nameA} Secrent Santa for 2024"

        message = f"""
                Hi {nameA}, 
                \n 
                Merry Christmas! 
                You're secret Santa to {nameB} :)
                
                """
        print(f"Paired: {nameA} and {numberA}")

        nameA, nameB = nameB, nameA
        numberA, numberB = numberB, numberA
        range -= 1

        print(message)

        try:
            send_bulk_emails(numberA, subject, message)
        except:
            print('Unable to send email')

