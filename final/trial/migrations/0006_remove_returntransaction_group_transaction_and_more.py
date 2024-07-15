# Generated by Django 5.0.1 on 2024-05-10 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0005_returntransaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returntransaction',
            name='group_transaction',
        ),
        migrations.AddField(
            model_name='returntransaction',
            name='group_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trial.groupaccount'),
        ),
    ]
