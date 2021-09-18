**Create and Activate Venv**

```
python -m  venv venv

venv/Scripts/activate-->activation command in windows

```

**Start Django Project**

```
django-admin startproject School .

```

**Create Django App**

```
python manage.py startapp classroom

```

**Managing ENV Files**

```
pip install python-decouple

'PASSWORD': config("DATABASE_PASSWORD"),

```

**Running Tests**

```
python manage.py test

```

**Set Up**

```

Comes in very handy in writing Tests for functions that
are replicated across various test cases..

You can even instanticate a class the same way as you
would a property an use it across various testcases

Some of the Setup functions:

(a)Setting up new users
(b)Getting access tokens/logged in users
(c)Setting up timers

```

**Using Mixer**

```
It is a very Important package in autgenerating Models.

pip install mixer

It helps me save so much time, instead of Hardcoding Models,
especially the more complex ones.

Where you want to override default models generated , You
can do as below,

student1 = mixer.blend(Student, average_score=10)


```

**Why Pytest??**

```
Why pytest over the django default test cases??

Configuration
(a)pip install pytest

(b)pip install pytest pytest-django

(c)configuration file called either pytest.ini || setup.cfg
(c)pytest --->running tests


```

**Notes By**

```
Mbugua Caleb

```
