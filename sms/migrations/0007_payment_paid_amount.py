# Generated by Django 2.1.5 on 2019-02-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_payment_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid_amount',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]