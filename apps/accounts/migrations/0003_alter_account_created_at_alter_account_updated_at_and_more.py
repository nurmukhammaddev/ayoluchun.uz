# Generated by Django 4.1.7 on 2023-03-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='account',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='purchased_course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='purchased_course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='region',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='region',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti'),
        ),
    ]
