eta = getPyeta("""
group Main() {
  role onRun() {
    print('Hello, world!')
    console.writeLine('Note that this does not work with Pyetas Panda3D/PyGame tools.');
   }
}
""")

exec(eta)
