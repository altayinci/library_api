# Generated by Django 4.0.4 on 2022-04-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(blank=True, max_length=255, null=True)),
                ('book_author', models.CharField(blank=True, max_length=255, null=True)),
                ('last_udpated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
