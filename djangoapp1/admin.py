from django.contrib import admin
#from django import forms
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from django.db.models import Count
from .models import ProgramSarpras, KegiatanSarpras, Sarpras, Kecamatan, JalanPropinsi, JalanKabupaten, InfrastrukturJalan, Dinas


"""
class ProgramSaranaForm(forms.ModelForm):
    class Meta:
        model = ProgramSarpras
        fields = (('kodeProgram', 'namaProgram'), 'keterangan')
        
        fieldsets = (
             (None, {
                 'fields': ('kodeProgram',)
             }),
             ('Opsional tambahan', {
                 'classes': ('collapse',),  # extrapretty/wide/collapse
                 'fields': ('namaProgram',),
             }),
         )
        
        #exclude = ['keterangan']
"""

class ProgramSarprasAdmin(admin.ModelAdmin):
    #actions_on_top = False
    #save_as = True
    list_display = ['kodeProgram','namaProgram','keterangan','kode_nama']
    list_per_page = 10
    #list_display_links = ['kodeProgram','namaProgram']
    #list_editable = ['namaProgram','keterangan']
    search_fields = ('kodeProgram', 'namaProgram',)
    #fields = (('kodeProgram','namaProgram'),)
    #prepopulated_fields = {"keterangan": ("kodeProgram",)}
    ordering = ('kodeProgram',)
    fieldsets = (
         ('Jenis Program Sarana Prasarana dan Insrastruktur', {
             'fields': (('kodeProgram','namaProgram'),)
         }),
         ('Keterangan tambahan program', {
             'classes': ('collapse',),  # extrapretty/wide/collapse
             'fields': ('keterangan',),
         }),
     )
    # exclude = ('keterangan',)
    #model = ProgramSarpras
    #form = ProgramSaranaForm

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('programsarprass.read_item'):
            return (f.name for f in self.model._meta.fields)
        return super(ProgramSarprasAdmin, self).get_readonly_fields(
            request, obj=obj
        )

