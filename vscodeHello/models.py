from django.db import models
from django.utils import timezone


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Contact(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    timestamp_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.firstName}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Test_Result_Log(models.Model):
    documentType = models.CharField(max_length=50)
    documnetId = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    linetype = models.CharField(max_length=10)
    lineNbr = models.CharField(max_length=10)
    sku = models.CharField(max_length=20)
    actualResult = models.CharField(max_length=255)
    expectedResult = models.CharField(max_length=255)
    verify = models.CharField(max_length=100)
    runId = models.CharField(max_length=20)
    testSuite = models.CharField(max_length=50)
    testCase = models.CharField(max_length=50)
    tester = models.CharField(max_length=50)
    environment = models.CharField(max_length=10)
    additionalComment = models.CharField(max_length=100)
    userStory = models.CharField(max_length=100)
    accpetanceCriteria = models.CharField(max_length=100)
    jira = models.CharField(max_length=10, null=True)
    timestamp = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.firstName}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_nmae


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
