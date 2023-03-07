import smtplib, random
import datetime as dt

Quotes_file_path = "C:\programming\Python\Projects\Smtp\Sunday Motivation\quotes.txt"

recipients = [
    
]

# Enter email & password
email = ""
password = ""

quotes = []
with open(Quotes_file_path, "r") as f:
    for line in f:
        quotes.append(line)

curr = dt.datetime.now()
today = curr.weekday()
print(today)

if today == 6:
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=recipients[0],
            msg=f"Subject:Today Motivation by tejas\n\n{quote}",
        )
        connection.sendmail(
            from_addr=email,
            to_addrs=recipients[1],
            msg=f"Subject:Today Motivation by tejas\n\n{quote}",
        )
        connection.sendmail(
            from_addr=email,
            to_addrs=recipients[2],
            msg=f"Subject:Today Motivation by tejas\n\n{quote}",
        )

"""
"""
