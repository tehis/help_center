# Generated by Django 4.0.6 on 2022-07-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_help', '0002_useraddress_created_at_useraddress_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='creator_type',
            field=models.CharField(choices=[('USR', 'User'), ('SUP', 'Supporter')], default='USR', max_length=3),
        ),
    ]