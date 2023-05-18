# Generated by Django 3.2.18 on 2023-05-18 05:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
