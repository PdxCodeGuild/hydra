from django.db import models


class Claim(models.Model):
    claim_number = models.CharField(max_length=30, null=True, blank=True)
    lit_dates = models.CharField(max_length=200, null=True, blank=True)
    claimant = models.CharField(max_length=100, null=True, blank=True)
    action_required = models.CharField(max_length=200, null=True, blank=True)
    in_suit = models.CharField(max_length=100, null=True, blank=True)
    dc_assigned = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    date_coverage_letter_sent = models.CharField(
        max_length=100, null=True, blank=True)
    # last_note_date = models.DateField(null=True, blank=True)
    days_since_last_note = models.CharField(
        max_length=100, null=True, blank=True)
    # follow_up_date = models.DateField(null=True, blank=True)
    insured_facility = models.CharField(max_length=200, null=True, blank=True)
    coverage_letter = models.CharField(max_length=200, null=True, blank=True)
    settlement_value = models.CharField(max_length=200, null=True, blank=True)
    insurer_policy = models.CharField(max_length=200, null=True, blank=True)
    bulk_insured = models.CharField(max_length=200, null=True, blank=True)
    claim_type = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.claim_number


class Email(models.Model):
    claimNum = models.CharField(max_length=100, null=True, blank=True)
    emailSubject = models.CharField(max_length=200, null=True, blank=True)
    emailFrom = models.CharField(max_length=200, null=True, blank=True)
    emailFromAddress = models.CharField(max_length=200, null=True, blank=True)
    emailTo = models.CharField(max_length=200, null=True, blank=True)
    emailBody = models.CharField(max_length=10000, null=True, blank=True)


    def __str__(self):
        return self.emailSubject
