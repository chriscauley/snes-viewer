const fs = require('fs')

const lines = ['/* File was autogenerated using client/repack.js */']
const loadStatic = s => JSON.parse(fs.readFileSync('../server/static/'+s))
const toSassMap = obj => JSON.stringify(obj, null, 2).replace("{","(").replace("}",")")

const portal_colors = loadStatic('sm/portal/colors.json')

lines.push(`$portal_colors: ${toSassMap(portal_colors)};`)
fs.writeFileSync('./src/styles/variables.scss', lines.join('\n\n'))