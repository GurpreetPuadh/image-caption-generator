# 🎨 AI Image Caption Generator

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2-green.svg)
![AI](https://img.shields.io/badge/AI-Hugging%20Face-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**An intelligent web application that generates detailed AI-powered captions for images in multiple languages**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

</div>

---

## 📖 About

AI Image Caption Generator is a Django-based web application that leverages the power of Salesforce's BLIP (Bootstrapping Language-Image Pre-training) model to automatically generate descriptive captions for images. The application supports translation into 6 different languages, making it accessible to a global audience.

### 🎯 Key Highlights

- **50-word detailed captions** for comprehensive image descriptions
- **Multi-language support** with instant translation
- **Batch processing** for multiple images simultaneously
- **Real-time generation** with progress indicators
- **Modern, responsive UI** that works on all devices
- **Export functionality** to save captions as JSON

---

## ✨ Features

### Core Capabilities

🤖 **AI-Powered Captioning**
- Uses Salesforce BLIP model for accurate image understanding
- Generates detailed 50-word descriptions
- Handles various image formats (JPG, PNG, WebP)

🌍 **Multi-Language Support**
- **English** 🇬🇧 - Default language
- **Spanish** 🇪🇸 - Español
- **French** 🇫🇷 - Français
- **German** 🇩🇪 - Deutsch
- **Hindi** 🇮🇳 - हिन्दी
- **Chinese** 🇨🇳 - 中文

📤 **Batch Processing**
- Upload up to 5 images at once
- Parallel processing for efficiency
- Progress tracking for each image

💾 **Data Management**
- Save caption history in database
- Export all captions as JSON
- Admin panel for management

🎨 **User Experience**
- Drag & drop file upload
- Real-time caption preview
- One-click copy to clipboard
- Responsive design for mobile/desktop
- Beautiful gradient UI with animations

---

## 🎬 Demo

### How It Works

1. **Upload**: Drag & drop or click to select images
2. **Select Language**: Choose from 6 available languages
3. **Generate**: Click button and wait for AI processing
4. **Copy & Save**: Copy captions or download as JSON

### Sample Output

**Image**: *A beautiful sunset over mountains*

**English Caption (50 words)**:
```
A breathtaking sunset scene over a majestic mountain range, with the sun 
casting vibrant orange and pink hues across the sky. The silhouette of 
the mountains creates a dramatic contrast against the colorful backdrop, 
while wispy clouds add texture to the serene landscape.
```

**Hindi Translation**:
```
पहाड़ों के ऊपर एक लुभावना सूर्यास्त दृश्य, सूरज आकाश में जीवंत नारंगी और 
गुलाबी रंग बिखेर रहा है। पहाड़ों का सिल्हूट रंगीन पृष्ठभूमि के खिलाफ एक 
नाटकीय विपरीतता पैदा करता है, जबकि बादल शांत परिदृश्य में बनावट जोड़ते हैं।
```

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **pip** (Python package manager)
- **Git** (for cloning repository)
- **2GB+ free disk space** (for AI model)
- **Internet connection** (for first-time model download)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/image-caption-generator.git
cd image-caption-generator

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

### 🌐 Access the Application

Open your browser and navigate to: **http://127.0.0.1:8000/**

---

## 📦 Dependencies

All required packages are listed in `requirements.txt`:

```txt
Django==4.2
Pillow==10.1.0
transformers==4.35.0
torch==2.1.0
googletrans==4.0.0rc1
```

### Installation Notes

- **First run**: The BLIP model (~1GB) will be downloaded automatically
- **Estimated time**: 5-10 minutes for initial setup
- **PyTorch**: CPU version is used by default (faster installation)

---

## 💻 Usage

### Basic Usage

1. **Start the server**
   ```bash
   python manage.py runserver
   ```

2. **Upload images**
   - Click the upload area or drag & drop
   - Select 1-5 images (JPG, PNG, WebP)

3. **Select language**
   - Choose from dropdown menu
   - Default is English

4. **Generate captions**
   - Click "Generate Captions"
   - Wait 30-60 seconds (first time only)
   - View generated captions

5. **Copy or download**
   - Click "Copy Caption" for individual captions
   - Click "Download All" for JSON export

### Admin Panel

Access the admin panel at: **http://127.0.0.1:8000/admin/**

```bash
# Create superuser
python manage.py createsuperuser

# Enter credentials:
Username: admin
Email: admin@example.com
Password: (your password)
```

**Admin Features**:
- View all uploaded images
- See captions in all languages
- Filter by upload date
- Search captions
- Delete images

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/upload/` | POST | Upload images and generate captions |
| `/download/` | GET | Download all captions as JSON |
| `/admin/` | GET | Django admin panel |

---

## 🛠️ Tech Stack

### Backend
- **Django 4.2** - Web framework
- **Python 3.8+** - Programming language
- **SQLite** - Database (upgradeable to PostgreSQL)

### AI/ML
- **Hugging Face Transformers** - Model integration
- **Salesforce BLIP** - Image captioning model
- **PyTorch** - Deep learning framework
- **Google Translate API** - Multi-language translation

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradients & animations
- **JavaScript (Vanilla)** - Interactive features
- **Responsive Design** - Mobile-first approach

### Image Processing
- **Pillow (PIL)** - Image manipulation and metadata

---

## 📁 Project Structure

```
image-caption-generator/
│
├── caption_project/              # Django project configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI configuration
│
├── captioner/                   # Main Django app
│   ├── migrations/              # Database migrations
│   ├── templates/
│   │   └── captioner/
│   │       └── index.html       # Main template
│   ├── models.py                # Database models
│   ├── views.py                 # View logic
│   ├── admin.py                 # Admin configuration
│   └── urls.py                  # App URL routing
│
├── media/                       # User uploaded images
│   └── uploads/
│
├── venv/                        # Virtual environment (not in git)
│
├── .gitignore                   # Git ignore file
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## ⚙️ Configuration

### settings.py

Key configuration options in `caption_project/settings.py`:

```python
# Maximum upload size (10MB)
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files
STATIC_URL = '/static/'
```

### Caption Generation

Adjust caption length in `captioner/views.py`:

```python
out = model.generate(
    **inputs, 
    max_length=250,      # Adjust for longer/shorter captions
    min_length=100,      # Minimum caption length
    num_beams=5,         # Quality (higher = better but slower)
)
```

---

## 🎯 Features Roadmap

### ✅ Completed
- [x] AI-powered image captioning
- [x] Multi-language support (6 languages)
- [x] Batch processing (5 images)
- [x] Real-time generation
- [x] Copy to clipboard
- [x] Download as JSON
- [x] Admin panel
- [x] Responsive design
- [x] 50-word detailed captions

### 🔜 Planned
- [ ] User authentication & profiles
- [ ] Caption editing functionality
- [ ] Social media sharing
- [ ] More languages (10+)
- [ ] Advanced image filters
- [ ] REST API for developers
- [ ] Caption confidence scores
- [ ] Dark/Light theme toggle
- [ ] Video frame captioning

---

## 🐛 Troubleshooting

### Common Issues

**Issue 1: "Module not found" errors**
```bash
# Solution: Ensure virtual environment is activated
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Issue 2: First caption takes 60+ seconds**
- **Normal behavior**: Model is downloading on first run (~1GB)
- **Subsequent captions**: Should be <5 seconds

**Issue 3: Translation not working (shows English)**
```bash
# Solution: Reinstall googletrans
pip uninstall googletrans
pip install googletrans==4.0.0rc1
```

**Issue 4: "No such table" error**
```bash
# Solution: Run migrations
python manage.py makemigrations
python manage.py migrate
```

**Issue 5: Port already in use**
```bash
# Solution: Use different port
python manage.py runserver 8001
```

### Debug Mode

Enable detailed error messages in `settings.py`:
```python
DEBUG = True  # Only for development!
```

**Warning**: Never use `DEBUG = True` in production!

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Write clear commit messages
- Add comments to your code
- Update documentation
- Test your changes thoroughly
- Follow PEP 8 style guide for Python code

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **[Hugging Face](https://huggingface.co/)** - For the amazing Transformers library
- **[Salesforce Research](https://github.com/salesforce/BLIP)** - For developing the BLIP model
- **[Django](https://www.djangoproject.com/)** - For the robust web framework
- **[Google Translate](https://translate.google.com/)** - For translation capabilities

---

## 📧 Contact & Support

- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- **LinkedIn**: [Your Profile](https://linkedin.com/in/your-profile)
- **Email**: your.email@example.com

### Issues & Bugs

Found a bug? Have a feature request? Please open an issue:
- [Report Bug](https://github.com/YOUR_USERNAME/image-caption-generator/issues/new)
- [Request Feature](https://github.com/YOUR_USERNAME/image-caption-generator/issues/new)

---

## 📊 Project Stats

- **Language**: Python
- **Framework**: Django
- **AI Model**: Salesforce BLIP
- **Languages Supported**: 6
- **Max Caption Length**: ~50 words
- **Max Batch Size**: 5 images
- **Database**: SQLite (upgradeable)

---

## 🌟 Show Your Support

If you found this project helpful, please consider:

- ⭐ **Starring the repository**
- 🍴 **Forking for your own use**
- 📢 **Sharing with others**
- 💬 **Providing feedback**

---

## 📈 Version History

- **v1.0.0** (2024) - Initial release
  - AI-powered captioning
  - 6 language support
  - Batch processing
  - 50-word detailed captions

---

<div align="center">

**Made with ❤️ using Django and AI**

[⬆ Back to Top](#-ai-image-caption-generator)

</div>