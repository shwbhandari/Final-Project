# Generated by Django 3.1.3 on 2021-02-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_women_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='accussedNum',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='women',
            name='maritalStatus',
            field=models.CharField(default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='women',
            name='crimeName',
            field=models.CharField(max_length=200),
        ),
    ]
