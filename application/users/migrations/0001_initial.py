# Generated by Django 4.1.7 on 2023-03-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('group', models.CharField(choices=[('ADMIN', 'admin'), ('OPERATOR', 'operator'), ('VISITOR', 'visitor')], max_length=32)),
            ],
            options={
                'permissions': [],
            },
        ),
    ]
