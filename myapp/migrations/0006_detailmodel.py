# Generated by Django 4.1 on 2022-09-06 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_ordermoder_ordermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('unitprice', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('dtotal', models.IntegerField()),
                ('dorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ordermodel')),
            ],
        ),
    ]