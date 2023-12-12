# Generated by Django 5.0 on 2023-12-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myuser",
            name="created_date",
        ),
        migrations.RemoveField(
            model_name="myuser",
            name="updated_date",
        ),
        migrations.RemoveField(
            model_name="myuser",
            name="user_id",
        ),
        migrations.RemoveField(
            model_name="myuser",
            name="username",
        ),
        migrations.AddField(
            model_name="myuser",
            name="id",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name="myuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="myuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="myuser",
            name="email",
            field=models.EmailField(
                max_length=255, unique=True, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="myuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
