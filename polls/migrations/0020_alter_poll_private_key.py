# Generated by Django 4.0.1 on 2022-01-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_alter_poll_private_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='private_key',
            field=models.CharField(default='u7T*cCS}92&MDoLG', editable=False, max_length=16, null=True),
        ),
    ]
