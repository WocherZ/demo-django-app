# Generated by Django 4.1.7 on 2023-03-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitor',
            options={'permissions': [], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Список пользователей'},
        ),
        migrations.AddField(
            model_name='visitor',
            name='login',
            field=models.CharField(default='adminlogin', max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='name',
            field=models.CharField(default='adminname', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='group',
            field=models.CharField(choices=[('ADMIN', 'admin'), ('OPERATOR', 'operator'), ('VISITOR', 'visitor')], max_length=32, verbose_name='Группа пользователя'),
        ),
    ]
