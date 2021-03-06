# Generated by Django 3.1.4 on 2020-12-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='current_city',
            field=models.CharField(max_length=256, verbose_name='City/Municipality'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='current_region',
            field=models.CharField(max_length=256, verbose_name=' State/Province'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='current_street',
            field=models.CharField(max_length=256, verbose_name='Street '),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='current_town',
            field=models.CharField(max_length=256, verbose_name='Barangay/Town'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='perm_city',
            field=models.CharField(max_length=256, verbose_name='City/Municipality'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='perm_region',
            field=models.CharField(max_length=256, verbose_name='State/Province'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='perm_street',
            field=models.CharField(max_length=256, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='perm_town',
            field=models.CharField(max_length=256, verbose_name='Barangay/Town'),
        ),
    ]
