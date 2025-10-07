from django.contrib import admin
from .models import CaptionedImage

@admin.register(CaptionedImage)
class CaptionedImageAdmin(admin.ModelAdmin):
    list_display = ('original_filename', 'uploaded_at', 'caption_en', 'get_file_size_display')
    list_filter = ('uploaded_at',)
    search_fields = ('original_filename', 'caption_en')
    readonly_fields = ('uploaded_at', 'image_width', 'image_height', 'file_size')
    
    fieldsets = (
        ('Image Information', {
            'fields': ('image', 'original_filename', 'uploaded_at', 'file_size', 'image_width', 'image_height')
        }),
        ('Captions', {
            'fields': ('caption_en', 'caption_es', 'caption_fr', 'caption_de', 'caption_hi', 'caption_zh')
        }),
    )
    
    def get_file_size_display(self, obj):
        return obj.get_file_size_display()
    get_file_size_display.short_description = 'File Size'