from django.db import models
from django.utils import timezone

class CaptionedImage(models.Model):
    """Model to store uploaded images and their generated captions"""
    
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    original_filename = models.CharField(max_length=255)
    
    # Caption in original language (English)
    caption_en = models.TextField(blank=True)
    
    # Translated captions
    caption_es = models.TextField(blank=True, null=True)  # Spanish
    caption_fr = models.TextField(blank=True, null=True)  # French
    caption_de = models.TextField(blank=True, null=True)  # German
    caption_hi = models.TextField(blank=True, null=True)  # Hindi
    caption_zh = models.TextField(blank=True, null=True)  # Chinese
    
    # Metadata
    uploaded_at = models.DateTimeField(default=timezone.now)
    file_size = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Captioned Image'
        verbose_name_plural = 'Captioned Images'
    
    def __str__(self):
        return f"{self.original_filename} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"
    
    def get_caption(self, language='en'):
        """Get caption in specified language"""
        language_map = {
            'en': self.caption_en,
            'es': self.caption_es,
            'fr': self.caption_fr,
            'de': self.caption_de,
            'hi': self.caption_hi,
            'zh': self.caption_zh,
        }
        return language_map.get(language, self.caption_en)
    
    def get_file_size_display(self):
        """Return human-readable file size"""
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"