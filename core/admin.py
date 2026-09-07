from django.contrib import admin
from .models import User, Material, RawMaterial, ProcessResult


# User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role', 'is_approved')
    list_filter = ('role', 'is_approved')
    search_fields = ('username',)


# Material Admin
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'predicted_yield')
    search_fields = ('name',)


# Raw Material Admin
@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'purity')
    search_fields = ('name',)


# Process Result Admin (🔥 MAIN FIX)
@admin.register(ProcessResult)
class ProcessResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'material',
        'aluminum_yield',
        'digestion_temp',
        'digestion_pressure',
        'energy_consumption',
        'co2_emissions',
        'created_at'
    )

    list_filter = (
        'material',
        'digestion_temp',
        'digestion_pressure',
    )

    search_fields = (
        'material__name',
    )

    ordering = ('-created_at',)