# Generated by Django 3.1.5 on 2024-03-14 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0016_merge_20240314_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PRESENT', 'PRESENT')], default='PRESENT', max_length=50),
        ),
    ]