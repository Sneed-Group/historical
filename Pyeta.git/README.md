# Pyeta
## A worse Python3 variant (JK LOL), and the husband project of LowJS.

[***HEY LOWJS, REMEMBER WHEN SANS?***](https://www.youtube.com/embed/Hsf3gQ0b6Ik?controls=0)

Pyeta is a programming language aiming to fix most of my problems with Python, and is a hard fork of CBLang.

Pyeta can be either interpreted, transpiled to python, or compiled into an exe using [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/).

Pyeta can run without any dependencies (including PyInstaller/Panda3D - *you just won't be able to compile your programs or do anything Panda3D related*, but they will run and transpile fine). Also: Panda3D only is currently officially supported via transpiling. TLDR: Compiling Panda3D code is not supported. (For now.)

Pyeta is only tested on macOS, but I'm sure it wouldn't be hard at all to get working on Linux or Windows.

Be warned that everything is basically held together by hopes and dreams, *so you are going to get a load of super random errors*. ***#jokes***

So, how does it work?

## Using the language

```
group Main() {
  role onRun() {
    # A basic "Hello world" program.
    console.writeLine("Hello World");
  }
}
```

## Credits

* NodeMixaholic - creator of the hard fork of cbLang (this project)
* Chadderbox - creator of the original project (cbLang)
* Contributors that are like you. Thank you!
