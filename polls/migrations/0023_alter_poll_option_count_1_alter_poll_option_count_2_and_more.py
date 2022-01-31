# Generated by Django 4.0.1 on 2022-01-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_alter_poll_private_key_delete_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='option_count_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_count_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_count_3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_count_4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='private_key',
            field=models.CharField(default='p]gDyc^{6(r?wo4B', editable=False, max_length=16, null=True),
        ),
    ]
