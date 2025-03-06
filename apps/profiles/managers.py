from django.db import models
from django.db.models import Q


class ProfileManager(models.Manager):
    def get_all_profiles(self, me):
        from apps.profiles.models import Profile
        
        profiles = Profile.objects.select_related('user').filter(user__is_verified_email=True)
        return profiles