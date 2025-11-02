from django.shortcuts import render 
from rest_framework import generics
from basic_api.models import DRFPost,Mahasiswa,Dosen
from basic_api.serializers import DRFPostSerializer,MahasiswaSerializer,DosenSerializer
from .models import DRFPost
from .forms import DRFPostEditForm ,DRFPostCreateForm
from django.shortcuts import get_object_or_404, redirect

def dashboard_list(request):
    posts = list(DRFPost.objects.all()) # Konversi QuerySet ke list
    grouped_posts = []
    
    # Mengelompokkan data menjadi baris dengan 3 item per baris
    for i in range(0, len(posts), 3):
        grouped_posts.append(posts[i:i + 3])
        
    context = {
        'grouped_posts': grouped_posts,
    }
    return render(request, 'dashboard.html', context)

def post_edit(request, pk):
    # 1. Ambil objek yang akan diedit
    post = get_object_or_404(DRFPost, pk=pk)
    
    if request.method == 'POST':
        form = DRFPostEditForm(request.POST, request.FILES,instance=post)
        
        if form.is_valid():
            # 3. Form.save() memanggil metode ModelForm untuk menyimpan data ke database.
            #    Karena kita memberikan 'instance', ini akan melakukan operasi UPDATE.
            form.save() 
            
            # 4. Redirect ke halaman lain setelah berhasil (misalnya, dashboard)
            #    Ini mencegah pengiriman ulang form jika pengguna me-refresh halaman.
            return redirect('dashboard') 
    else:
        # GET request: Tampilkan form dengan data lama.
        form = DRFPostEditForm(instance=post)
        
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'post_edit.html', context)
#generics:
# kalo misal mau nambah data itu post dan kalau mau ambil data itu get
# Create your views here.
def post_create(request):
    if request.method == 'POST':
        # 1. Inisialisasi Form dengan data POST DAN file (request.FILES)
        #    request.FILES wajib ada jika ada ImageField atau FileField.
        form = DRFPostCreateForm(request.POST, request.FILES) 
        
        if form.is_valid():
            # 2. Menyimpan objek baru ke database (operasi CREATE)
            form.save() 
            
            # 3. Redirect ke dashboard setelah berhasil
            return redirect('dashboard') 
    else:
        # GET request: Tampilkan form kosong
        form = DRFPostCreateForm()
        
    context = {
        'form': form,
        'judul_halaman': 'Tambah Postingan Baru',
        'is_create': True # Digunakan di template untuk menyesuaikan teks tombol/judul
    }
    # Render ke template yang akan kita buat selanjutnya
    return render(request, 'post_create.html', context)

class API_objects(generics.ListCreateAPIView):
    queryset=DRFPost.objects.all()
    serializer_class=DRFPostSerializer

class API_objects_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=DRFPost.objects.all()
    serializer_class=DRFPostSerializer

class MahasiswaList(generics.ListCreateAPIView):
    queryset=Mahasiswa.objects.all()
    serializer_class=MahasiswaSerializer

class MahasiswaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mahasiswa.objects.all()
    serializer_class=MahasiswaSerializer

class DosenList(generics.ListCreateAPIView):
    queryset=Dosen.objects.all()
    serializer_class=DosenSerializer

class DosenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Dosen.objects.all()
    serializer_class=DosenSerializer