# class KegiatanSarprasAdmin(admin.ModelAdmin):
#     list_display = ('kodeProgram', 'jumlahKegiatan')
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.annotate(
#             _jumlahKegiatan=Count("kodeKegiatan", distinct=True),
#         )
#         return queryset
#     def jumlahKegiatan(self, obj):
#         return obj._jumlahKegiatan

"""
class KegiatanSarprasInline(admin.TabularInline):
    model = KegiatanSarpras

class ProgramSarprasAdmin(admin.ModelAdmin):
    list_display = ['kodeProgram']
    inlines = [
        KegiatanSarprasInline,
    ]
"""


def upper_case_name3(obj):
    return ("%s" % (obj.kodeProgram))
upper_case_name3.short_description = 'Kode Program'

class KegiatanSarprasAdmin(admin.ModelAdmin):
    raw_id_fields = ('kodeProgram',)
    list_display = ('upper_case_name', 'namaKegiatan', 'keterangan', 'kodeProgram','nama_Program')
    search_fields = ('kodeKegiatan', 'namaKegiatan',)
    list_filter =  ['kodeKegiatan', 'kodeProgram']
    save_on_top = True
    save_as = True
    save_as_continue = False
    view_on_site = True
    #readonly_fields = ['keterangan']
    #list_filter = ('kodeProgram',)
    #prepopulated_fields = {"keterangan": ("kodeProgram","kodeKegiatan", "namaKegiatan")}
    #radio_fields = {'kodeProgram': admin.VERTICAL}
    #ordering = ('kodeProgram',)

    def nama_Program(self, obj):
        return obj.kodeProgram.namaProgram
    nama_Program.short_description = 'Nama Program'

    def upper_case_name(self, obj):
        return ("%s" % (obj.kodeKegiatan)).upper()

    upper_case_name.short_description = 'Kode Kegiatan'


    #def programS(self, obj):
    #    return obj.kodeProgram.kodeProgram
    #programS.short_description = "Kode ProgramS"

class SarprasAdmin(OSMGeoAdmin):
    list_display = ('kodeSarpras','namaSarpras', 'tahun', 'userS')
    search_fields = ('kodeSarpras', 'namaSarpras','userS')
    filter_fields = ('kodeSarpras', 'namaSarpras', 'tahun', 'userS')
    list_select_related = ('kodeKegiatan',)
    exclude = ('verifikasiS',)
    default_lat = -536310
    default_lon = 11579017
    default_zoom= 12

class InfrastrukturJalanAdmin(OSMGeoAdmin):
    list_display = ('kodeInfrastrukturJ', 'namaInfrastrukturJ', 'tahun')
    default_lat = -536310
    default_lon = 11579017
    default_zoom = 10

class KecamatanAdmin(OSMGeoAdmin):
    list_display = ('kodeKec', 'namaKec', 'keterangan')
    default_lat = -536310
    default_lon = 11579017
    default_zoom = 10

class JalanPropinsiAdmin(OSMGeoAdmin):
    list_display = ('kodeJalanP', 'namaJalanP','fungsiJalanP')

class JalanKabupatenAdmin(OSMGeoAdmin):
    list_display = ('kodeJalanK', 'namaJalanK','fungsiJalanK')

class DinasAdmin(LeafletGeoAdmin):
    list_display = ('dinas', 'ASN', 'tahunInputData')
    #fields = (('dinas', 'ASN'),)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["kodeKegiatan"].label = "Kode Kegiatan"
        form.base_fields["dinas"].label = "Nama Dinas"
        form.base_fields["tahunInputData"].label = "Tahun Input"
        form.base_fields["ASN"].label = "Jumlah ASN"
        form.base_fields["nonASN"].label = "Jumlah Non ASN"
        form.base_fields["sd"].label = "Jumlah lulus SD"
        form.base_fields["smp"].label = "Jumlah lulus SMP"
        form.base_fields["sma"].label = "Jumlah lulus SMA"
        form.base_fields["d1"].label = "Jumlah lulus D1"
        form.base_fields["d2"].label = "Jumlah lulus D2"
        form.base_fields["d3"].label = "Jumlah lulus D3"
        form.base_fields["d4"].label = "Jumlah lulus D4"
        form.base_fields["s1"].label = "Jumlah lulus S1"
        form.base_fields["s2"].label = "Jumlah lulus S2"
        form.base_fields["s3"].label = "Jumlah lulus S3"
        form.base_fields["gol1a"].label = "Jumlah pegawai Gol IA"
        form.base_fields["gol1b"].label = "Jumlah pegawai Gol IB"
        form.base_fields["gol1c"].label = "Jumlah pegawai Gol IC"
        form.base_fields["gol1d"].label = "Jumlah pegawai Gol ID"
        form.base_fields["gol2a"].label = "Jumlah pegawai Gol IIA"
        form.base_fields["gol2b"].label = "Jumlah pegawai Gol IIB"
        form.base_fields["gol2c"].label = "Jumlah pegawai Gol IIC"
        form.base_fields["gol2d"].label = "Jumlah pegawai Gol IID"
        form.base_fields["gol3a"].label = "Jumlah pegawai Gol IIIA"
        form.base_fields["gol3b"].label = "Jumlah pegawai Gol IIIB"
        form.base_fields["gol3c"].label = "Jumlah pegawai Gol IIIC"
        form.base_fields["gol3d"].label = "Jumlah pegawai Gol IIID"
        form.base_fields["gol4a"].label = "Jumlah pegawai Gol IVA"
        form.base_fields["gol4b"].label = "Jumlah pegawai Gol IVB"
        form.base_fields["gol4c"].label = "Jumlah pegawai Gol IVC"
        form.base_fields["gol4d"].label = "Jumlah pegawai Gol IVD"
        form.base_fields["gol4e"].label = "Jumlah pegawai Gol IVE"
        form.base_fields["anggaran2016"].label = "Anggaran Tahun 2016"
        form.base_fields["anggaran2017"].label = "Anggaran Tahun 2017"
        form.base_fields["anggaran2018"].label = "Anggaran Tahun 2018"
        form.base_fields["anggaran2019"].label = "Anggaran Tahun 2019"
        form.base_fields["anggaran2020"].label = "Anggaran Tahun 2020"
        form.base_fields["anggaran2021"].label = "Anggaran Tahun 2021"
        form.base_fields["foto"].label = "Foto Gedung"
        form.base_fields["keterangan"].label = "Keterangan (tidak boleh kosong)"
        form.base_fields["geometry"].label = "Lokasi Gedung"
        return form

    default_lat = -505878
    default_lon = 11588093
    default_zoom = 15

admin.site.register(ProgramSarpras, ProgramSarprasAdmin)
admin.site.register(KegiatanSarpras, KegiatanSarprasAdmin)
admin.site.register(Sarpras, SarprasAdmin)
admin.site.register(InfrastrukturJalan, InfrastrukturJalanAdmin)
admin.site.register(Kecamatan, KecamatanAdmin)
admin.site.register(JalanPropinsi, JalanPropinsiAdmin)
admin.site.register(JalanKabupaten, JalanKabupatenAdmin)
admin.site.register(Dinas, DinasAdmin)