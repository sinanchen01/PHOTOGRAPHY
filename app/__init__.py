from flask import Flask


app = Flask(__name__)
app.secret_key = "you will never guess"

from app import routes

#-- -----------------------------------------------------
#-- Create Database 
#-- -----------------------------------------------------
#CREATE DATABASE IF NOT EXISTS PHOTOGRAPHY;

#USE PHOTOGRAPHY;
#DROP Table Users;
#-- -----------------------------------------------------
#-- Create Table 
#-- -----------------------------------------------------
#CREATE TABLE IF NOT EXISTS Users
#(
      #id  int	AUTO_INCREMENT,
      #username varchar(200)   NOT NULL,
      #email varchar(200) NOT NULL,
      #password_hash varchar(1000) NOT NULL,
	  #UNIQUE (username),
      #PRIMARY KEY (id)
#);
#-- -----------------------------------------------------
#-- Insert into Table 
#-- -----------------------------------------------------
#INSERT INTO Users(id,username,email,password_hash) 
#VALUES (1,'susan', 'susan@example.com','cat'); 