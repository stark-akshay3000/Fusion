# Generated by Django 3.1.5 on 2024-03-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0014_auto_20240312_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PRESENT', 'PRESENT')], default='PRESENT', max_length=50),
        ),
    ]
