from hello.models import Event


# python manage.py shell

event1 = Event(name="Test1",  event_date='2018-12-17',
               venue='Boston', manager='Peter')

event1 = Event(name="Rest1",  event_date='2018-12-17',
               venue='Boston', manager='Bob')

event1.save()

# Retrive All Records
# ********************************************************************
event_list = Event.objects.all()

# retrive single record
Event.objects.get(id=12)

Event.objects.get(manager='Joe')
Event.objects.get(name='Test1')

# Multiple records
Event.objects.filter(name__contains='Test')

Event.objects.filter(manager='Joe', name__contains='Test')r

Event.objects.filter(manager='Joe', name__startswith='T')


Event.objects.filter()

# OrderBy
# ********************************************************************
Event.objects.order_by('name')

Event.objects.order_by('-name')

Event.objects.order_by('-name', 'manager')

Event.objects.filter(name='Test1').order_by('-name')

# Slicing Data
Event.objects.filter(name='Test1').order_by('name')[0]

Event.objects.filter(name='Test1')[-1] - not supported
Event.objects.filter(name='Test1').order_by('-name')[0]

Event.objects.all()[1:2]

Event.objects.filter(name='Test1').order_by('name')[0:2]


# Updating Records
# ********************************************************************
# subsequent update after save
event1 = Event(name="Test1",  event_date='2018-12-17',
               venue='Boston', manager='Peter')
event1.save()
event1.manager = 'Simon'
event1.save()

event1.id
Event.objects.filter(id=12).update(manager='Joe')

# update multiple records
Event.objects.filter(manager='Joe').update(venue='San Francisco')


# Delete Records
# ********************************************************************
# Like
Event.objects.filter(name__contains='Test').delete()
# equal
Event.objects.filter(manager='Bob').delete()

# delete all
Event.objects.all().delete()


# event.object

# event_list = Event.objects.all()

# event_list = Event.objects.filter(manager='Bob')
