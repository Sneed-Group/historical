//Note that (so far) the only reason this is async is to allow for other async functions to work.
async function jsBench(func) {
  let preform = performance.now()
  await func()
  preform = performance.now()
  return `Score: ${preform/1000} seconds`
}
