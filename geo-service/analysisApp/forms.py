from flask_wtf import FlaskForm
from wtforms import SelectField, TextField, FloatField
class ArenaForm(FlaskForm):
    description = "Use the dropdown to select an arena."
    selections = SelectField('Select an Arena',choices=[])

class AddForm(FlaskForm):
	name = TextField('Arena Name')
	longitude = FloatField('Longitude')
	latitude = FloatField('Latitude')
