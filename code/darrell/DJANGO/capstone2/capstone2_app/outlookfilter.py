from .outlookexport import outlook_export
import re


def outlook_filter():
    messages = outlook_export()
    filtered_email = []
    print(len(filtered_email))

    for x in messages:
       
        
        subject = x['Subject']
        email_body = x['Body']

        regex = r"(#([0-9]{6,7})+(-G[A-Z])*)"

        if re.search(regex, subject):
            filtered_email.append(x)
        elif re.search(regex, email_body):
          filtered_email.append(x)

    print(len(messages))
    print(len(filtered_email))
    return filtered_email
    

    
    
    
# print(outlook_filter())





    