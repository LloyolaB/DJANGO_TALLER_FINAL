# Generated by Django 4.1.4 on 2022-12-18 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Institucion",
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
                    "institucion",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="nombre de la institucion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inscrito",
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
                ("nombre", models.CharField(max_length=50)),
                ("telefono", models.CharField(max_length=50)),
                ("fecha_inscripcion", models.DateField(auto_now_add=True)),
                ("fecha_reservada", models.DateField()),
                ("hora", models.TimeField()),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Reservado", "Reservado"),
                            ("Completada", "Completada"),
                            ("Anulada", "Anulada"),
                            ("No Asisten", "No Asisten"),
                        ],
                        default="Reservado",
                        max_length=50,
                    ),
                ),
                ("observaciones", models.TextField(blank=True, null=True)),
                (
                    "institucion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inscripcion.institucion",
                    ),
                ),
            ],
        ),
    ]
