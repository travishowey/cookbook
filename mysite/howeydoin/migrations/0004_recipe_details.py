# Generated by Django 2.2 on 2022-04-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howeydoin', '0003_auto_20220420_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='details',
            field=models.CharField(default="it's a good recipe, really", max_length=2000),
        ),
    ]