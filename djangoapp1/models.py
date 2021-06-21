from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from django.contrib.gis.db import models as gis_models

class ProgramSarpras(models.Model):
    kodeProgram = models.CharField('Kode Program', primary_key=True, max_length=15, unique=True, editable=True)
    namaProgram = models.CharField('Nama Program', max_length=200)
    keterangan = models.TextField('Keterangan', max_length=300)

    #save_as = False

    def __str__(self):
        return u"%s -- %s" % (self.kodeProgram, self.namaProgram)

    def kode_nama(self):
        return format_html('Gabungan: %s - <b>%s' %(self.kodeProgram, self.namaProgram))

    class Meta:
        ordering = ('kodeProgram',)
        verbose_name = 'Program'
        verbose_name_plural = '2. Program'
        permissions =(
            ('read_item','can read_item'),
        )



class KegiatanSarpras(models.Model):
    kodeKegiatan = models.CharField('Kode Kegiatan', primary_key=True, max_length=15)
    kodeProgram = models.ForeignKey('ProgramSarpras', on_delete=models.CASCADE)
    namaKegiatan = models.CharField('Nama Kegiatan', max_length=200)
    keterangan = models.TextField('Keterangan', max_length=300, null=True)
    #untuk model many to many dan one to many bukan cascade
    #manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    #attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__ (self):
        return "%s -- %s" % (self.kodeKegiatan, self.namaKegiatan)

    class Meta:
        ordering = ('kodeKegiatan',)
        verbose_name = 'Kegiatan'
        verbose_name_plural = '3. Kegiatan'


class Sarpras(models.Model):
    kodeSarpras = models.CharField(primary_key=True, max_length=15)
    kodeKegiatan = models.ForeignKey('KegiatanSarpras', on_delete=models.CASCADE)
    namaSarpras = models.CharField(max_length=150)
    tahun = models.IntegerField()
    foto = models.ImageField(upload_to='static/uploads/%Y/%m/%d', null=True)
    lokasi = gis_models.PointField(srid=4326)
    keterangan = models.TextField(max_length=300)
    verifikasiS = models.BooleanField(default=True)
    userS = models.CharField(max_length=20, null=True)

    # keterangan = RichTextUploadingField(verbose_name='keterangan', null=True)

    def __self__(self):
        return self.title

    class Meta:
        ordering = ('kodeSarpras',)
        verbose_name_plural = "6. Kegiatan Sarana dan Prasarana"

class InfrastrukturJalan(models.Model):
    kodeInfrastrukturJ = models.CharField(primary_key=True, max_length=15)
    kodeKegiatan = models.ForeignKey('KegiatanSarpras', on_delete=models.CASCADE)
    namaInfrastrukturJ = models.CharField(max_length=150)
    tahun = models.IntegerField()
    foto = models.ImageField(upload_to='static/uploads/%Y/%m/%d', null=True)
    lokasi = gis_models.LineStringField(srid=4326)
    keterangan = models.TextField(max_length=300)

    # keterangan = RichTextUploadingField(verbose_name='keterangan', null=True)

    def __self__(self):
        return self.title

    class Meta:
        ordering = ('kodeInfrastrukturJ',)
        verbose_name_plural = "7. Kegiatan Infrastruktur Jalan"

class Kecamatan(models.Model):
    kodeKec = models.CharField(max_length=10)
    namaKec = models.CharField(max_length=50)
    namaKec2 = models.CharField(max_length=45)
    keterangan = models.TextField(max_length=200, null=True)
    geometry = gis_models.MultiPolygonField(srid=4326)

    class Meta:
        ordering = ('kodeKec',)
        verbose_name_plural = "1. Daftar Kecamatan"

class JalanPropinsi(models.Model):
    kodeJalanP = models.CharField(max_length=10, null=True)
    namaJalanP = models.CharField(max_length=70)
    fungsiJalanP = models.CharField(max_length=40, null=True)
    panjangJalanP = models.FloatField(null=True)
    lebarJalanP = models.FloatField(null=True)
    photo = models.ImageField(upload_to='static/uploads/%Y/%m/%d', null=True)
    kondisiJalanP = models.CharField(max_length=15, null=True)
    keterangan = models.TextField(max_length=100, null=True)
    geometry =gis_models.MultiLineStringField(srid=4326, null=True)

    class Meta:
        ordering = ('kodeJalanP',)
        verbose_name_plural = "4. Jalan Propinsi"

class JalanKabupaten(models.Model):
    kodeJalanK = models.CharField(max_length=10, null=True)
    namaJalanK = models.CharField(max_length=70)
    fungsiJalanK = models.CharField(max_length=40, null=True)
    panjangJalanK = models.FloatField(null=True)
    lebarJalanK = models.FloatField(null=True)
    photo = models.ImageField(upload_to='static/uploads/%Y/%m/%d', null=True)
    kondisiJalanK = models.CharField(max_length=15, null=True)
    keterangan = models.TextField(max_length=100, null=True)
    geometry =gis_models.MultiLineStringField(srid=4326, null=True)

    class Meta:
        ordering = ('kodeJalanK',)
        verbose_name_plural = "5. Jalan Kabupaten"

#tambahan data dinas di Pemda OKUS
#23 Maret 2021
class Dinas(models.Model):
    kodeKegiatan = models.ForeignKey('KegiatanSarpras', on_delete=models.CASCADE, null=True)
    dinas = models.CharField(max_length=70)
    posisi = models.CharField(max_length=30),
    tahunInputData = models.IntegerField(default=2021)
    ASN = models.IntegerField(default=0)
    nonASN = models.IntegerField(default=0)
    sd = models.IntegerField(default=0)
    smp = models.IntegerField(default=0)
    sma = models.IntegerField(default=0)
    d1 = models.IntegerField(default=0)
    d2 = models.IntegerField(default=0)
    d3 = models.IntegerField(default=0)
    d4 = models.IntegerField(default=0)
    s1 = models.IntegerField(default=0)
    s2 = models.IntegerField(default=0)
    s3 = models.IntegerField(default=0)
    gol1a = models.IntegerField(default=0)
    gol1b = models.IntegerField(default=0)
    gol1c = models.IntegerField(default=0)
    gol1d = models.IntegerField(default=0)
    gol2a = models.IntegerField(default=0)
    gol2b = models.IntegerField(default=0)
    gol2c = models.IntegerField(default=0)
    gol2d = models.IntegerField(default=0)
    gol3a = models.IntegerField(default=0)
    gol3b = models.IntegerField(default=0)
    gol3c = models.IntegerField(default=0)
    gol3d = models.IntegerField(default=0)
    gol4a = models.IntegerField(default=0)
    gol4b = models.IntegerField(default=0)
    gol4c = models.IntegerField(default=0)
    gol4d = models.IntegerField(default=0)
    gol4e = models.IntegerField(default=0)
    tahunInput = models.IntegerField(default=2021),
    anggaran2016 = models.FloatField(default=0.0)
    anggaran2017 = models.FloatField(default=0.0)
    anggaran2018 = models.FloatField(default=0.0)
    anggaran2019 = models.FloatField(default=0.0)
    anggaran2020 = models.FloatField(default=0.0)
    anggaran2021 = models.FloatField(default=0.0)
    foto = models.ImageField(upload_to='static/uploads/%Y/%m/%d', null=True)
    keterangan = models.TextField(max_length=100, null=True)
    geometry = gis_models.PointField(srid=4326, null=True)

    class Meta:
        verbose_name_plural = "8. Dinas Kabupaten OKUS"