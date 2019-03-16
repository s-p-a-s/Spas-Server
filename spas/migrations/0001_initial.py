# Generated by Django 2.1.7 on 2019-03-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lights', models.IntegerField(max_length=200)),
                ('timeOut', models.IntegerField(default=0)),
                ('timeIn', models.IntegerField(default=0)),
            ],
        ),

    ]
