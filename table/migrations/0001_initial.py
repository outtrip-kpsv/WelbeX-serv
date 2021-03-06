# Generated by Django 4.0.2 on 2022-02-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableRows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Расстояние')),
            ],
        ),
    ]
