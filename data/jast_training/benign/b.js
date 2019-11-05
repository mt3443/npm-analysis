/*!
 * precode.js v1.1.0
 *
 * Copyright 2017 e-JOINT.jp
 * https://ejointjp.github.io/precode.js
 * MIT license
 */

(function (factory) {
  if (typeof module === 'object' && typeof module.exports === 'object') {
    module.exports = factory(require('jquery'), window, document)
  } else {
    factory(jQuery, window, document)
  }
}(function ($, window, document, undefined) {
  'use strict'

  $.fn.precode = function () {
    return this.each(function () {
      var html = $(this).html()
      var children = $(this).children()
      var hasChildren = children.length

      var startBlank = /^\s+/
      var endBlank = /\s+$/
      var blank = /^\s*$/

      //子要素を持っている場合、子要素のhtmlのみを対象とする
      if(hasChildren === 1) {
        html = children.html()
      }

      var lineArray = html.split(/\r\n|\r|\n/)
      var firstLine = lineArray[0]

      //1行目が空白なら配列から削除
      if(firstLine.match(blank)) {
        lineArray.shift()
        firstLine = lineArray[0]
      }

      var lastLine = lineArray[lineArray.length - 1]

      //最後の行が空白なら配列から削除
      if(lastLine.match(blank)) {
        lineArray.pop()
      }

      var trimLineArray = []
      var indent

      $.each(lineArray, function () {
        //空行以外の行の場合、インデントが取得されていなければ取得する
        if(!this.match(blank)) {
          if(indent === undefined) {
            indent = this.match(startBlank)
          }
        }
        var line = this.replace(indent, '')
        trimLineArray.push(line)
      })

      var trimHtml = trimLineArray.join('\n')

      //子要素がある場合、子要素にトリミング後のHTMLを返した後、子要素タグの前後の空白を削除
      if(hasChildren === 1) {
        children.html(trimHtml)

        html = $(this).html()
          .replace(startBlank, '')
          .replace(endBlank, '')

        $(this).html(html)
      } else {
        $(this).html(trimHtml)
      }
    })
  }
}))
