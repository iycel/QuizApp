from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password  # passwordun validate olması için import ettik
from django.contrib.auth.hashers import make_password
from dj_rest_auth.serializers import TokenSerializer  
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())])  # username unique olması için
    first_name = serializers.CharField(required=True)  # isim girmenin required olması için yeniden yazdık
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})  # Passwordlarını girerken gözükmemesi için style={'input_type':'password'} yazdık

    class Meta :
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]

        extra_kwargs = {
            'password' : {'write_only' : True},  # Passwordların database de gözükmemesi için extra argüman ekledim
            'password2': {'write_only' : True}
        }

        # User modelimin fieldlerinda password 2 olmadığı için create metodunu overwrite edeceğiz. Create metodunun içerisinde gelen validated data create metodunu çıkartıp userimizi create edeceğiz.
    
    def create(self, validated_data):  # self olacak ve gelen datayı validated_data diye alıyoruz (Object-level validation -- 2 ayrı fieldi karşılaştırdığımız için)
        password = validated_data.get('password')
        validated_data.pop('password2') # validated_data dan pop modeli ile password2 yi çıkarıyoruz
        user = User.objects.create(**validated_data)  # validated_datadan userimizi create ettik
        user.set_password(password) # passwordlarımız database e açık bir şekilde yazamıyoruz. Hash lenerek yazıyoruz. O yüzden user create ederken password ü ayrı set etmemiz lazım.
        # user.password = make_password(password)  buda yazılabilir
        user.save()
        return user

    def validate(self, data):  # (Object-level validation -- 2 ayrı fieldi karşılaştırdığımız için)
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'Password fields did not match'})
        return data

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name'
        )
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)
    class Meta(TokenSerializer.Meta) :
        fields = (
            'key', 'user'
        )
