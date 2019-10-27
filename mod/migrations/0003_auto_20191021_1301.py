# Generated by Django 2.2.5 on 2019-10-21 13:01

from django.db import migrations, models
import mod.validator


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0002_auto_20191010_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='zain', max_length=30)),
                ('last_name', models.CharField(default='zain', max_length=30)),
                ('email', models.CharField(default='zain@gmail.com', max_length=40, unique=True, validators=[mod.validator.valid_email])),
                ('note', models.TextField(default='Comming soon .....', max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public'), ('private', 'Private'), ('publish', 'Publish')], default='draft', max_length=120),
        ),
    ]