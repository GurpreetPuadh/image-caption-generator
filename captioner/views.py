from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from PIL import Image
import json
import os

from transformers import BlipProcessor, BlipForConditionalGeneration
from googletrans import Translator

from .models import CaptionedImage

# Initialize the model (lazy loading)
processor = None
model = None
translator = Translator()

def load_model():
    """Load the BLIP model lazily"""
    global processor, model
    if processor is None or model is None:
        print("Loading BLIP model... This may take 30-60 seconds on first run.")
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        print("Model loaded successfully!")

def generate_caption(image_path):
    """Generate caption for an image using BLIP model - 50 words"""
    load_model()
    
    # Open and process image
    raw_image = Image.open(image_path).convert('RGB')
    
    # Process image
    inputs = processor(raw_image, return_tensors="pt")
    
    # Generate longer caption (50 words approximately = 250 tokens max)
    out = model.generate(
        **inputs, 
        max_length=250,  # Increased for ~50 words
        min_length=100,  # Minimum length for better descriptions
        num_beams=5,     # Better quality
        repetition_penalty=2.0,  # Avoid repetition
        length_penalty=1.0,
        early_stopping=True
    )
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

def translate_caption(text, target_language):
    """Translate caption to target language"""
    try:
        if target_language == 'en':
            return text
        
        print(f"Translating to {target_language}: {text}")
        
        # Use googletrans for translation
        translation = translator.translate(text, src='en', dest=target_language)
        translated_text = translation.text
        
        print(f"Translation result: {translated_text}")
        return translated_text
        
    except Exception as e:
        print(f"Translation error: {e}")
        # Fallback: try again with a fresh translator instance
        try:
            new_translator = Translator()
            translation = new_translator.translate(text, src='en', dest=target_language)
            return translation.text
        except:
            print(f"Fallback translation also failed, returning original text")
            return text

def index(request):
    """Main page view"""
    recent_images = CaptionedImage.objects.all()[:10]
    return render(request, 'captioner/index.html', {
        'recent_images': recent_images
    })

@csrf_exempt
def upload_image(request):
    """Handle single or multiple image uploads"""
    if request.method == 'POST' and request.FILES:
        results = []
        
        # Get language preference
        target_language = request.POST.get('language', 'en')
        print(f"Selected language: {target_language}")
        
        # Process each uploaded file
        files = request.FILES.getlist('images')
        
        for uploaded_file in files[:5]:  # Limit to 5 images
            try:
                # Save image
                file_path = default_storage.save(f'uploads/{uploaded_file.name}', uploaded_file)
                full_path = default_storage.path(file_path)
                
                # Get image dimensions
                with Image.open(full_path) as img:
                    width, height = img.size
                
                # Generate caption (50 words)
                print(f"Generating caption for {uploaded_file.name}...")
                caption_en = generate_caption(full_path)
                print(f"Caption generated (English): {caption_en}")
                print(f"Caption word count: {len(caption_en.split())}")
                
                # Translate if needed
                if target_language != 'en':
                    caption_translated = translate_caption(caption_en, target_language)
                    print(f"Caption translated ({target_language}): {caption_translated}")
                else:
                    caption_translated = caption_en
                
                # Save to database
                captioned_image = CaptionedImage.objects.create(
                    image=file_path,
                    original_filename=uploaded_file.name,
                    caption_en=caption_en,
                    file_size=uploaded_file.size,
                    image_width=width,
                    image_height=height
                )
                
                # Save translated caption based on language
                if target_language == 'es':
                    captioned_image.caption_es = caption_translated
                elif target_language == 'fr':
                    captioned_image.caption_fr = caption_translated
                elif target_language == 'de':
                    captioned_image.caption_de = caption_translated
                elif target_language == 'hi':
                    captioned_image.caption_hi = caption_translated
                elif target_language == 'zh':
                    captioned_image.caption_zh = caption_translated
                
                captioned_image.save()
                
                results.append({
                    'success': True,
                    'filename': uploaded_file.name,
                    'caption': caption_translated,
                    'caption_en': caption_en,
                    'image_url': captioned_image.image.url,
                    'width': width,
                    'height': height,
                    'size': captioned_image.get_file_size_display(),
                    'language': target_language
                })
                
            except Exception as e:
                print(f"Error processing {uploaded_file.name}: {e}")
                import traceback
                traceback.print_exc()
                results.append({
                    'success': False,
                    'filename': uploaded_file.name,
                    'error': str(e)
                })
        
        return JsonResponse({'results': results})
    
    return JsonResponse({'error': 'No images uploaded'}, status=400)

def download_captions(request):
    """Download all captions as JSON"""
    images = CaptionedImage.objects.all()
    
    data = []
    for img in images:
        data.append({
            'filename': img.original_filename,
            'uploaded_at': img.uploaded_at.isoformat(),
            'captions': {
                'en': img.caption_en,
                'es': img.caption_es,
                'fr': img.caption_fr,
                'de': img.caption_de,
                'hi': img.caption_hi,
                'zh': img.caption_zh,
            },
            'image_info': {
                'width': img.image_width,
                'height': img.image_height,
                'size': img.get_file_size_display()
            }
        })
    
    response = JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
    response['Content-Disposition'] = 'attachment; filename="captions.json"'
    return response