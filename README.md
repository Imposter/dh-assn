# DevHaus Assignment

A simple Fizz-Buzz python program with accompanying tests and docker image.

## How it Works

### Python program

The python program determines whether to print "DevHaus", "Learning", "Model", or certain combinations of the aformentioned strings depending on the integer provided and if it's a multiple of 3, 5, or 7. This is an expanded variant of the typical [Fizz-Buzz](https://en.wikipedia.org/wiki/Fizz_buzz) program.

### Tests

The tests are run during the docker image building process. The unit tests cover all the code paths of the `fizz_buzz` function using the built-in python testing framework. This ensures that the function works as intended. The tests are specified in the `src/tests.py` file.

### Docker Image

The docker image utilizes an Alpine linux base image and expands upon it by installing a Python 3 runtime. It copies the source into the image, runs the python tests and executes a shell script. The shell script runs the python program and waits for 60 seconds before exiting.