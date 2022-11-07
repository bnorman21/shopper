# shopper
Backend setup
create virtual env in root directory
python3 -m venv env
source env/bin/activate
pip install django djangorestframework


Whenever you make a change to data mode:
python manage.py makemigrations
python manage.py migrate  

To run server:
python manage.py runserver 

Frontend setup 
Make sure you have npm set up 
npm init -y 
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom

To run
frontend % npm run dev
shopper % python manage.py runserver



