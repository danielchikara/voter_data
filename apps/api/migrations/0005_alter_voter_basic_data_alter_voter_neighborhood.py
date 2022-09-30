# Generated by Django 4.1.1 on 2022-09-30 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_leader_basic_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='basic_data',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basic_data_voter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='voter',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhood_voters', to='api.neighborhood'),
        ),
    ]