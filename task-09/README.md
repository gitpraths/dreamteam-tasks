# task_09

Here is the complete code to setup a flask application in your task_09 directory:

cd task_09
python -m venv venv
source venv/bin/activate
pip install flask
touch app.py
You can then run the application and use the curl command to test the API endpoints. For example:

curl -X POST -H "Content-Type: application/json" -d '{"username": "prarthana", "email": "prarthana_desai2004@gmail.com", "password": "password123"}' http://127.0.0.1:5000/register

curl -X POST -H "Content-Type: application/json" -d '{"username": "prarthana", "password": "password123"}' http://127.0.0.1:5000/login

curl -X GET \
 http://127.0.0.1:5000/protected \
 -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMjg3Njg4OSwianRpIjoiNzc4ZWU4MDktNTMxZS00NjQ5LTkxYTUtNzRmMDc0M2ZlMDE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByYXJ0aGFuYSIsIm5iZiI6MTczMjg3Njg4OSwiY3NyZiI6IjE5N2Q3NjBlLTc4MmMtNDJlNS1iMTNiLTE2ZTIyZjE4ZmRlYyIsImV4cCI6MTczMjg3Nzc4OX0.L8Jl_J0-BF94um3HTaUXoRN6FWFoU8PvsoEowwb3azo'
