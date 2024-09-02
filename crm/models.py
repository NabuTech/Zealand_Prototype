from django.db import models

class Lead(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Additional Details
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)  # Job title or position of the lead
    source = models.CharField(
        max_length=100,
        choices=[
            ('website', 'Website'),
            ('email', 'Email'),
            ('event', 'Event'),
            ('referral', 'Referral'),
            ('social_media', 'Social Media'),
        ],
        default='website'
    )  # Source of the lead

    # Status and Activity Tracking
    status = models.CharField(
        max_length=50,
        choices=[
            ('new', 'New'),
            ('contacted', 'Contacted'),
            ('qualified', 'Qualified'),
            ('unqualified', 'Unqualified'),
        ],
        default='new'
    )  # Status in the sales funnel
    last_contacted = models.DateTimeField(blank=True, null=True)  # Date of last contact
    notes = models.TextField(blank=True, null=True)  # Additional notes about the lead

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)  # Date the lead was created
    updated_at = models.DateTimeField(auto_now=True)  # Date the lead was last updated

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_name if self.company_name else 'Individual'}"
