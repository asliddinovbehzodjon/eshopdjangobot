# Generated by Django 4.0.3 on 2022-03-21 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mahsulotlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mahsulotlar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.foydalanuvchi')),
            ],
        ),
    ]
