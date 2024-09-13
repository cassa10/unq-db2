# Fake data script

Fake data script to generate fake data in mssql server.

Use https://faker.readthedocs.io/en/master/ as Fake data generator and some python native random methods.

## Requirement

- mssql server 2022 running (maybe works with other versions, but not tested) 
- python 3 installed

libs:
- watch 

## Install script dependencies

Execute this command in the current folder (`./fake-data-script/`)

```bash
pip install -r ./requirements.txt 
```

## Execute script

- Help:
```
py ./src/main.py -h
```

- Example command:
```
py ./src/main.py -s localhost:1433 -n test -u sa -p pass -g 50
```

- With debug mode:
```
py ./src/main.py -p pass -g 50 -d
```