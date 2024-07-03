for g in range(200):
    import time
    import random

    # Define the probabilities for each game
    probabilities = [
        [39, 28, 33],
        [33, 30, 37],
        [38, 29, 33],
        [34, 30, 36],
        [37, 25, 38],
        [42, 25, 33],
        [42, 29, 29],
        [37, 29, 34],
    ]

    # Generate 1000 random combinations
    combinations = []
    for _ in range(1000):
        combination = [random.choices([1, 2, 3], weights=probabilities[i])[0] for i in range(8)]
        combinations.append(''.join(map(str, combination)))

    # Write the combinations to a file
    with open('destiny.txt', 'w') as f:
        for combination in combinations:
            f.write(combination + '\n')
    for p in range(1):
        import os

        # folder_name = "chiko"
        # filako = os.path.join(folder_name, f"kenken{p}.txt")
        filako = (f"destiny.txt")
        from itertools import product
        import time

        # Read student attempts from the file
        with open(filako, 'r') as file:
            student_attempts = [line.strip() for line in file]


        # Function to count how many students scored exactly 1 out of 8
        def count_students_scored_one(combination, student_attempts):
            count = 0
            for attempt in student_attempts:
                score = sum(a == b for a, b in zip(combination, attempt))
                if score == 5:  # Check if exactly one answer is correct
                    count += 1
            return count


        # Generate all possible answer combinations
        possible_answers = [''.join(combination) for combination in product('123', repeat=8)]

        # You might want to adjust the criteria based on the actual requirements or data
        # Filter out combinations based on the number of students scoring exactly 1/8
        valid_combinations = [comb for comb in possible_answers if
                              102 < count_students_scored_one(comb, student_attempts) < 104]

        # Open the file in append mode
        with open('allofthem.txt', 'a') as file:
            for comb in valid_combinations:
                file.write(f"{comb}\n")  # Write each combination followed by a newline



    print(g)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
from_email = 'gauvinisa10@gmail.com'
password = 'wslp zqug qmwy sefo'
to_email = 'gauvinisa10@gmail.com'

# Email subject and body
subject = 'Subject of the Email'
body = 'Body of the email'

# Create the email
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# Open the file to be sent
filename = 'allofthem.txt'
attachment = open('allofthem.txt', 'rb')

# Instance of MIMEBase and named as p
part = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
part.set_payload((attachment).read())

# Encode into base64
encoders.encode_base64(part)

part.add_header('Content-Disposition', f"attachment; filename= {filename}")

# Attach the instance 'part' to instance 'msg'
msg.attach(part)

# Create SMTP session for sending the mail
server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
server.starttls()

# Login to the email account
server.login(from_email, password)

# Convert the Multipart msg into a string
text = msg.as_string()

# Send the email
server.sendmail(from_email, to_email, text)
# Terminate the session
server.quit()
print("Email sent successfully")
