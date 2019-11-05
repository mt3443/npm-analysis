(function() {
	var Pyramid = function(ele, opt) {
		this.$element = ele
		this.defaultOptions = {
			height: this.$element.height(),
			width: this.$element.width(),
			css: {
				'-webkit-clip-path': 'polygon(50% 0, 0 100%, 100% 100%, 50% 0)',
		    '-moz-clip-path': 'polygon(50% 0, 0 100%, 100% 100%, 50% 0)',
		    'clip-path': 'polygon(50% 0, 0 100%, 100% 100%, 50% 0)',
		    'background': '#ccc'
			}
		}
		this.options = $.extend({}, this.defaultOptions, opt)
	}
	Pyramid.prototype = {
		init: function() {
			this.$element.css(this.options.css)
			this.createFloor(this.getEachFloorHeight(this.options.height, this.options.proportion))
		},
		getEachFloorHeight: function(height, proportion) {
			var totalProportion = proportion.reduce((sum, value) => sum + value);
		  return proportion.map((scale,index) => {
		    //从金字塔顶到底，每算一层，当前梯形高度 = 当前层的三角形高度 - 上层的三角形高度
		    var lastScale = 0;//上层三角形总高度
		    var currentScale = 0;//当前层三角形的总高度
		    for(var i = 0;i <= index;i++) {
		      if(i > 0) lastScale+=proportion[i-1]; //如果是在第一层,index = 0，没有上一层，所以需要判断index > 0的时候才有上一层
		      currentScale+=proportion[i]; //叠加当前层的三角形总高度
		    }
		    //当前层三角形高度 - 上层三角形高度
		    return Math.sqrt(currentScale/totalProportion*Math.pow(height, 2)) - Math.sqrt(lastScale/totalProportion*Math.pow(height, 2));
		  })
		},
		createFloor: function(heights) {
			for(let i = 0;i < heights.length;i++) {
      //插入div
	      this.$element.append($("<div class='pyramid-floor'></div>"))
	      //配置当前div的样式
	      this.$element.find(".pyramid-floor:eq("+i+")").css({
		        'height': heights[i]+'px',
		        'border-bottom': '1px solid #fff'
	        });
	    }
		}
	}
	$.fn.pyramid = function(options) {
	  //计算比例总数 然后通过各数/总数则得到对应比例
	  var pyramid = new Pyramid(this, options)
	  return pyramid.init()
	}
})($)