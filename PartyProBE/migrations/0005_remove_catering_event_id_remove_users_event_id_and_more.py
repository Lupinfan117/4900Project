# Generated by Django 4.2.5 on 2023-10-20 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PartyProBE', '0004_remove_users_rsvp_id_users_event_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catering',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='event_id',
        ),
        migrations.AddField(
            model_name='catering',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PartyProBE.users'),
        ),
        migrations.AddField(
            model_name='users',
            name='catering_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='PartyProBE.catering'),
        ),
    ]
