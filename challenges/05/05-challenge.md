# Typing your id

## Description

There are –at least– 3 identification numbers in Spain:
- DNI (locals): 12345678X
- NIE (foreigners): X1234567-P
- CIF (companies): A1234567-L

Each one follows different formats and conventions. For example, not any combination of eight digits + a letter can build a DNI. This is the same for NIE and CIF; each one follows their own rules.

In this challenge you must ask the user for an id and he/she will enter one of his/her choice. Your task is to:
1. Discover which type of id the user has entered (between DNI, NIE and CIF).
2. Validate if it is correct or not (according to each id algorithm).

You must also validate the input, so for example inputs with or without slashes are valid (i.e.: 12345678X == 12345678-X).

### Input

- Ask the user por his/her input.

### Output

Something like:
- Your id belongs to the [DNI/NIE/CIF] category.
- Your id [is/is] not valid.

## Bonus points for:

- Store user's input on a .txt file. You can use one file for the correct ones, and another one for the not valid.
- If you enter a special key combination, files content is deleted.