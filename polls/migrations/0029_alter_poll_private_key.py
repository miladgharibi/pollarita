# Generated by Django 4.0.1 on 2022-01-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_alter_poll_option_3_alter_poll_option_4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='private_key',
            field=models.CharField(default='cXE2LHj]wzUJWbG0', editable=False, max_length=16, null=True),
        ),
    ]