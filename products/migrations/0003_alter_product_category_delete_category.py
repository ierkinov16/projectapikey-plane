# Generated by Django 4.2 on 2023-05-02 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('products', '0002_category_product_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
