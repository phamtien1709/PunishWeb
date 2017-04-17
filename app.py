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

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    image_random = image[random.randint(0, len(image)-1)]
    text = "**..Anything will be appeared when you push PUNISH..**"
    if request.method == "GET":
        return render_template("index.html", text=text, image_random=image_random)
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
        return render_template("index.html", idea1=idea1, idea2=idea2, idea3=idea3, text=text, image_random=image_random)


# @app.route('/test')
# def test():
#     return render_template("test.html")

# @app.route('/images')
# def send_images(path):
#     print(path)
#     return send_from_directory('images', path)

if __name__ == '__main__':
    app.run()
