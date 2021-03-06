# Generated by Django 3.1.4 on 2020-12-09 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracing', '0002_auto_20201210_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstablishmentProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishment_name', models.CharField(max_length=256, verbose_name='Establishment Name')),
                ('street', models.CharField(max_length=256, verbose_name='Street')),
                ('town', models.CharField(max_length=256, verbose_name='Barangay/Town')),
                ('city', models.CharField(max_length=256, verbose_name='City/Municipality')),
                ('region', models.CharField(max_length=256, verbose_name='State/Province')),
                ('mobile1', models.CharField(max_length=11, verbose_name='Primary Mobile No.')),
                ('mobile1_confirmed', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('mobile2', models.CharField(blank=True, max_length=11, null=True, verbose_name='Alternative Mobile No.')),
                ('mobile2_confirmed', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('landline', models.CharField(max_length=11, verbose_name='Landline No.')),
                ('landline_confirmed', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Time Created')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='Time Updated')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Email Address')),
            ],
            options={
                'verbose_name': 'Establishment Profile',
                'verbose_name_plural': 'Establishment Profiles',
            },
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='mobile1_confirmed',
            field=models.BooleanField(default=False, verbose_name='Confirmed'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='mobile2_confirmed',
            field=models.BooleanField(default=False, verbose_name='Confirmed'),
        ),
        migrations.CreateModel(
            name='TracingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transact', models.CharField(choices=[('EN', 'Entry'), ('EX', 'Exit')], max_length=2, verbose_name='Transaction')),
                ('transact_time', models.DateTimeField(auto_now=True, verbose_name='Transaction Time')),
                ('establishment_profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tracing.establishmentprofilemodel', verbose_name='Establishment')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tracing.userprofilemodel', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'Trace',
                'verbose_name_plural': 'Traces',
            },
        ),
    ]
