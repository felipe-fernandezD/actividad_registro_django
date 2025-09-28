from django.contrib import admin
from .models import Armador,Nave,Certificado

# Register your models here.
class CertidicadoInline(admin.TabularInline):
    model = Certificado
    extra = 0
@admin.register(Nave)
class NaveAdmin(admin.ModelAdmin):
    list_display = ("matricula","nombre","tipo","armador","anio","activa")
    list_filter = ("activa","tipo","anio")
    search_fields = ("matricula","nombre","armador__nombre")
    inlines = [CertidicadoInline]
    actions= ["marcar_inactiva"]
    
    @admin.action(description="Marcar seleccionada como inactivas")
    def marcar_inactivas(self,request,queryset):
        updated = queryset.update(activa=False)
        self.message_user(request,f"{updated} naves marcadas como inactivas.")
@admin.register(Armador)
class ArmadorAdmin(admin.ModelAdmin):
    list_display = ("nombre","rut","email")
    search_fields = ("nombre","rut","email")

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ("nave","tipo","fecha_emision","fecha_vencimiento")
    list_filter = ("tipo",)
    search_fields = ("nave__matricula","nave__nombre","tipo")
    