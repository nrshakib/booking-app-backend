from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        UserModel = get_user_model()
        identifier = username or kwargs.get("email")

        if not identifier or not password:
            return None
        
        fields = {field.name for field in UserModel._meta.fields}
        query = Q()

        if "email" in fields:
            query |= Q(email__iexact=identifier)

        if "username" in fields:
            query |= Q(username__iexact=identifier)

        if not query:
            return None

        
        try:
            user = UserModel.objects.get(query)

        except UserModel.DoesNotExist:
            return None

        except UserModel.MultipleObjectsReturned:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None