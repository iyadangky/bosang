# Generated by Django 3.2.6 on 2022-07-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]