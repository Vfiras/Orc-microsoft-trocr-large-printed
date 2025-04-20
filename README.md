OCR with Gemini - Arabic Handwriting Recognition ✍️🤖
This project is a Flask web application that performs Optical Character Recognition (OCR) on Arabic handwriting using Google's Gemini AI model. It transcribes handwritten Arabic text exactly as it appears, ensuring no characters are guessed or modified. The app processes images, enhances their quality with preprocessing techniques, and uses the Gemini AI model to perform the transcription. 🌟

Features 🌟
Arabic Handwriting OCR: Transcribe handwritten Arabic text from images 📜➡️📝

Image Preprocessing: Automatically improves brightness, contrast, and sharpness for clearer readability 🎨

Generative AI Integration: Powered by Google's Gemini AI for accurate Arabic text transcription 🤖

Flask Web API: A simple HTTP POST API to process images 🌐

Requirements 🛠️
Python 3.6+

Flask

Flask-CORS

Pillow (PIL)

Google Generative AI SDK

Installation 🚀
Clone the repository:

bash
Copy
git clone https://github.com/yourusername/Orc-microsoft-trocr-large-printed.git
cd Orc-microsoft-trocr-large-printed
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set your Gemini API key as an environment variable:

bash
Copy
export GEMINI_API_KEY="your-gemini-api-key"
Run the Flask application:

bash
Copy
python gemihtt.py
The app will be available at: http://localhost:5002 🌍

API Usage 📡
The OCR service exposes a single API endpoint:

POST /ocr: Accepts an image file and returns the recognized Arabic text.

Request Format 💬
URL: http://localhost:5002/ocr

Method: POST

Body: Form-data with an image file attached (key: image).

Example Request (using curl) 🖼️:
bash
Copy
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:5002/ocr
Example Response 📜:
json
Copy
{
  "recognized_text": "أهلاً وسهلاً"
}
Image Preprocessing 🖼️
Before sending the image to the Gemini model, the app performs several preprocessing steps:

Grayscale conversion: Converts the image to grayscale for simplicity 🎨

Resizing: Resizes the image to fit within a maximum size of 800x800 pixels 📐

Enhancement: Adjusts brightness and contrast to improve the readability of handwriting ✨

Sharpening: Applies an unsharp mask filter to enhance fine details 🔍

Error Handling ⚠️
If no image is provided in the request, the API will return a 400 error with the message No image uploaded.

Any other exceptions will result in a 500 error with the exception message.

Debugging 🛠️
If needed, the processed image will be saved in a debug directory (final_sent_to_gemini.jpg) for inspection 🖼️.

License 📝
This project is licensed under the MIT License - see the LICENSE file for details.
