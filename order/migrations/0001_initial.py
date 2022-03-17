# Generated by Django 4.0.3 on 2022-03-17 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assortment', '0001_initial'),
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_in_queue', models.CharField(blank=True, max_length=64, verbose_name='name in queue')),
                ('status', models.SmallIntegerField(choices=[(0, ''), (1, 'Заказ принимается'), (2, 'Заказ готовится'), (3, 'Заказ готов'), (4, 'Заказ выдан')], default=1, verbose_name='status')),
                ('place', models.SmallIntegerField(blank=True, null=True, verbose_name='number of place')),
                ('comment', models.TextField(blank=True, verbose_name='comment')),
                ('is_registered', models.BooleanField(default=False, verbose_name='is registered')),
                ('paid', models.BooleanField(default=False, verbose_name='paid')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coupon.coupon')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order', verbose_name='order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='assortment.product')),
            ],
        ),
    ]
