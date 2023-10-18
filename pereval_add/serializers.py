from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *


# сериализатор вложенной модели уровней сложности перевала
class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring',
        ]


# сериализатор вложенной модели географичеких координат перевала
class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height',
        ]


# сериализатор вложенной модели пользователя, создающего запись о перевале
class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
            'mail',
            'fam',
            'name',
            'otc',
            'phone',
        ]

    def save(self, **kwargs):
        self.is_valid()
        user = Users.objects.filter(mail=self.validated_data.get('mail'))
        if user.exists():
            return user.first()
        else:
            new_user = Users.objects.create(
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
                phone=self.validated_data.get('phone'),
                mail=self.validated_data.get('mail'),
            )
            return new_user


class ImagesSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Pereval_image
        fields = [
            'pk',
            'image'
        ]


# сериализатор модели самого перевала
class PerevalAddedSerializer(WritableNestedModelSerializer):
    coords = CoordsSerializer()
    category = SeasonSerializer()
    users = UsersSerializer()
    images = ImagesSerializer()

    class Meta:
        model = Pereval_added
        depth = 1
        fields = [
            'id',
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'users',
            'coords',
            'season',
            'images',
            'status',
        ]

    # переопределяем метод post
    def create(self, validated_data, **kwargs):
        users = validated_data.pop('users')
        coords = validated_data.pop('coords')
        season = validated_data.pop('season')
        images = validated_data.pop('images')

        users_ = Users.objects.filter(mail=users['mail'])
        if users_.exists():
            users_serializer = UsersSerializer(data=users)
            users_serializer.is_valid(raise_exception=True)
            users = users_serializer.save()
        else:
            author = Users.objects.create(**users)

        coords = Coords.objects.create(**coords)
        season = Season.objects.create(**season)
        pereval = Pereval_added.objects.create(**validated_data, images=images, author=author,
                                               coords=coords, season=season)
        if images:
            for imag in images:
                name = imag.pop(name)
                photos = photos.pop(photos)
                Pereval_image.objects.create(pereval=pereval, name=name, photo=photos)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_users = self.instance.users
            data_users = data.get('users')
            users_fields_for_validation = [
                instance_users.fam != data_users['fam'],
                instance_users.name != data_users['name'],
                instance_users.otc != data_users['otc'],
                instance_users.phone != data_users['phone'],
                instance_users.email != data_users['mail'],
            ]
            if data_users is not None and any(users_fields_for_validation):
                raise serializers.ValidationError(
                    {
                        'Отказано': 'Данные пользователя не могут быть изменены',
                    }
                )
        return data


class PerevalDetailSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    images = ImagesSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = Pereval_added
        fields = ['id',
                  'beautyTitle',
                  'title',
                  'other_titles',
                  'connect',
                  'add_time',
                  'status',
                  'season',
                  'coords',
                  'users',
                  'images']

    def validate(self, data):
        users_data = data.get('users')
        user = self.instance.user
        if users_data is not None:

            if user.first_name != users_data.get('first_name') \
                    or user.last_name != users_data.get('last_name') \
                    or user.patronymic != users_data.get('patronymic') \
                    or user.email != users_data.get('email') \
                    or user.phone != users_data.get('phone'):
                raise ValidationError({'message': 'Редактирование пользовательских данных запрещено'})
            return data
