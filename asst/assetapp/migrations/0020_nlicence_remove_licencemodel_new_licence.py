# Generated by Django 4.0.2 on 2022-08-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0019_licencemodel_new_licence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nlicence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_licence', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Nlicence',
            },
        ),
        migrations.RemoveField(
            model_name='licencemodel',
            name='new_licence',
        ),
    ]
