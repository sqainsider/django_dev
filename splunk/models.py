from django.db import models
from django.utils import timezone


class Document(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class TestSuite(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class TestCase(models.Model):
    Name = models.CharField(max_length=30)
    TestSuite = models.ForeignKey(
        TestSuite, on_delete=models.CASCADE,)
    Expected_result = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    item = models.CharField(max_length=255)


class Environment(models.Model):
    Name = models.CharField(max_length=10)
    url = models.CharField(max_length=100)


class DV_Result_Log(models.Model):

    document = models.CharField(max_length=30)
    docuemnt_id = models.CharField(max_length=30)
    log_type = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    line_nbr = models.IntegerField()
    item = models.CharField(max_length=100)
    actual_result = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255)
    verify = models.CharField(max_length=255)
    comment = models.TextField()
    testsuite = models.CharField(max_length=30)
    testcase = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)
    environment = models.CharField(max_length=10)
    status_overide = models.BooleanField()
    final_status = models.CharField(max_length=10)
    additional_comment = models.TextField()
    jira = models.CharField(max_length=10)
    user_story = models.CharField(max_length=255)
    accpetance_criteria = models.CharField(max_length=100)
