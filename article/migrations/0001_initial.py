# Generated by Django 4.0.3 on 2022-03-18 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hardware", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date de création"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date de modification"
                    ),
                ),
                ("quantity", models.PositiveSmallIntegerField(verbose_name="Quantité")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Prix"
                    ),
                ),
                (
                    "hardware",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hardware.hardware",
                        verbose_name="Matériel",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
