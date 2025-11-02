# data_app/forms.py (Contoh)
from django import forms
from .models import DRFPost

class DRFPostEditForm(forms.ModelForm):
    # Asumsi Grade choices sudah didefinisikan
    class Meta:
        model = DRFPost
        fields = ['nama', 'author', 'rating','image'] 
        
        # Tambahkan kelas 'form-control' untuk styling Bootstrap
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            # Field rating (ChoiceField) juga akan mengambil kelas form-control secara default 
            # jika didefinisikan sebagai ChoiceField di form atau model.
            'rating': forms.Select(attrs={'class': 'form-select'}), 
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# data_app/forms.py



# Choices untuk Form harus mencocokkan nilai di Model
# Models: [('excellent', 1), ('average', 0), ('bad', -1)] 
# Nilai (kiri) harus sama: 'excellent', 'average', 'bad'
# Label (kanan) bisa diubah untuk tampilan
FORM_GRADE_CHOICES = (
    ('excellent', 'Excellent (Rating 1)'),
    ('average', 'Average (Rating 0)'),
    ('bad', 'Bad (Rating -1)'),
)

class DRFPostCreateForm(forms.ModelForm):
    # Field rating di-override untuk menggunakan choices yang disesuaikan
    rating = forms.ChoiceField(choices=FORM_GRADE_CHOICES, label='Rating Kualitas')

    class Meta:
        model = DRFPost
        # Masukkan semua field yang ingin diisi, termasuk 'image'
        fields = ['nama', 'author', 'rating', 'image'] 
        
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            # ImageField menggunakan ClearableFileInput secara default
        }