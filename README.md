Python CCmS using Flask
=====================

Technologies Used
-------------

> **Back-end**
>> - Python 3.5
>> - Flask framework
>> - SQLAlchemy
>
> **Front-end**
>> - HTML5
>> - CSS3
>
> **Database Engine**
> >- SQLite 3

> **Automated testing**
>> - Selenium



----------------------------------------------------
#### :heavy_exclamation_mark: Prerequsites

Check that you have installed following:

* Python >= 3.5
* [PIP](https://pypi.python.org/pypi)
* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

Optional:
* [Selenium](http://www.seleniumhq.org/)


----------------------------------------------------
#### :information_source: How to run CCmS
Standard mode:
```
python3 main.py
```
Create database from sql file:
```
python3 main.py --init
```
Run with debug mode:
```
python3 main.py --debug
```
In all modes the next step is:    
Open web-browser and navigate to [http://localhost:5000](http://localhost:5000)

----------------------------------
#### Selenium Tests
```
In /tests/ run:
python3 web_tests.py
```
