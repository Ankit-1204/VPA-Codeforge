import smtplib
import csv
def mail(date_entity,time_entity,user_names_found,event_names_found):
    gmail_user = 'astha00803@gmail.com'
    gmail_password = 'pzda pnke duzc wdjl'
    user_emails=[]
    with open('users.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            username = row['username']
            email = row['email']

            # Check if the current username is in the list of user_names_found
            if username in user_names_found:
                user_emails.append(email)
    if len(user_names_found) == 1:
        participants= ""  # Return an empty string if the size is 1
    else:
        # Concatenate the usernames using "between" and commas
        participants = " between " + ", ".join(user_names_found[:-1]) + " and " + user_names_found[-1]
    sent_from = gmail_user
    to = user_emails
    subject = "Scheduled"+event_names_found[0]
    body = "On "+str(date_entity) +" "+str(time_entity)+" "+event_names_found[0]+" is scheduled"+participants

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)