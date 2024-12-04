##----------( SETUP / INSTALL )----------## 1.) Extract Code.zip in empty directory 2.) > mkdir data 3.) Extract Data.zip in data directory 4.) cd back to main directory / > cd .. 5.) > virtualenv venv 6.) > source venv/bin/activate 7.) > pip install -r requirements.txt 8.) > pip install whoosh 9.) > pip install flask 10.) > pip install us 11.) > pip install numpy 12.) > flask db init 13.) > flask db upgrade

##----------( RUNNING )----------## 1.) flask --app ./manage.py run --debug
