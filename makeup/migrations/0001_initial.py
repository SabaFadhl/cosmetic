# Generated by Django 4.0.1 on 2022-01-26 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Orgin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Kind', models.CharField(max_length=50)),
                ('Descreption', models.CharField(max_length=50)),
                ('Expir_date', models.DateField()),
                ('Price', models.IntegerField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='makeup.brand')),
            ],
        ),
    ]
