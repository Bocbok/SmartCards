# Generated by Django 2.1.4 on 2018-12-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinche', '0002_auto_20181217_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listcards',
            old_name='value',
            new_name='value_atout',
        ),
        migrations.AddField(
            model_name='listcards',
            name='value_non_atout',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]