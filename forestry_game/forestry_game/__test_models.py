from forestry_game.models import CustomUser, Map, Execution
from django.contrib.auth.models import User

# Creating user
basic_user = User(username="yee", password="yee2", email="yee3")
basic_user.save()
custom_user = CustomUser(user=basic_user)
custom_user.save()

print(custom_user.user.username)
print(custom_user.user.password)
print(custom_user.user.email)

# Creating map

custom_map = Map(height=20, width=40)
custom_map.save()

print(custom_map.height)
print(custom_map.width)

# Creating new Execution

execution = Execution(score=10, user=custom_user, map=custom_map)
execution.save()

print(execution.score)
print(execution.user.user.username)
print(execution.map.width)

# delete data created in tests
execution.delete()
custom_map.delete()
custom_user.delete()
basic_user.delete()
