# Using github codespace
config codespace for my python project according to doc(Setting up a Python project for GitHub Codespaces).
## problems & fix
here are some records for problem i meet and actions to fix them.
- input ``python -m flask run``, but output shows ``No module named flask``
    - 'flask' module was missing, install it with ``pip install flask``.
- when 'flask' installed, ``python -m flask run`` still not work and output shows ``Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.``
    - i have no 'app.py' as main file in my working dir, create it and it works. [refers to](https://www.cnblogs.com/hailin2018/p/13567714.html)
## doc reference
- [Setting up a Python project for GitHub Codespaces](https://docs.github.com/zh/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)