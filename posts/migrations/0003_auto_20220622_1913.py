# Generated by Django 3.2.6 on 2022-06-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220622_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='airbag',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='birth',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='carModel',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='carNumber',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='client',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='driveType',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='eventDate',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='fuel',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(default='', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(default='', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(default='', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(default='', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image5',
            field=models.ImageField(default='', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image6',
            field=models.ImageField(default='', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='insuranceCompany',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='mileage',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='note',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='others1',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='others2',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='others3',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='phoneNumber',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='proposedCompensation',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='repairCost',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='trim',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
