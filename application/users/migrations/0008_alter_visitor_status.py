# Generated by Django 3.2 on 2023-03-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20230330_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='status',
            field=models.CharField(choices=[('Оплачено', 'оплачено'), ('Неоплачено', 'неоплачено')], default='Оплачено', max_length=32),
        ),
    ]
