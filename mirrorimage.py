# from PIL import Image
# # Enter the image path 
# Image.open("C:\\Users\\hp\\Pictures\\download.jpg")
# img = Image.open("C:\\Users\\hp\\Pictures\\download.jpg")
# Mirror_image = img.transpose(Image.FLIP_LEFT_RIGHT)
# Mirror_image.save(r'arsh_mirror.png')
# Image.open('arsh_mirror.png')

from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", mirrored_image=None)

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    if file:
        img = Image.open(file)
        mirrored_image = img.transpose(Image.FLIP_LEFT_RIGHT)
        mirrored_image_path = "images/arsh_mirror.png"
        mirrored_image.save(mirrored_image_path)

        return render_template("index.html", mirrored_image=mirrored_image_path)

if __name__ == "__main__":
    app.run(debug=True)
