from django.contrib.auth.models import BaseUserManager

class UsersManager(BaseUserManager):
    def actives(self):
        return self.filter(is_active=True)
    def admins(self):
        return self.filter(is_admin=True)
    def deleted(self):
        return self.filter(is_deleted=True)
