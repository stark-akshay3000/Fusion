# Generated by Django 3.1.5 on 2024-02-15 17:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
        ('hostel_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelAllottment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignedBatch', models.CharField(max_length=50)),
                ('assignedCaretaker', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='globals.staff')),
                ('assignedWarden', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='globals.faculty')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
    ]