import secrets
from google.auth.transport import requests
from google.oauth2 import id_token
from accounts.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed



class Google():
	@staticmethod
	def validate(access_token):
		try:
			id_info = id_token.verify_oauth2_token(access_token, requests.Request())
			if "accounts.google.com" in id_info['iss']:
				return id_info

		except Exception as e:
			return "token is invalid or has expired"



def generate_strong_password(length=16):
	char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
	password = ''.join(secrets.choice(char_set) for i in range(length))
	return password


def login_social_user(email, password):
	user=authenticate(email=email, password=password)
	user_tokens = user.tokens()

	return {
		'email':user.email,
		'full_name': user.get_full_name,
		'access_token': str(user_tokens.get('access')),
		'refresh_token': str(user_tokens.get('refresh'))
	}


def register_social_user(provider, email, first_name, last_name):
	user = User.objects.filter(email=email)
	password = generate_strong_password()
	if user.exists():
		if provider == user[0].auth_provider:
			login_social_user(email, password)
		else:
			raise AuthenticationFailed(
				detail=f"please continue your login with {user[0].auth_provider}"
			)
	else:
		new_user = {
			'email':email,
			'first_name':first_name,
			'last_name':last_name,
			'password':password
		}
		register_user=User.objects.create_user(**new_user)
		register_user.auth_provider=provider
		register_user.is_verified=True
		register_user.save()

		login_social_user(email=register_user.email, password=password)