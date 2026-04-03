"""
OCR Service for extracting student information from ID card images.
Uses Tesseract OCR via pytesseract.

Designed for Sri Lankan university ID cards (SLIIT, UoM, UoC, etc.)
"""
import re
import logging
from datetime import datetime
from PIL import Image, ImageFilter, ImageEnhance

logger = logging.getLogger(__name__)

# Faculty code mapping (first 2 letters of Reg No)
FACULTY_MAP = {
    'IT': 'Computing',
    'SE': 'Computing',
    'CS': 'Computing',
    'DS': 'Computing',
    'EN': 'Engineering',
    'CE': 'Engineering',
    'ME': 'Engineering',
    'EE': 'Engineering',
    'BM': 'Business',
    'BA': 'Business',
    'MG': 'Business',
    'HS': 'Humanities & Sciences',
    'BT': 'Humanities & Sciences',
    'NS': 'Humanities & Sciences',
}

# Known university names for matching
KNOWN_UNIVERSITIES = [
    "SLIIT", "NSBM", "IIT", "CINEC", "SLTC", "Horizon Campus",
    "University of Moratuwa", "University of Colombo",
    "University of Peradeniya", "University of Sri Jayewardenepura",
    "University of Kelaniya", "University of Ruhuna",
    "University of Jaffna", "Eastern University",
    "Rajarata University", "Wayamba University",
    "Sabaragamuwa University", "South Eastern University",
    "Uva Wellassa University",
]

# Email domain mapping per university
EMAIL_DOMAIN_MAP = {
    "SLIIT": "@my.sliit.lk",
    "NSBM": "@students.nsbm.ac.lk",
    "IIT": "@iit.ac.lk",
}


def preprocess_image(image: Image.Image) -> Image.Image:
    """Preprocess image: grayscale, contrast boost, sharpen, scale up."""
    if image.mode != 'RGB':
        image = image.convert('RGB')

    width, height = image.size
    if width < 1200:
        scale = 1200 / width
        image = image.resize(
            (int(width * scale), int(height * scale)), Image.LANCZOS
        )

    image = image.convert('L')
    image = ImageEnhance.Contrast(image).enhance(2.5)
    image = ImageEnhance.Sharpness(image).enhance(2.0)
    image = image.filter(ImageFilter.SHARPEN)
    return image


def extract_reg_no(text: str) -> str:
    """
    Extract registration number from OCR text.
    Handles formats like:
      'IT 23 7795 70' -> 'IT23779570'
      'IT23779570'    -> 'IT23779570'
      'EN 22 1234 56' -> 'EN22123456'
    """
    # Pattern: 2 letters followed by digits with optional spaces
    # Matches 'IT 23 7795 70', 'IT23779570', etc.
    match = re.search(
        r'\b([A-Z]{2})\s*(\d{2})\s*(\d{3,4})\s*(\d{2,4})\b', text
    )
    if match:
        return ''.join(match.groups())

    # Fallback: simple pattern like IT23779570
    match = re.search(r'\b([A-Z]{2}\d{8,10})\b', text)
    if match:
        return match.group(1)

    return ""


def extract_nic_number(text: str) -> str:
    """Extract NIC number: 200232103198 or 991234567V."""
    match = re.search(r'\b(\d{12})\b', text)
    if match:
        return match.group(1)
    match = re.search(r'\b(\d{9}[vVxX])\b', text)
    if match:
        return match.group(1)
    return ""


