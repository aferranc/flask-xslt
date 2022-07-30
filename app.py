import lxml.etree as ET
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    with open('datos.xml', 'rb') as file:
        root = ET.fromstring(file.read())
        transform = ET.XSLT(ET.parse('hojaEstilos.xslt'))
        return ET.tostring(transform(root), pretty_print=True)


if __name__ == "__main__":
	app.run()
