from rest_framework import serializers
from basic_api.models import DRFPost,Mahasiswa,Dosen

class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=DRFPost
        fields='__all__'
    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class DosenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosen
        fields = '__all__'

class MahasiswaSerializer(serializers.ModelSerializer):
    dosen = DosenSerializer(read_only=True)
    dosen_id = serializers.PrimaryKeyRelatedField(
        queryset=Dosen.objects.all(), source='dosen', write_only=True, required=False, allow_null=True
    )
    class Meta:
        model = Mahasiswa
        fields = ['id', 'nama', 'nim', 'dosen', 'dosen_id']