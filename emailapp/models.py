# emailapp/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAccount(models.Model):
    """Represents an individual or shared email account."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email_account', blank=True, null=True)
    email_address = models.EmailField(unique=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    users_with_access = models.ManyToManyField(User, related_name='accessible_email_accounts', blank=True)

    def __str__(self):
        return self.email_address


class EmailFolder(models.Model):
    """Represents folders for organizing emails (like Inbox, Sent, etc.)."""
    account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.account.email_address} - {self.name}"


class Email(models.Model):
    """Represents an individual email message."""
    account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE, related_name='emails')
    sender = models.ForeignKey(User, related_name='sent_emails', on_delete=models.CASCADE)
    recipient = models.ForeignKey(EmailAccount, related_name='received_emails', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(EmailFolder, on_delete=models.SET_NULL, null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Email from {self.sender.email} to {self.recipient.email_address} - {self.subject}"
