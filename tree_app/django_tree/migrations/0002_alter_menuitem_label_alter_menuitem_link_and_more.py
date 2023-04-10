# Generated by Django 4.1.4 on 2023-04-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_tree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='label',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='link',
            field=models.CharField(max_length=255, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default='main', max_length=255, verbose_name='Имя меню'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='django_tree.menuitem', verbose_name='Родитель'),
        ),
    ]