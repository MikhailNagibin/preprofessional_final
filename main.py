import requests
from flask import *
# from our_requests import *
import base64
import io
from forms import *
from PIL import Image


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route('/')
def index():
    img = Image.new('RGB', (300, 300), color=(255, 0, 0))

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template("map_blank.html", img_data=img_base64)

@app.route('/input_link')
def input_link():
    form = InventoryaddForm()
    if request.method == "POST":
        return redirect('/input_link')
    return render_template("input_link.html", form=form, active_page="input_link")


IMAGES = {
    "base_stations": "default-image-6.jpg",
    "station_radii": "default-image-6.jpg",
    "research_stations": "default-image-6.jpg"
}

@app.route('/map_blank', methods=["GET", "POST"])
def map_blank():
    current_image = "default.jpg"

    if request.method == "POST":
        button_clicked = request.form.get("action")
        if button_clicked in IMAGES:
            current_image = IMAGES[button_clicked]

    return render_template("map_blank.html", active_page="map_blank", current_image=current_image)




if __name__ == "__main__":
    # conn = get_db_connection()
    # cur = conn.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)