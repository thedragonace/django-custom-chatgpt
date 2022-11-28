# Generated by Django 4.1.3 on 2022-11-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, default='')),
                ('summary', models.TextField(blank=True, default='')),
                ('questions', models.TextField(blank=True, default='')),
                ('corectness', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
