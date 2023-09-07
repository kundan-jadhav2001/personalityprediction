# Generated by Django 4.2.2 on 2023-09-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personality',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.IntegerField()),
                ('age', models.IntegerField()),
                ('openness', models.IntegerField()),
                ('neuroticism', models.IntegerField()),
                ('conscientiousness', models.IntegerField()),
                ('agreeableness', models.IntegerField()),
                ('extraversion', models.IntegerField()),
                ('result', models.CharField(max_length=20)),
            ],
        ),
    ]
