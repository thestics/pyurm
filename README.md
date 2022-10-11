# Unlimited Registers Machine interpreter

## Goal
Implementation of simple interpreter for [URM](https://proofwiki.org/wiki/Definition:Unlimited_Register_Machine) programs
with minimal UI

## Install
```
git clone git@github.com:thestics/pyurm.git
cd pyurm
python3 -m venv venv
source venv/bin/activate

# to deactivate python venv
deactivate
```

## Run
```pyurm prog1.urm```

## Features
- [x] Core functionality
- [x] File format and syntax definition
- [x] Offline run
- [ ] Support for comments in src
- [ ] REPL

## File format and syntax

- Source file to contain two have extension `.urm` and
to contain two sections named `REGISTERS:` and `PROGRAM:`
- Spaces, newlines and tabs to be ignored
- Comments to be started with `#` symbol
```
# src/program.urm

REGISTERS:
{0: 0, 2: 10, 3: 24}

PROGRAM:
S(1)
S(2)
Z(0)
T(3, 2)
```
