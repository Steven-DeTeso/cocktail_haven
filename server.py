from flask_app import app
from flask_app.controllers import users, drinks

if __name__=="__main__":
    app.run(debug=True)

# for any table in our database; create their own models and controllers files. 

# still need to go into the new file folder and pipenv install flask pymysql , this will rewrite the files that are already here. 
