## Information

See: https://github.com/fastapi/fastapi/discussions/14464

- Python version: 3.12.12
- OS: Ubuntu 22.04
- Good `fastapi` version: 0.123.6
- Bad `fastapi` version: 0.123.7

## Reproduction

1. Create a venv `$ python3 -m venv .venv`
1. Activate venv `$ source .venv/bin/activate`
1. Install requirements for good case `$ pip install -r requirements.good.txt`
1. Run app `$ uvicorn --reload --app-dir . main:app`
1. See no error
1. Stop app
1. Install requirements for bad case `$ pip install -r requirements.bad.txt`
1. Run app `$ uvicorn --reload --app-dir . main:app`
1. See app crashing with `NameError: name 'config' is not defined`
1. Open file `main.py`
1. Comment out line 16 and save the file
1. See app reloading and the error is gone

## Notes

Original repro setup closer to my real application is on branch `example-close-to-real-app`.
