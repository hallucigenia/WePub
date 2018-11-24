import sae
from mainapp import app
application = sae.create_wsgi_app(app)

