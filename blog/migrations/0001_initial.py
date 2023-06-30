# Generated by Django 4.2.2 on 2023-06-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Nom de l'article"),
                ),
                ("desc", models.TextField()),
                ("image", models.ImageField(upload_to="articles")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
