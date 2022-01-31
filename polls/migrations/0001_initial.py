# Generated by Django 4.0.1 on 2022-01-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('status', models.IntegerField(choices=[('0', 'Private (with a uuid to access)'), ('1', 'Public (everyone can access)')], default='1')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]