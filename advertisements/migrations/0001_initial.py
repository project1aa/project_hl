# Generated by Django 2.1 on 2018-09-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('code', models.TextField()),
                ('image', models.ImageField(upload_to='images/advertisements')),
                ('position', models.CharField(choices=[('a', 'A'), ('b1', 'B1'), ('b2', 'B2'), ('c', 'C'), ('d1', 'D1'), ('d2', 'D2'), ('e', 'E')], max_length=2)),
            ],
        ),
    ]
