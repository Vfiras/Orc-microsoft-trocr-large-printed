from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageEnhance, ImageFilter
import google.generativeai as genai
import io
import os

# 🔐 Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# 🧠 Load Gemini model (change to Pro model if you have access)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# 📜 Stronger prompt
prompt = """
You are an OCR system. Your job is to transcribe Arabic handwriting exactly as it appears.

The image contains a sentence written by a child, in informal Arabic handwriting.

Please follow these rules very strictly:
- Return ONLY the original Arabic text, exactly as it is written.
- DO NOT guess or fix characters.
- DO NOT translate, summarize, or interpret.
- If you cannot read a word or letter, wrap it in [brackets] — do not guess.

Your output must be a single Arabic sentence. No explanation. No changes.
"""

# 🌍 Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        # 🖼️ Load image
        image = Image.open(io.BytesIO(request.files['image'].read()))
        image = image.convert("L")  # Grayscale

        # 🧠 Resize if needed
        max_size = 800
        if image.width > max_size or image.height > max_size:
            image.thumbnail((max_size, max_size))

        # ✨ Preprocessing to improve readability
        image = ImageEnhance.Brightness(image).enhance(1.1)
        image = ImageEnhance.Contrast(image).enhance(1.3)
        image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

        # 🔎 (Optional) Save image to inspect if needed
        os.makedirs("debug", exist_ok=True)
        image.save("debug/final_sent_to_gemini.jpg")

        # 🤖 Gemini OCR
        response = model.generate_content([prompt, image])

        return jsonify({
            "recognized_text": response.text.strip()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🚀 Run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)