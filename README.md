# Foxsay

This is a simple program that generates pictures of a cute fox with a message.

It is like a `cowsay` but without cows! Fox girls are better!

![Fox Image](./assets/fox.png)

## Usage

```sh
$ ./foxsay.py "Hello, Github!"
# Or.
$ python3 ./foxsay.py "Hello, Github!"
# Or call it without text to get a fox's wisdom.
$ ./foxsay.py

# ╭────────────────╮
# │                │
# │ Hello, Github! │
# │                │
# ╰─v──────────────╯
#
#      |\_|\             ,_.=-,_
#   ._.@ @  ,._.-=-.,_.=`   {.-`
#     '-.,_      (   .-,_ _.`
#          'm`m^"-m.G    `
```

## How to add a new wisdom
Just add it into the `WISDOM` (in [./foxsay.py](./foxsay.py) file) and create
a new Pull Request!

``` python
WISDOM = [
    # ...
    "Add your own one! :)",
]
```

---

#### License
[MIT](./LICENSE)

---

With :heart: by [Anastasia Kim (@gingermuffin)](https://github.com/gingermuffin)
