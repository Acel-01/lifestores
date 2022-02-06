# About 
Developer assessment test for Lifestores

# How to use
- download the github repository using `git clone https://github.com/Acel-01/lifestores.git`
- Activate a virtual environment on your device
- Install dependencies 
  ### On Ubuntu/Mac
  - Run `pipenv shell`
  ### On windows
  - Run `pip install -r requirements.txt` for python 2.x
  - Run `pip3 install -r requirements.txt` for python 3.x
- Follow the instruction here to manually fix a bug for Graphene and Django 4.0+
  `https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding`
- Set up environment Variables
  - Create a .env file with `touch .env`
  - fill it in with the following:
    ```
    export DEBUG=True
    export SECRET_KEY=*your app's secret key*
    export DATABASE_URL=sqlite:///db.sqlite3
    export AWS_S3_ACCESS_KEY_ID=*your AWS s3 bucket access key id*
    export AWS_S3_SECRET_ACCESS_KEY=*your AWS s3 bucket access key*
    export AWS_STORAGE_BUCKET_NAME=*your AWS s3 bucket name*
    ```
- Start the local server with `python manage.py runserver`
- Open `http://127.0.0.1:8000/graphql` in your browser
