"""
Cit Categorias, formularios
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CitCategoriaForm(FlaskForm):
    """Formulario CitCategoria"""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
    guardar = SubmitField("Guardar")
