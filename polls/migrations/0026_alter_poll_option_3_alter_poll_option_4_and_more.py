# Generated by Django 4.0.1 on 2022-01-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_alter_poll_option_3_alter_poll_option_4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='option_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='private_key',
            field=models.CharField(default='Zw(}mh@)BJjxfK\\n', editable=False, max_length=16, null=True),
        ),
    ]