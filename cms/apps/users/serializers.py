__author__ = 'cagey'
__date__ = '2019/5/21 10:30 AM'
from .models import Upload_file,UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"

class Upload_fileSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.url

    class Meta:
        model = Upload_file
        fields = "__all__"


# class Upload_fileListSerializer(serializers.Serializer):
#     files = serializers.ListField(
#         child=serializers.FileField(max_length=100000,
#                                     allow_empty_file=False,
#                                     use_url=True),write_only=True
#     )
    # upload_files = serializers.ListField(
    #     child=serializers.CharField(max_length=1000,),read_only=True
    # )

    # def create(self, validated_data):
    #     files = validated_data.get('files')
    #     # files_list = []
    #     for index, url in enumerate(files):
    #         file = Upload_file.objects.create(url=url, user=UserProfile.objects.get(id=self.context['request'].user.id))
    #         # file = Upload_file.objects.create(url=url)
    #         f = Upload_fileSerializer(file, context=self.context)
    #         # files_list.append(f.data['url'])
    #         url = f.data['url']
    #     # return {'upload_files':files_list}
    #     return {'upload_file':url}