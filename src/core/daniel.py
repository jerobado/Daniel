"""
Daniel, personal email client of Jero Bado

What it can do?
    * create*, send, receive and save* emails
"""

from email.message import EmailMessage


def create_email(sender: str, recipient: str, subject: str, message, attachment=None) -> EmailMessage:
    """ Create a simple email. """

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(message)

    return msg


def save_email(email: EmailMessage, filename: str) -> None:
    """ Save an email to disk. """

    with open(filename, 'wb') as f:
        f.write(bytes(email))
