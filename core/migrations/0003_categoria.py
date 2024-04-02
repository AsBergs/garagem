from django.db import migrations, models

class MIgration(migrations.MIgration):

    dependencies =[
        ("core", '0002_acessorio'),
    ]  

    operation = [
        migrations.CreateModel(name="Categoria", fields =[(
                "id", models.BIgAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"))

                (descricao = models.CharField(max_length=100))
            ]
    
        )
    ]
