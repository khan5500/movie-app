import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io

# 1. ایپ کا مین سیٹ اپ
st.set_page_config(page_title="Imran's Cinematic VIP", page_icon="🎬", layout="centered")

# 2. تھیم سلیکٹر (ایپ کا رنگ بدلنے کے لیے)
with st.sidebar:
    st.markdown("### 🎨 ایپ ڈیزائن")
    تھیم = st.selectbox("تھیم منتخب کریں:", ["نیون گرین (Default)", "گولڈن وی آئی پی", "ڈارک نائٹ"])

# تھیم کے مطابق رنگوں کا انتخاب
if تھیم == "نیون گرین (Default)":
    مین_رنگ = "#00FF66"; بیک_گراؤنڈ = "#0d1117"
elif تھیم == "گولڈن وی آئی پی":
    مین_رنگ = "#FFD700"; بیک_گراؤنڈ = "#1a1a1a"
else:
    مین_رنگ = "#FFFFFF"; بیک_گراؤنڈ = "#000000"

# 3. خوبصورت ڈیزائن (CSS)
st.markdown(f"""
    <style>
    .main {{ background-color: {بیک_گراؤنڈ}; }}
    h1 {{ text-align: center; color: {مین_رنگ}; font-family: 'Arial Black'; text-shadow: 0px 0px 15px {مین_رنگ}; }}
    h3 {{ text-align: center; color: white; }}
    .stButton>button {{
        background-color: {مین_رنگ} !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        height: 55px;
        width: 100%;
        margin-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<h1>🎬 IMRAN'S CINEMATIC 🎬</h1>", unsafe_allow_html=True)
st.markdown("<h3>VIP Multi-Function Studio</h3>", unsafe_allow_html=True)
st.write("---")

# 4. کیمرہ ان پٹ
کیمرہ_فائل = st.camera_input("📸 کیمرہ آن کریں")

if کیمرہ_فائل:
    اصلی_تصویر = Image.open(کیمرہ_فائل)
    st.write("---")
    
    # آپ کی پسند کا بٹن سسٹم (Expanders)
    
    # لسٹ 1: وی آئی پی فلٹرز
    with st.expander("✨ 1. وی آئی پی فلٹرز کی لسٹ"):
        فلٹر = st.radio("کوئی ایک فلٹر چنیں:", ["بغیر فلٹر", "ونٹیج گرین", "سپاہی بلو", "گلوئنگ سکن", "بلیک اینڈ وائٹ"])

    # لسٹ 2: بیک گراؤنڈ اور موڈ ایفیکٹس
    with st.expander("🖼️ 2. بیک گراؤنڈ اور لائٹ ایفیکٹس"):
        موڈ = st.radio("موڈ منتخب کریں:", ["نارمل", "سنیماٹک ڈارک", "برائٹ ڈے", "وارم وائب"])

    # فلٹرز کا لاجک
    فائنل = اصلی_تصویر
    if فلٹر == "ونٹیج گرین":
        r, g, b = فائنل.split(); g = g.point(lambda i: i * 1.2); فائنل = Image.merge('RGB', (r, g, b))
    elif فلٹر == "سپاہی بلو":
        r, g, b = فائنل.split(); b = b.point(lambda i: i * 1.3); فائنل = Image.merge('RGB', (r, g, b))
    elif فلٹر == "گلوئنگ سکن":
        فائنل = ImageEnhance.Brightness(فائنل).enhance(1.3)
    elif فلٹر == "بلیک اینڈ وائٹ":
        فائنل = ImageOps.grayscale(فائنل)

    # موڈ کا لاجک
    if موڈ == "سنیماٹک ڈارک":
        فائنل = ImageEnhance.Brightness(فائنل).enhance(0.7)
    elif موڈ == "برائٹ ڈے":
        فائنل = ImageEnhance.Brightness(فائنل).enhance(1.5)
    elif موڈ == "وارم وائب":
        r, g, b = فائنل.convert('RGB').split(); r = r.point(lambda i: i * 1.2); فائنل = Image.merge('RGB', (r, g, b))

    # فائنل رزلٹ اور سیو بٹن
    st.image(فائنل, caption="✅ آپ کا وی آئی پی رزلٹ تیار ہے", use_column_width=True)
    
    buf = io.BytesIO(); فائنل.convert('RGB').save(buf, format="JPEG")
    st.download_button("📥 تصویر گیلری میں سیو کریں", buf.getvalue(), "Imran_VIP.jpg", "image/jpeg")

st.write("---")
st.success(f"🔥 عمران بھائی، اب 'تھیم'، 'فلٹر' اور 'موڈ' کے بٹن لسٹ کے ساتھ تیار ہیں! 🔥")
