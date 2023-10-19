from django.core.exceptions import ValidationError
from rest_framework import serializers
from account.models import User

# for sending a password reset link to email
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from account.utils import Util
import pdb



# Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
	# Additional field for confirming the password during registration
	password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
	class Meta:
		model = User
		fields = ['email', 'name', 'password', 'password2', 'tc']
		extra_kwargs={
			'password':{'write_only':True}
		}

	# Custom validation for password and confirm password match
	def validate(self, attrs):     # data comes from view in attrs in this function
		password = attrs.get('password')
		password2 = attrs.get('password2')
		if password != password2:
			raise serializers.ValidationError('Password and Confirm Password does not match')
		return attrs

	def create(self, validate_data):
		return User.objects.create_user(**validate_data)



# Serializer for user login
class UserLoginSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(max_length=200)
	class Meta:
		model = User 
		fields = ['email', 'password']



# Serializer for user profile
class UserProfileSerializer(serializers.Serializer):
	class Meta:
		model = User
		fields = ['id', 'email', 'name']



# Serializer for changing a user's password
class UserChangePasswordSerializer(serializers.Serializer):
	password = serializers.CharField(max_length=200, style={'input_type':'password'}, write_only=True)
	password2 = serializers.CharField(max_length=200, style={'input_type':'password'}, write_only=True)
	class Meta:
		fields = ['password', 'password2']

	def validate(self, attrs):
		password = attrs.get('password')
		password2 = attrs.get('password2')
		user = self.context.get('user')   # Getting the user from view
		if password != password2:
			raise serializers.ValidationError('Password & Confirm Password does not match')
		user.set_password(password)
		user.save()
		return attrs



# Serializer for sending password reset email
class SendPasswordResetEmailSerializer(serializers.Serializer):
	email = serializers.EmailField(max_length=200)
	class Meta:
		fields = ['email']

	def validate(self, attrs):
		email = attrs.get('email')
		# Check if the user with the provided email exists
		if User.objects.filter(email=email).exists():
			user = User.objects.get(email=email)
			# Encode the user's ID and generate a password reset token
			user_id = urlsafe_base64_encode(force_bytes(user.id))
			print('Encoded user_id : ', user_id)
			token = PasswordResetTokenGenerator().make_token(user)
			print('Password Reset token : ', token)
			# Construct the password reset link
			link = 'http://localhost:3000/api/user/reset/' + user_id + '/' + token 
			print('Password Reset link : ', link)

			# Send an email to the user with the password reset link
			body = 'Click the following link to reset your Password : ' + link
			data = {
				'subject' : 'Reset Your Password',
				'body' : body,
				'to_email' : user.email
			}
			Util.send_email(data)     # Function to send emails in the Util module

			return attrs
		else:
			raise ValidationError('You are not a registered user')




# Serializer for resetiing a user's password
class UserPasswordResetSerializer(serializers.Serializer):
	password = serializers.CharField(max_length=200, style={'input_type':'password'}, write_only=True)
	password2 = serializers.CharField(max_length=200, style={'input_type':'password'}, write_only=True)
	class Meta:
		fields = ['password', 'password2']

	def validate(self, attrs):
		try:
			password = attrs.get('password')
			password2 = attrs.get('password2')
			user_id = self.context.get('user_id')   # get user_id & token from view
			token = self.context.get('token')
			if password != password2:
				raise serializers.ValidationError('Password & Confirm Password does not match')
			idd = smart_str(urlsafe_base64_decode(user_id))
			user = User.objects.get(id=idd)
			if not PasswordResetTokenGenerator().check_token(user, token):
				raise ValidationError('Token is not Valid or Expired')
			user.set_password(password)
			user.save()
			return attrs
		except DjangoUnicodeDecodeError as identifier:
			PasswordResetTokenGenerator().check_token(user, token)
			raise ValidationError('Token is not valid or expired')