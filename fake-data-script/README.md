# Fake data script

Fake data script to generate fake data in mssql server

## Requirement

- mssql server 2022 (maybe works with other versions, but not tested) 

## Install script dependencies

Execute this command in the current folder (`./fake-data-script/`)

```bash
pip install -r ./requirements.txt 
```

## Execute script

- Help:
```
py ./main.py -h
```

- Example command:
```
py ./main.py -s localhost:1433 -n test -u sa -p pass
```

- With debug mode:
```
py ./main.py -p pass -d
```