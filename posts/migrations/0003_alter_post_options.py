# Generated by Django 3.2 on 2021-05-12 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
    ]
