var glob = require('glob')
var path = require('path')
var config = require('..')
var dir = config.dir
var entries = config.entryFiles
var entry = {}

Object.keys(entries).forEach(function (key) {
  var file = entries[key]
  var root = path.join(dir.abs.src, file.dir.src) // file's root dir
  var absGlob = path.join(root, file.name) // file's absolute name with glob

  glob.sync(absGlob).map(function (fullName) {
    var fileName = path.relative(root, fullName) // file's relative name from files root
    var distName = path.join(file.dir.dist, fileName)
    var ext = path.extname(distName)

    var name = path.format({
      dir: path.dirname(distName),
      name: path.basename(distName, ext),
      ext: 'ext' in file ? file.ext : ext
    })

    entry[name] = fullName
  })
})

module.exports = entry
