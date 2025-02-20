# Generated by Django 4.1.7 on 2023-04-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_alter_houseplants_feeding_alter_houseplants_homeland_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseplants',
            name='feeding',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='flowering_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='homeland',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='humidity',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='irrigation_level',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='leaf_color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='level_of_care',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='light_level',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='soil',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='houseplants',
            name='temperature',
            field=models.CharField(max_length=200),
        ),
    ]
