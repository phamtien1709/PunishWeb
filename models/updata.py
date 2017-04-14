import pyexcel
import mlab
from models.GetIdea import GetIdea

mlab.connect()

records = pyexcel.iget_records(file_name="Data1.xlsx")
for record in records:
    Idea = record["IDEAS"]
    idea_for_hack = GetIdea(Idea=Idea)
    idea_for_hack.save()
