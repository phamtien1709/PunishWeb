from flask import *
import mlab
import random
from models.GetIdea import GetIdea

mlab.connect()

# open xlsx
# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# records = pyexcel.iget_records(file_name="Data1.xlsx")
# sheet = pyexcel.get_sheet(file_name="Data1.xlsx")


#def updata(records):
# for record in records:
#     Idea = record["IDEAS"]
#     ideas_hack = GetIdea(Idea=Idea)
#     ideas_hack.save()
# ideaa = []
# idea_load = GetIdea.objects()
# for idea in idea_load:
#     ideaa.append(idea["Idea"])
# i = random.randint(0, 12)
#
# idea1 = ideaa[i]

image1 = "/static/images/background1.png"
image2 = "/static/images/background.jpg"
image3 = "/static/images/background2.png"
image4 = "/static/images/background3.png"
image5 = "/static/images/background4.png"
image = [image1, image2, image3, image4, image5]
color1 = ["#171a1c", "#4e873d", "#afbfdc"]
color2 = ["#ceeae6", "#291b4f", "#fcd42b"]
color3 = ["#3f2b2c", "#ec3047", "#aca287"]
color4 = ["#590a30", "#90aa3c", "#ef6125"]
color5 = ["#0f2043", "#79cedc", "#d5a458"]
color6 = ["#704f50", "#f0a979", "#f9f0af"]
color7 = ["#561210", "#ef9121", "#f6eb1f"]
color8 = ["#561010", "#ef9121", "#f3ec20"]
color9 = ["#b3b3b3", "#1f1a4f", "#c82027"]
color10 = ["#060809", "#434343", "#ee682a"]
color = [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10]


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    color_ran = color[random.randint(0, len(color)-1)]
    [co1, co2, co3] = [color_ran[0], color_ran[1], color_ran[2]]
    image_random = image[random.randint(0, len(image)-1)]
    text = "**..Anything will be appeared when you push PUNISH..**"
    if request.method == "GET":
        return render_template("index.html", text=text, image_random=image_random, co1=co1, co2=co2, co3=co3)
    elif request.method == "POST":
        text = ""
        ideaa = []
        idea_load = GetIdea.objects()
        for idea in idea_load:
            ideaa.append(idea["Idea"])
        x = random.randint(0, len(ideaa)-1)
        y = random.randint(0, len(ideaa)-1)
        while y == x:
            y = random.randint(0, len(ideaa)-1)
        z = random.randint(0, len(ideaa)-1)
        while z == x or z == y:
            z = random.randint(0, len(ideaa)-1)
        idea1 = ideaa[x]
        idea2 = ideaa[y]
        idea3 = ideaa[z]
        return render_template("index.html", idea1=idea1, idea2=idea2, idea3=idea3, text=text, image_random=image_random, co1=co1, co2=co2, co3=co3)


# @app.route('/test')
# def test():
#     return render_template("test.html")

# @app.route('/images')
# def send_images(path):
#     print(path)
#     return send_from_directory('images', path)

if __name__ == '__main__':
    app.run()
