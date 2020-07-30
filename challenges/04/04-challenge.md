# What time is it?

## Description

Ask for a date. A date is composed by year, month, day, hour, minute and second. Something like `2020-03-14 23:15:32` could be enough. But it could also be `14-03-2020 23:15:32`, or `23:15:32 14-03-2020`. Whatever you want.

Choose a date & time format, and create your data. **Ask the user for an input according to your format**, but since —everybody knows— the user is a moron, you will need to validate his/her input.

You must think your grandpa/grandma is typing the input. What should I check? These things can happen (among others; let's assume we ask for `YYYY-MM-DD HH:MM:ss`)
- Change `DD` for `MM`
- Time first, date second.
- Put `/` instead of `-`
- 20 instead of 2020
- Forget the seconds
- A cat/dog could type on the keyboard (qwwwwwiwiiiiii22226666666)


This challenge is about validation.

For further information take a look at these references:
- [Chapter 8 - Input validation](https://automatetheboringstuff.com/2e/chapter8/)
- [Most Pythonic way to do input validation](https://stackoverflow.com/questions/20540274/most-pythonic-way-to-do-input-validation)
- [Asking the user for input until they give a valid response](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response)

After the validation process you should return the number of seconds since 1st of Jan., 1970 (a.k.a. [timestamp()](https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp)).


### Input

Ask the user for the input you consider. Validate it. This challenge will be tested by a party of drugged and drunk monkeys.

### Output

Something like:

`Your input is XXXXXXXXXXXXXX. That means we are in the year YYYY, month MM and day D, and today is DAY_OF_THE_WEEK. It's HH:MM and ss seconds. We are XXXXXXXXXXXXXX seconds from 1970.`

## Bonus points for:

- Input validation with a regex (see [re package](https://docs.python.org/3/library/re.html))