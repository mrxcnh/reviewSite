# Generated by Django 3.2.8 on 2021-10-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0002_alter_epic_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='epic',
            name='global_url',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
