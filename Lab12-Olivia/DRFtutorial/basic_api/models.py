from django.db import models


Grade=[
    ('excellent',1),
    ('average',0),
    ('bad',-1)
]

class DRFPost(models.Model):
    nama=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    uploaded_date=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=Grade,max_length=10,default=0)
    image = models.ImageField(upload_to='image/', blank=True, null=True,default=None)#default none biar data sebelumnya gada gapapa
    class Meta:
        ordering=['uploaded_date']

    def __str__(self):
        return self.nama
    
class Mahasiswa(models.Model):
    nama=models.CharField(max_length=100)
    nim=models.CharField(max_length=100)
    dosen = models.ForeignKey(
        'Dosen',
        on_delete=models.SET_NULL,  # atau models.CASCADE sesuai kebutuhan
        null=True,
        blank=True,
        related_name='mahasiswas'
    )

    def __str__(self):
        return self.nama
    
class Dosen(models.Model):
    nama=models.CharField(max_length=100)
    prodi=models.CharField(max_length=100)

    def __str__(self):
        return self.nama