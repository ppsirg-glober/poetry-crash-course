# poetry crash course

## create new module with poetry

create a module named superlib

`poetry new superlib`

i want my module as simple fastapi app and a client, so im adding fastapi, uvicorn and requests libraries, those are installed and a virtualenv is created to contain installed libraries.

```bash
cd superlib
poetry add fastapi uvicorn requests
```

then i want to see my installed packages with

`poetry show`

now, by default poetry set tests for my module, i can run it with

`poetry run pytest`

now, im adding some code to my new lib, i can write a fastapi app and a client, but i already did it and those .py  files are located on oldproject folder, so:

```bash
scp ../oldproject/*.py superlib
cd superlib
```

now i can run executables such as inside my virtualenv:

`poetry run uvicorn app:app`

or i can open virtualenv shell directly and run code i want.

```bash
poetry shell
python client.py
```



## initialize existent module with poetry

i already have oldproject module, it contains fastapi app and a client, now i want to use poetry on my module, so, i place terminal inside main folder of my existing module and initialize poetry

```bash
cd oldproject
poetry init
```

now i have a wizard that helps me to configure current module, poetry gives me default values and let me override those.

once setup is done, i can install again my libraries with `poetry add fastapi uvicorn requests` and run all code inside with `poetry run` or `poetry shell`.

## final thoughts

poetry value lays on having a strong dependency management shown on `poetry.lock` mapping and locking all dependences between libraries, system requirement and python interpreter and `pyproject.toml` keeping overall project setup related to metadata, OS, libraries and python interpreters.

poetry has `poetry update` that uses all above to update libraries in a safe way to avoid problems with interpeters, OS setup, system dependencies or library compilation, also it makes easier to use tools like docker or make.