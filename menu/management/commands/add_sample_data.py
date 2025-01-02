from django.db import migrations

def add_sample_menu_items(apps, schema_editor):
    MenuItem = apps.get_model('menu', 'MenuItem')
    MenuItem.objects.bulk_create([
        MenuItem(id=1, name='Margherita Pizza', price=12.99, image='images/margherita.jpg', description='Classic pizza with fresh mozzarella and basil.'),
        MenuItem(id=2, name='Spaghetti Carbonara', price=15.99, image='images/carbonara.jpg', description='Creamy pasta with pancetta and Parmesan.'),
        MenuItem(id=3, name='Caesar Salad', price=9.99, image='images/caesar.jpg', description='Crisp romaine lettuce with Caesar dressing.')
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('menu', 'previous_migration_name'),  # Change this to the last migration you created
    ]

    operations = [
        migrations.RunPython(add_sample_menu_items),
    ]
