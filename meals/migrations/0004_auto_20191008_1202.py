# Generated by Django 2.2 on 2019-10-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20191008_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
    ]
