# Generated by Django 2.0 on 2017-12-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truecallerdata',
            name='area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='truecallerdata',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='truecallerdata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='truecallerdata',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='truecallerdata',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='truecallerdata',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
