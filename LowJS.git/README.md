# LowJS
"Pyeta! There is no Sans! Wake up!"

## What is LowJS?

LowJS provides web support for, and is the wife project of Pyeta. Pyeta, but made for PyScript and the web.

```
index.html:

<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
<script defer src="https://pyscript.net/latest/pyscript.js"></script> 
<py-script src="https://raw.githubusercontent.com/NodeMixaholic/LowJS/main/lowjs.py"></py-script>
<py-script src="main.py"></py-script> 
```

```
main.py (this is where the python part comes in):

eta = getPyeta("""
group Main() {
  role onRun() {
    print('Hello, world!')
    console.writeLine('Note that this does not work with Pyetas Panda3D/PyGame tools.');
   }
}
""")

exec(eta)


```

