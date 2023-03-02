# from django.contrib.auth.base_user import BaseUserManager




# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_user(self, phone_number, password=None,**extra_fields):
#         if not phone_number:
#             raise ValueError('Phone number is required')
        
#         user = self.model(phone_number=phone_number,**extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
     