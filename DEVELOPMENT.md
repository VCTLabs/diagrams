# Development Guide

## Docker local development setup

You should have docker installed in your system, if not click [here](https://docs.docker.com/get-docker/).

1. Go to diagrams root directory.

2. Build the docker image.

    ```shell
    docker build --tag diagrams:1.0 -f ./docker/dev/Dockerfile .
    ```

3. Create the container, run in background and mount the project source code.

    ```shell
    docker run -d \
    -it \
    --name diagrams \
    --mount type=bind,source="$(pwd)",target=/usr/src/diagrams \
    diagrams:1.0
    ```

4. Run unit tests in the host using the container to confirm that it's working.

    ```shell
    docker exec diagrams python -m unittest tests/*.py -v
    ```

5. Run the bash script `autogen.sh` to test.

    ```shell
    docker exec diagrams ./autogen.sh
    ```

6. If the unit tests and the bash script `autogen.sh` is working correctly, then your system is now ready for development.


## Mac local development setup

To be able to develop and run diagrams locally on you Mac device, you should have [Python](https://www.python.org/downloads/), [Go](https://golang.org/doc/install), and [brew](https://brew.sh/) installed on your system.

1. Go to diagrams root directory.

2. Install poetry, the Python project management package used by diagrams.

    ```shell
    pip install poetry
    ```

3. Install the project's Python dependencies.

    ```shell
    poetry install
    ```

4. Install diagrams binary dependencies.

    ```shell
    brew install imagemagick inkscape black
    go install github.com/mingrammer/round@latest
    # ln -sf ~/go/bin/round ~/.local/bin/round
    ```

5. Run unit tests to confirm that it's working.

    ```shell
    python -m unittest tests/*.py -v
    ```

6. Run the bash script `autogen.sh` to test.

    ```shell
    ./autogen.sh
    ```

7. If the unit tests and the bash script `autogen.sh` is working correctly,
then your system is now ready for development.

## Alternate workflow using Tox

To test with multiple versions of Python (with a single command!) and
different platforms, you can use [Tox](http://pypi.python.org/pyp
i/tox).  In general, each defined tox command will create a Python
virtual environment in the tox working directory under the command name,
eg, for the first command shown below: `.tox/py`.

Installing from OS packages is recommended, however, you can instead
install in a Python virtual environment.  So either use something like:

    $ sudo apt-get install tox  # on Debian/Ubuntu
    $ sudo emerge dev-python/tox  # on Gentoo/Funtoo

or create a virtual environment and activate it, then:

    $ pip install tox

The following command will use your default system Python version to run
tests:

    $ tox -e py

To run tests on multiple versions with coverage, try:

    $ tox -e py38-linux,py39-linux  # for example

(substitute your platform above, eg, macos or windows)

Additional tox env commands:

    $ tox -e dev  # create a dev environment and run `autogen.sh`
    $ tox -e lint  # run pylint analysis
    $ tox -e mypy  # run mypy import/type checking

Note you can use the tox environments just like any other Python venv, eg:

    $ source .tox/dev/bin/activate
