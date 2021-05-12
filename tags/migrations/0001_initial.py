# Generated by Django 3.2 on 2021-05-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0003_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(to='posts.Post', verbose_name='tags')),
            ],
        ),
    ]
