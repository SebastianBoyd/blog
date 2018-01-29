/* globals describe, it, after */
const assert = require('assert')
const path = require('path')
const fs = require('fs')
const methods = require('./node_modules/responsive-images-generator/lib')

const getResponsiveImages = methods.getResponsiveImages
const generateResponsiveImages = methods.generateResponsiveImages
const renameImagesToSize = methods.renameImagesToSize

const imgPath = path.join(__dirname, '/images/full-res/');

const configs = [
    {width: '20%', rename: {suffix: '@1x'}},
    {width: '40%', rename: {suffix: '@2x'}},
    {width: '60%', rename: {suffix: '@3x'}},
    {width: '80%', rename: {suffix: '@4x'}},
    {width: '100%', rename: {suffix: '@5x'}}
]

const contents = imgPath + fs.readdirSync(imgPath).filter((f) => f !== '.DS_Store')
console.log(contents);

const images = [
  path.join(imgPath, 'katsobushi.jpg')
]
console.log(images)

generateResponsiveImages(images, configs);