from distutils.log import debug
from website._init_ import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug= True)
    