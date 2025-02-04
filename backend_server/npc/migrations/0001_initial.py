# Generated by Django 5.1.5 on 2025-02-04 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('diplomation', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MerchantInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='npc.merchant')),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('role', models.CharField(choices=[('merchant', 'Merchant'), ('bounty_hunter', 'Bounty Hunter'), ('pirate', 'Pirate'), ('officer', 'Officer'), ('scientist', 'Scientist'), ('enemy', 'Enemy'), ('ally', 'Ally')], max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('dialogue', models.TextField(blank=True)),
                ('reputation_effect', models.IntegerField(default=0)),
                ('faction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='npcs', to='diplomation.faction')),
            ],
        ),
        migrations.AddField(
            model_name='merchant',
            name='npc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='merchant', to='npc.npc'),
        ),
        migrations.CreateModel(
            name='QuestGiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_quests', models.ManyToManyField(related_name='quest_givers', to='items.questitem')),
                ('npc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quest_giver', to='npc.npc')),
            ],
        ),
    ]