def extract_name(text: str) -> str:
    """
    Extract student name from OCR text.
    Strategy:
    1. Look for text between 'STUDENT ID' line and 'Reg' line
    2. Find lines that look like names (all uppercase letters + spaces)
    """
    lines = [l.strip() for l in text.split('\n') if l.strip()]

    # Strategy 1: Find name between known markers
    student_id_idx = -1
    reg_idx = -1
    for i, line in enumerate(lines):
        lower = line.lower()
        if 'student id' in lower or 'student' in lower:
            student_id_idx = i
        if 'reg' in lower and ('no' in lower or ':' in lower):
            reg_idx = i

    # Name is typically between STUDENT ID header and Reg. No
    if student_id_idx >= 0 and reg_idx > student_id_idx:
        for i in range(student_id_idx + 1, reg_idx):
            candidate = lines[i].strip()
            # Name line: mostly letters and spaces, at least 4 chars
            cleaned = re.sub(r'[^A-Za-z\s]', '', candidate).strip()
            if len(cleaned) >= 4 and re.match(r'^[A-Za-z\s]+$', cleaned):
                return cleaned

    # Strategy 2: Look for "Name:" pattern
    for line in lines:
        if 'name' in line.lower() and ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2 and len(parts[1].strip()) > 2:
                return parts[1].strip()

    # Strategy 3: Find the longest uppercase-only line (likely the name)
    name_candidates = []
    for line in lines:
        cleaned = line.strip()
        # Skip lines with numbers, "SLIIT", "STUDENT", etc.
        if any(skip in cleaned.upper() for skip in ['SLIIT', 'STUDENT', 'REG', 'NIC', 'DATE', 'DIRECTOR', 'ADMIN']):
            continue
        if re.match(r'^[A-Z\s\.]{4,50}$', cleaned):
            name_candidates.append(cleaned)

    if name_candidates:
        return max(name_candidates, key=len)

    return ""


def extract_university(text: str) -> str:
    """Match OCR text against known university names."""
    text_lower = text.lower()
    for uni in KNOWN_UNIVERSITIES:
        if uni.lower() in text_lower:
            return uni
    return ""


def derive_faculty(reg_no: str) -> str:
    """Derive faculty from registration number prefix (first 2 chars)."""
    if len(reg_no) >= 2:
        prefix = reg_no[:2].upper()
        return FACULTY_MAP.get(prefix, "")
    return ""


def derive_academic_year(reg_no: str) -> str:
    """
    Calculate academic year from reg number.
    E.g., IT23... -> joined 2023. If current year is 2026, that's Year 3.
    """
    if len(reg_no) >= 4:
        try:
            year_digits = int(reg_no[2:4])
            # Convert 2-digit year to 4-digit
            if year_digits > 50:
                joined_year = 1900 + year_digits
            else:
                joined_year = 2000 + year_digits

            current_year = datetime.now().year
            years_since = current_year - joined_year + 1  # +1 because Year 1 starts at join

            if 1 <= years_since <= 6:
                return f"Year {years_since}"
            elif years_since > 6:
                return "Graduated"
        except ValueError:
            pass
    return ""


def derive_email(reg_no: str, university: str) -> str:
    """
    Generate student email from reg number and university.
    E.g., IT23779570 + SLIIT -> IT23779570@my.sliit.lk
    """
    if reg_no and university:
        domain = EMAIL_DOMAIN_MAP.get(university, "")
        if domain:
            return f"{reg_no}{domain}"
    return ""


def extract_data_from_id_image(image_file) -> dict:
    """
    Main OCR function: Opens an image, runs Tesseract,
    extracts fields, and derives additional data.
    """
    try:
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    except ImportError:
        logger.error("pytesseract is not installed. Run: pip install pytesseract")
        return {"error": "OCR library not available on server."}

    try:
        image = Image.open(image_file)
        processed = preprocess_image(image)

        # Run Tesseract OCR with multiple PSM modes for best results
        raw_text = pytesseract.image_to_string(processed, config='--psm 6')
        logger.info(f"OCR Raw Text (PSM 6):\n{raw_text}")

        # Also try PSM 3 (fully automatic) for comparison
        raw_text_auto = pytesseract.image_to_string(processed, config='--psm 3')
        combined_text = raw_text + "\n" + raw_text_auto

        # --- Extract raw fields ---
        university = extract_university(combined_text)
        full_name = extract_name(combined_text)
        reg_no = extract_reg_no(combined_text)
        nic_number = extract_nic_number(combined_text)

        # --- Derive smart fields from Reg No ---
        faculty = derive_faculty(reg_no)
        academic_year = derive_academic_year(reg_no)
        email = derive_email(reg_no, university)

        result = {
            "raw_text": raw_text,
            "extracted": {
                "full_name": full_name,
                "student_id": reg_no,
                "nic_number": nic_number,
                "university": university,
                "faculty": faculty,
                "academic_year": academic_year,
                "email": email,
            }
        }

        logger.info(f"OCR Extraction Result: {result['extracted']}")
        return result

    except Exception as e:
        logger.error(f"OCR processing failed: {e}")
        import traceback
        traceback.print_exc()
        return {"error": f"Failed to process image: {str(e)}"}
