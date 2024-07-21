from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    table_count = models.IntegerField()
    confirmation_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    checked_in = models.BooleanField(default=False)

    class Meta:
        unique_together = ('event', 'vendor')

    def __str__(self):
        return f"{self.vendor.name} attending {self.event.name}"
