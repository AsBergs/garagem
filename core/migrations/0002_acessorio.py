from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Acessorio", fields =[(
                "id", models.BIgAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"))

                (descricao = models.CharField(max_length=100))
            ]
        )
    ]