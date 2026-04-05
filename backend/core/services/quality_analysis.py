import os
import io
import PyPDF2
from docx import Document
import logging

logger = logging.getLogger(__name__)

def analyze_resource_quality(file_handle):
    """
    Analyzes a file to determine page count, word count, and a quality score.
    Supports PDF and DOCX.
    """
    stats = {
        'page_count': 1,
        'word_count': 0,
        'quality_score': 50.0, # Base quality
        'bonus_points': 0
    }

    try:
        filename = file_handle.name.lower()
        file_content = file_handle.read()
        file_handle.seek(0) # Reset pointer for later saving
        
        file_stream = io.BytesIO(file_content)

        if filename.endswith('.pdf'):
            stats = _analyze_pdf(file_stream)
        elif filename.endswith('.docx'):
            stats = _analyze_docx(file_stream)
        
        # Calculate bonus points (Capped at 50)
        # 2 points per page (up to 10 pages) -> 20 BP
        # 1 point per 100 words (up to 3000 words) -> 30 BP
        page_bonus = min(stats['page_count'] * 2, 20)
        word_bonus = min(stats['word_count'] // 100, 30)
        stats['bonus_points'] = page_bonus + word_bonus
        
        # Initial Quality Score (0-100)
        # Combination of length and density
        stats['quality_score'] = min(50 + (page_bonus + word_bonus), 100)

    except Exception as e:
        logger.error(f"Error analyzing document quality: {e}")
        # Return defaults on error

    return stats

def _analyze_pdf(stream):
    try:
        reader = PyPDF2.PdfReader(stream)
        pages = len(reader.pages)
        word_count = 0
        
        # Sample text from first 3 pages and last 3 pages to estimate word count
        sample_pages = list(range(pages))
        if pages > 6:
            sample_pages = [0, 1, 2, pages-3, pages-2, pages-1]
            
        for i in sample_pages:
            try:
                page_text = reader.pages[i].extract_text()
                if page_text:
                    word_count += len(page_text.split())
            except:
                continue
        
        # Extrapolate if we sampled
        if pages > 6:
            word_count = int(word_count * (pages / 6))

        return {
            'page_count': pages,
            'word_count': word_count
        }
    except:
        return {'page_count': 1, 'word_count': 0}

def _analyze_docx(stream):
    try:
        doc = Document(stream)
        word_count = 0
        for para in doc.paragraphs:
            word_count += len(para.text.split())
        
        # Estimating pages for docx is tricky, we'll use a rough word/page ratio
        # ~250 words per page
        pages = max(1, word_count // 250)
        
        return {
            'page_count': pages,
            'word_count': word_count
        }
    except:
        return {'page_count': 1, 'word_count': 0}
