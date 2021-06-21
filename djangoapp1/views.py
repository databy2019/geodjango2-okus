from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from .models import Kecamatan, Sarpras, JalanPropinsi, JalanKabupaten, InfrastrukturJalan, Dinas

#library untuk form daftar
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

UserModel = get_user_model()
from .forms import SignUpForm
from django.views.generic import TemplateView
from .tokens import account_activation_token


class HomePageView(TemplateView):
    template_name = 'home.html'

def home(request):
    count = User.objects.count()
    all_lists = Kecamatan.objects.all().order_by('kodeKec')
    return render(request, 'home.html', {
        'count': count,
        'all_lists': all_lists,
    })

def login(request):
    return render(request, 'login.html', {
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

#prosedur alternatif untuk daftar
def daftar(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Silahkan aktifkan user Anda'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Silahkan konfirmasi email Anda untuk melanjutkan pendaftaran')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Terima kasih sudah sudah melakukan konfirmasi email, silahkan Anda sekarang bisa melakukan login')
    else:
        return HttpResponse('Activation link is invalid!')
#akhir dari prosedur daftar dan aktivasi

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

@login_required
def infrastruktur(request):
    return render(request, 'infrastruktur.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

def contact(request):
    return render(request, 'contact.html',{})

def SarprasData(request):
    #sarpras = serialize('geojson', Sarpras.objects.all(), geometry_field = 'point' , fields=('kodeSarpras', 'kodeKegiatan', 'namaSarpras', 'tahun','foto', 'lokasi','keterangan','verifikasiS','userS'))
    #sarpras = serialize('geojson', Sarpras.objects.filter(verifikasiS="True"))
    sarpras = serialize('geojson', Sarpras.objects.all())
    return HttpResponse(sarpras, content_type='json')

def KecamatanData(request):
    kecamatan = serialize('geojson', Kecamatan.objects.all())
    return HttpResponse(kecamatan, content_type='json')

def JalanPropinsiData(request):
    jalanpropinsi = serialize('geojson', JalanPropinsi.objects.all())
    return HttpResponse(jalanpropinsi, content_type='json')

def JalanKabupatenData(request):
    jalankabupaten = serialize('geojson', JalanKabupaten.objects.all())
    return HttpResponse(jalankabupaten, content_type='json')

def InfrastrukturJalanData(request):
    infrastrukturjalan = serialize('geojson', InfrastrukturJalan.objects.all())
    return HttpResponse(infrastrukturjalan, content_type='json')

def DinasData(request):
    dinas = serialize('geojson', Dinas.objects.all())
    return HttpResponse(dinas, content_type='json')