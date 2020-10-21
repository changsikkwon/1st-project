import json
import traceback
import bcrypt
import jwt
import local_settings

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from kibon.settings         import SECRET_KEY
from .models                import (
    User,
    Gender
)

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            gender, created = Gender.objects.get_or_create(gender = data['gender'])
            signup_user = User(
                name         = data['name'],
                birthdate    = data['birthdate'],
                identifier   = data['identifier'],
                password     = data['password'],
                gender       = gender,
                phone_number = data['phone_number'],
                email        = data['email']
            )
            signup_user.full_clean()
            signup_user.password = bcrypt.hashpw(signup_user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            signup_user.save()
            return JsonResponse({
                'message' : 'SUCCESS',
                'name' : data['name']
                },
                status = 200)

        except ValidationError as e:
            trace_back = traceback.format_exc()
            print(f"{e} : {trace_back}")
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        return JsonResponse({'message' : 'Invalid format or Duplicated Email'}, status = 400)

class LoginView(View): 
    def post(self, request): 
        data = json.loads(request.body)
            
        try: 
            if User.objects.filter(identifier = data['identifier']).exists(): 
                signin_user    = User.objects.get(identifier = data['identifier'])
                input_password = data['password']
                if bcrypt.checkpw(input_password.encode('utf-8'), signin_user.password.encode('utf-8')): 
                    token = jwt.encode({'identifier' : signin_user.identifier}, SECRET_KEY, algorithm = local_settings.algorithm)
                    return JsonResponse({'token' : token.decode()}, status = 200)

                return JsonResponse({'message' : 'INVALID_PASSWORD'})
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)
        except KeyError: 
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)