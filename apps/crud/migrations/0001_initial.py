from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('codigo_item', models.AutoField(primary_key=True, serialize=False)),
                ('nome_item', models.CharField(default='', max_length=100)),
                ('tipo_item', models.CharField(default='', max_length=100)),
                ('peso', models.CharField(default='', max_length=30)),
                ('raridade', models.CharField(default='', max_length=50)),
                ('descricao_item', models.TextField(blank=True, default='')),
                ('nome_encontrador', models.CharField(default='', max_length=100)),
                ('graduacao', models.CharField(default='', max_length=50)),
                ('local_encontrado', models.CharField(default='', max_length=150)),
                ('data_encontrado', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
