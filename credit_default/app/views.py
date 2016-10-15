import logging
import json

from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

from . import app, estimator, target_names


logger = logging.getLogger('app')

class PredictForm(Form):
    """Fields for Predict"""
    # sepal_length = fields.DecimalField('Sepal Length:', places=2, validators=[Required()])
    # sepal_width = fields.DecimalField('Sepal Width:', places=2, validators=[Required()])
    # petal_length = fields.DecimalField('Petal Length:', places=2, validators=[Required()])
    # petal_width = fields.DecimalField('Petal Width:', places=2, validators=[Required()])
    Limit_bal = fields.DecimalField('Limit Balance:', places=2, validators=[Required()])
    Gender = fields.DecimalField('Gender:', places=2, validators=[Required()])
    Education = fields.DecimalField('Education:', places=2, validators=[Required()])
    Marriage = fields.DecimalField('Marriage:', places=2, validators=[Required()])
    Age= fields.DecimalField('Age:', places=2, validators=[Required()])
    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    # predicted_iris = None
    predicted_default = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data

        # Retrieve values from form
        # sepal_length = float(submitted_data['sepal_length'])
        # sepal_width = float(submitted_data['sepal_width'])
        # petal_length = float(submitted_data['petal_length'])
        # petal_width = float(submitted_data['petal_width'])
        Limit_bal = float(submitted_data['Limit_bal'])
        Gender = float(submitted_data['Gender'])
        Education = float(submitted_data['Education'])
        Marriage = float(submitted_data['Marriage'])
        Age = float(submitted_data['Age'])

        # Create array from values
        # flower_instance = [sepal_length, sepal_width, petal_length, petal_width]
        default_instance = [Limit_bal, Gender, Education, Marriage, Age]
        # my_prediction = estimator.predict(flower_instance)
        my_prediction = estimator.predict(default_instance)
        # Return only the Predicted iris species
        # predicted_iris = target_names[my_prediction]
        predicted_default = target_names[my_prediction]

    return render_template('index.html',
        form=form,
        # prediction=predicted_iris
        prediction=predicted_default)
