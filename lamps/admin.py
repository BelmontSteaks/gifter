from django.contrib import admin
from lamps.models import UserProfile
from lamps.models import Group
from lamps.models import UserInGroup
from lamps.models import Gift
from lamps.models import List
from lamps.models import GiftOnList
from lamps.models import ListInGroup


admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(UserInGroup)
admin.site.register(Gift)
admin.site.register(List)
admin.site.register(GiftOnList)
admin.site.register(ListInGroup)
