# Generated by Django 3.2.9 on 2021-11-23 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0059_auto_20211123_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firewallmodel',
            old_name='Model_no',
            new_name='Machine_Model_no',
        ),
        migrations.RenameField(
            model_name='firewallmodel',
            old_name='Machine_Si_no',
            new_name='Machine_Sl_no',
        ),
    ]
