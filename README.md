# Cribbage Hand Optimizer
This nifty CLI application calculates and chooses your cribbage hand for you!

## Install
In order to install this package, type the following into the command line when at the project's directory:
```console
$ python3 setup.py install --user
```

## Usage
Starting up the application is as simple as:
```console
$ cribbage-opt
```

It will welcome you then ask:
```bash
Welcome to cribbage-optimizer!
Would you like to input a hand (h) or draw randomly (r)?
```

From here you have an option of inputting your own hand or having it draw six cards and do the optimization for you.
### Card input
If you so choose to input your own hand, it must be in the following format:
```bash
AC 5S 6H jD kc 5d
```
There are a couple of requirements:
- Each card (e.g., "5S") must be separated by a space
- The first part is the rank, valid inputs are all face card letters (uppercase or lowercase: e.g., "A" or "a")
- The secoind part is the suit, valid inputs are the first letter of the suits name (D, H, C, S). These can also be lowercase


### Example output

```bash
$ cribbage-opt
Welcome to cribbage-optimizer!
Would you like to input a hand (h) or draw randomly (r)? h
Please input 6 cards: 5d 5H 5C 5s jh kS

The hand you imported: 
        Five of Diamonds
        Five of Hearts
        Five of Clubs
        Five of Spades
        Jack of Hearts
        King of Spades

The following is the optimal chosen hand and crib for the greatest number of guaranteed points

Best hand:
        Five of Diamonds
        Five of Hearts
        Five of Clubs
        Five of Spades
Crib:
        King of Spades
        Jack of Hearts
With a guaranteed number of points of: 16
Would you like to use the optimizer again? (y/n) 
```