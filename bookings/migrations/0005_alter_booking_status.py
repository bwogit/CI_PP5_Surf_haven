# Generated by Django 3.2.21 on 2023-10-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Booking Confirmed', 'Booking Confirmed'), ('Booking Rejected', 'Booking Rejected'), ('Awaiting Confirmation', 'Awaiting Confirmation'), ('Booking Expired', 'Booking Expired')], default='Awaiting Confirmation', max_length=25),
        ),
    ]
