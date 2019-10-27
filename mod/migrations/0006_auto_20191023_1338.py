# Generated by Django 2.2.5 on 2019-10-23 13:38

from django.db import migrations, models
import mod.validator


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0005_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.CharField(default='zain@gmail.com', max_length=40, validators=[mod.validator.valid_email]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(default='Zain', max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(default='Yaseen', max_length=30),
        ),
    ]