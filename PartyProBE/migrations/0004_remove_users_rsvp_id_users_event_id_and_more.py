# Generated by Django 4.2.5 on 2023-10-20 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PartyProBE', '0003_alter_fooditem_catering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='rsvp_id',
        ),
        migrations.AddField(
            model_name='users',
            name='event_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='PartyProBE.event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rsvp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PartyProBE.guestrsvp'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PartyProBE.users'),
        ),
    ]
