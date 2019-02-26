# Generated by Django 2.1.7 on 2019-02-26 00:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DV_Result_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=30)),
                ('docuemnt_id', models.CharField(max_length=30)),
                ('log_type', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('line_nbr', models.IntegerField()),
                ('item', models.CharField(max_length=100)),
                ('actual_result', models.CharField(max_length=255)),
                ('expected_result', models.CharField(max_length=255)),
                ('verify', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('testsuite', models.CharField(max_length=30)),
                ('testcase', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('environment', models.CharField(max_length=10)),
                ('status_overide', models.BooleanField()),
                ('final_status', models.CharField(max_length=10)),
                ('additional_comment', models.TextField()),
                ('jira', models.CharField(max_length=10)),
                ('user_story', models.CharField(max_length=255)),
                ('accpetance_criteria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Expected_result', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='testcase',
            name='TestSuite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splunk.TestSuite'),
        ),
    ]