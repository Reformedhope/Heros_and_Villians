# Generated by Django 4.1.7 on 2023-02-23 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0002_supers_super_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supers',
            name='super_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
            preserve_default=False,
        ),
    ]
