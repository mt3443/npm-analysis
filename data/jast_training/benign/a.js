const $ = require('jquery')
const highlight = require('highlight.js')
const escape = require('escape-html')
const clipboard = require('clipboard')
require('./precode.js')

const datas = {
  target: 'pre',
  ignore: '.terminal',
  btnSuccessLabel: 'Copied!',
  btnErrorLabel: 'Copy failed...'
}

function showText (elem, string) {
  $(elem)
    .attr('data-balloon', string)
    .on('mouseleave', function () {
      $(this).removeAttr('data-balloon')
    })
}

function setupClipboard () {
  const cb = new clipboard('.precode-btn')
  cb.on('success', function (e) {
    showText(e.trigger, datas.btnSuccessLabel)
  })

  cb.on('error', function (e) {
    showText(e.trigger, datas.btnErrorLabel)
  })
}

function beautify () {
  setupClipboard()
  $(datas.target).precode()

  $(datas.target + ':not(' + datas.ignore + ') > code').each(function (i, block) {
    const doEscape =
      $(this).hasClass('html') ||
      $(this).hasClass('xml') ||
      $(this).hasClass('escape')

    if(doEscape) {
      const html = $(this).html()
      console.log(html)
      const escapeHtml = escape(html)
      $(this).html(escapeHtml)
    }

    highlight.highlightBlock(block)

    const itemID = 'precode-item-' + i
    const headerID = 'precode-header-' + i

    $(this)
      .attr('id', itemID)
      .addClass('precode-item')

    const name = $(this).data('precode-name')
    const parent = $(this).parent()

    parent
      .addClass('precode')
      .before('<div class="precode-header" id="' + headerID + '"></div>')

    if(name !== undefined) {
      parent
        .css({
          'border-top-left-radius': 0
        })

      $('#' + headerID)
        .prepend('<span class="precode-label">' + name + '</span>')
    }

    const copy = $(this).data('precode-copy')

    if(copy != false) {
      $('#' + headerID)
        .append('<button class="precode-btn" data-balloon-pos="up" data-clipboard-target="#' + itemID + '"></button>')
    }
  })
}

module.exports = datas
module.exports.beautify = beautify
