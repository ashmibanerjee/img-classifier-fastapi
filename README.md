# Build your Backend using FastAPI

## Pre-requisites
* Python (3.6+)

## Tutorial
:pushpin: [A 4 Step Tutorial to Serve an ML Model in Production using FastAPI](https://medium.com/@ashmi_banerjee/4-step-tutorial-to-serve-an-ml-model-in-production-using-fastapi-ee62201b3db3)
## Running the Code

1. Clone the project
   * `git clone git@github.com:ashmibanerjee/fastapi-backend.git`
   * `cd fastapi-backend`
2. Create virtual environment
   * `virtualenv venv`
   * `source venv/bin/activate`
3. Install dependencies 
   * `pip3 install -r requirements.txt`
4. Run the server
   * `python3 src/main.py`
5. Server should be running at `http://127.0.0.1:8000/docs`

## Testing the End points

### Running Unit Tests
1. `pytest`

### Running the performance Tests using Locust

1. `locust -f tests/performance-tests/locust_test.py 
`
2. Tests should appear at `http://127.0.0.1:8089/`

## Further Readings

### FastAPI
* [First Steps - FastAPI (tiangolo.com)](https://fastapi.tiangolo.com/tutorial/first-steps/)
* [Serving ML easily with FastAPI (slideshare.net)](https://www.slideshare.net/SebastinRamrezMontao/serving-ml-easily-with-fastapi?from_action=save)
* [Tutorial - User Guide - Intro - FastAPI (tiangolo.com)](https://fastapi.tiangolo.com/tutorial/)
* [FastAPI - The Good, the bad and the ugly. - DEV Community](https://dev.to/fuadrafid/fastapi-the-good-the-bad-and-the-ugly-20ob)
* [An Introduction to Python FastAPI – All About Tech (amalgjose.com)](https://amalgjose.com/2021/02/28/an-introduction-to-python-fastapi/)
* [Build And Host Fast Data Science Applications Using FastAPI | by Farhad Malik | Towards Data Science](https://towardsdatascience.com/build-and-host-fast-data-science-applications-using-fastapi-823be8a1d6a0#:~:text=Netflix%2C%20Uber%2C%20Microsoft%20amongst%20many,on%20standard%20Python%20type%20hints.)
* [For fast and secure sites | Jamstack](https://jamstack.org/)
* [An introduction to the JAMstack: the architecture of the modern web](https://www.freecodecamp.org/news/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca/)

### Testing
* [FastAPI - testing (tiangolo.com)](https://fastapi.tiangolo.com/tutorial/testing/)
* [https://locust.io/](https://locust.io/)
* [Performance testing FastAPI ML APIs with Locust](https://rubikscode.net/2022/03/21/performance-testing-fastapi-ml-apis-with-locust/)