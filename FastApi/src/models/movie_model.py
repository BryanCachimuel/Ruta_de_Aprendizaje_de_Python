from pydantic import BaseModel, Field, field_validator
import datetime

# Modelo de datos
# Para decir que un atributo es opcional se debe utilizar la librería Optional
# Este Modelo servirá para registrar datos o para consultar datos

class Movie(BaseModel):
      #id: Optional[int] = None
      id: int
      title: str
      overview: str
      year: int
      rating: float
      category: str

# Modelo para el método update
class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str

# Validación de datos, se usa Field para validar y se pode de dos maneras el defaul en cada atributo del Modelo
class MovieCreate(BaseModel):
    id: int
    title: str
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    # para no poner el defaul dentro de los Field
    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'title': 'My Movie',
                'overview': 'Está película trata acerca de ....',
                'year': 2023,
                'rating': 5.2,
                'category': 'Acción'
            }
        }
    }

    @field_validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError('Title field must have a minimun length of 5 chareacters')
        if len(value) > 15:
            raise ValueError('Title field must have a maximun length of 15 chareacters')
        return value