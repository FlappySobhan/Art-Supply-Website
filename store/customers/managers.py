from django.contrib.auth.models import BaseUserManager

class UsersManager(BaseUserManager):
    def actives(self):
        return self.filter(is_active=True)
    def admins(self):
        return self.filter(is_admin=True)
    def deleted(self):
        return self.filter(is_deleted=True)

    def create_user(self, phone_number, password, email=None, first_name=None,last_name=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            email=self.normalize_email(email) if email else None,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            is_active=True,
            is_admin=False,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, email=None,first_name=None,
    last_name=None, is_admin=True):
        user = self.create_user(phone_number,password, email, 
        first_name, last_name)
        user.is_active = True
        user.is_superuser = True
        user.is_admin = is_admin

        user.save(using=self._db)
        return user