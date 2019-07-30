# Generated by Django 2.2.3 on 2019-07-30 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ticket', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('pending', 'Pending'), ('close', 'Close')], default='open', max_length=50)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('response_time', models.DateTimeField()),
                ('priority', models.CharField(choices=[('high', 'High'), ('mid', 'Mid'), ('low', 'Low')], max_length=50)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
