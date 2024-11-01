# Function API Client Demo with Python
This demo is to illustrate how to install and leverage Function's API client using Python.

## Setup

Make sure you have at least Python 3.7 installed.

First, create a virtualenv and activate it.

<details>
<summary>macOS and Linux</summary>

```shell
python -m venv venv
source venv/bin/activate
```
</details>

<details>
<summary>Windows</summary>

```shell
python -m venv venv
venv\Scripts\activate
```
</details>

Next, add the Buf registry to pull Function's typed API client:

<details>
<summary>macOS and Linux</summary>

```shell
printf "
[global]
extra-index-url = https://buf.build/gen/python
" > venv/pip.conf
```
</details>

<details>
<summary>Windows</summary>

Create a new file in your `venv` directory named `pip.conf` and add the following:

```shell
[global]
extra-index-url = https://buf.build/gen/python
```
</details>

Finally, install dependencies:

```shell
pip install -r requirements.txt
```

## Run Demo

Copy the `env.example` file to `.env` and fill in your Function API key.

Once you have done that, you can run the demo:

```shell
python demo.py
```

## Source Code

See the [demo.py](demo.py) file for the source code.
