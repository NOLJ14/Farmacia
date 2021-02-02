# Generated by Django 3.1.3 on 2021-01-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nit', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidoPaterno', models.CharField(max_length=30)),
                ('apellidoMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.IntegerField(primary_key=True, serialize=False)),
                ('idUsuario', models.IntegerField()),
                ('ci', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellidoPaterno', models.CharField(max_length=30)),
                ('apellidoMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaFarmaceutica',
            fields=[
                ('idEmpresaFarmaceutica', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('idOrdenDeCompra', models.IntegerField(primary_key=True, serialize=False)),
                ('nit', models.IntegerField()),
                ('idProducto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('idPresentacion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('idEmpresaFarmaceutica', models.IntegerField()),
                ('idPresentacion', models.IntegerField()),
                ('Estante', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto_has_Proveedor',
            fields=[
                ('idProducto_has_Proveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('idProducto', models.IntegerField()),
                ('idProveedor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
                ('tipoDeUsuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=55)),
            ],
        ),
    ]
