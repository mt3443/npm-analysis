var VsForPanel = /** @class */ (function () {
    function VsForPanel(_element, _viewContainer, _templateRef, _renderer, _ngZone, _changeDetectorRef) {
        var _this = this;
        this._element = _element;
        this._viewContainer = _viewContainer;
        this._templateRef = _templateRef;
        this._renderer = _renderer;
        this._ngZone = _ngZone;
        this._changeDetectorRef = _changeDetectorRef;
        this.tagName = 'div';
        this.numOfScreenElements = 6;
        this.currentPage = 0;
        this.previousScrollTop = 0;
        this.currentPageOffset = 0;
        this._originalCollection = [];
        this._slicedCollection = [];
        this.dde = document.documentElement;
        this.matchingFunction = this.dde.matches ? 'matches' :
            this.dde.matchesSelector ? 'matchesSelector' :
                this.dde.webkitMatches ? 'webkitMatches' :
                    this.dde.webkitMatchesSelector ? 'webkitMatchesSelector' :
                        this.dde.msMatches ? 'msMatches' :
                            this.dde.msMatchesSelector ? 'msMatchesSelector' :
                                this.dde.mozMatches ? 'mozMatches' :
                                    this.dde.mozMatchesSelector ? 'mozMatchesSelector' : null;
        var _prevClientSize;
        var reinitOnClientHeightChange = function () {
            if (!_this.scrollParent) {
                return;
            }
            var ch = _this.getViewportSize(_this.scrollParent, _this.clientSizeProp);
            if (ch !== _prevClientSize) {
                _prevClientSize = ch;
                _this._ngZone.run(function () {
                    _this.refresh();
                });
            }
            else {
                _prevClientSize = ch;
            }
        };
        this.onZone = this._ngZone.onStable.subscribe(reinitOnClientHeightChange);
    }
    Object.defineProperty(VsForPanel.prototype, "originalCollection", {
        get: function () {
            return this._originalCollection;
        },
        set: function (value) {
            this._originalCollection = value || [];
            if (this.scrollParent) {
                this.refresh();
            }
            else {
                this.postDigest(this.refresh.bind(this));
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(VsForPanel.prototype, "slicedCollection", {
        get: function () {
            return this._slicedCollection;
        },
        set: function (value) {
            this._slicedCollection = value;
            this.view.context.vsCollection = this._slicedCollection;
        },
        enumerable: true,
        configurable: true
    });
    VsForPanel.prototype.onChanges = function () {
        if (this.scrollParent) {
            this.refresh();
        }
        else {
            this.postDigest(this.refresh.bind(this));
        }
    };
    VsForPanel.prototype.postDigest = function (fn) {
        var subscription = this._ngZone.onStable.subscribe(function () {
            fn();
            subscription.unsubscribe();
        });
    };
    VsForPanel.prototype.init = function (scrollParentClass, itemHeight) {
        var _this = this;
        this.view = this._viewContainer.createEmbeddedView(this._templateRef);
        this.parent = this.nextElementSibling(this._element.nativeElement);
        this.autoSize = true;
        this.clientSizeProp = 'clientHeight'; // this.__horizontal ? 'clientWidth' : ..
        this.offsetSizeProp = 'offsetHeight'; // this.__horizontal ? 'offsetWidth' : 'offsetHeight';
        this.scrollPosProp = 'scrollTop'; //this.__horizontal ? 'scrollLeft' : 'scrollTop';
        this.layoutProp = 'height'; //this.__horizontal ? 'width' : 'height';
        if (scrollParentClass) {
            this.scrollParent = this.closestElement(this.parent, scrollParentClass);
        }
        else {
            this.scrollParent = this.parent;
        }
        this.scrollParent.style['position'] = "relative";
        this.elementSize = itemHeight || 50;
        this.totalSize = 0;
        this.startIndex = 0;
        this.endIndex = 0;
        this.currentPage = 0;
        this.currentPageOffset = 0;
        this.previousScrollTop = 0;
        this.scrollParent.addEventListener('scroll', function () {
            _this.updateInnerCollection();
        });
        this.onWindowResize = function () {
            _this._ngZone.run(function () {
                _this.updateInnerCollection();
            });
        };
        window.addEventListener('resize', this.onWindowResize);
    };
    VsForPanel.prototype.destroy = function () {
        if (this.onWindowResize) {
            window.removeEventListener('resize', this.onWindowResize);
        }
        if (this.onZone) {
            this.onZone.unsubscribe();
        }
    };
    VsForPanel.prototype.refresh = function () {
        if (!this.view)
            return;
        if (!this.originalCollection || this.originalCollection.length < 1) {
            this.slicedCollection = [];
            this.originalLength = 0;
            this.updateTotalSize(0);
        }
        else {
            this.originalLength = this.originalCollection.length;
            this.autoSize = true;
            //this.postDigest(this.setAutoSize.bind(this));
        }
        this.reinitialize();
    };
    VsForPanel.prototype.updateTotalSize = function (size) {
        this.totalSize = size;
        this.numberOfPages = this.getNumberOfPages();
        this.pageCoefficient = this.getPageCoefficient();
        this.pageSize = this.getPageSize();
        this.scrollSize = this.getScrollSize();
    };
    VsForPanel.prototype.reinitialize = function () {
        this._prevStartIndex = void 0;
        this._prevEndIndex = void 0;
        this.updateTotalSize(this.elementSize * this.originalLength);
        this.parent.style[this.layoutProp] = this.scrollSize + "px";
        this.updateInnerCollection();
    };
    //setAutoSize() {
    //   if (this.autoSize) {
    //     let gotSomething = false;
    //   	if (this.parent.offsetHeight || this.parent.offsetWidth) { // element is visible
    //       const child = this.parent.children[0];
    //       if (child && child[this.offsetSizeProp]) {
    //         gotSomething = true;
    //         this.elementSize = child[this.offsetSizeProp];
    //       }
    //     }
    //     if (gotSomething) {
    //       this.autoSize = false;
    //       this._ngZone.run(() => {
    //         this.reinitialize();
    //       });
    //     }
    //   }
    // }
    VsForPanel.prototype.updateInnerCollection = function () {
        var scrollPosition = this.getScrollPos(this.scrollParent, this.scrollPosProp);
        var viewportSize = this.getViewportSize(this.scrollParent, this.clientSizeProp);
        var scrollOffset = this.parent === this.scrollParent ? 0 : this.getScrollOffset(this.parent, this.scrollParent);
        var __startIndex = this.startIndex;
        var __endIndex = this.endIndex;
        this.onScroll(viewportSize);
        var y = this.scrollParent.scrollTop + this.currentPageOffset, buffer = this.elementSize * this.numOfScreenElements, top = Math.floor((y - buffer) / this.elementSize), bottom = Math.ceil((y + viewportSize + buffer) / this.elementSize);
        this.startIndex = Math.max(0, top);
        this.endIndex = Math.min(this.totalSize / this.elementSize, bottom);
        var digestRequired = false;
        if (this._prevStartIndex == null) {
            digestRequired = true;
        }
        else if (this._prevEndIndex == null) {
            digestRequired = true;
        }
        if (!digestRequired) {
            digestRequired = this.startIndex !== this._prevStartIndex ||
                this.endIndex !== this._prevEndIndex;
        }
        if (digestRequired) {
            this.slicedCollection = this.originalCollection.slice(this.startIndex, this.endIndex);
            this._prevStartIndex = this.startIndex;
            this._prevEndIndex = this.endIndex;
            this._changeDetectorRef.markForCheck();
        }
        return digestRequired;
    };
    VsForPanel.prototype.moveItemIntoView = function (item) {
        var index = this.slicedCollection.indexOf(item);
        var itemTop = this.calcTopNum(index);
        if (itemTop < this.scrollParent.scrollTop)
            this.moveItemToTop(index);
        else if (itemTop + this.elementSize > this.getScrollBottom())
            this.moveItemToBottom(index);
    };
    VsForPanel.prototype.moveItemToTop = function (index) {
        this.scrollParent.scrollTop = this.calcTopNum(index);
    };
    VsForPanel.prototype.moveItemToBottom = function (index) {
        this.scrollParent.scrollTop = this.calcTopNum(index) + this.elementSize - this.getViewportSize(this.scrollParent, this.clientSizeProp);
    };
    VsForPanel.prototype.pageForward = function (curScrollTop) {
        this.currentPage++;
        this.currentPageOffset = Math.round(this.currentPage * this.pageCoefficient);
        this.previousScrollTop = curScrollTop - this.pageCoefficient;
        this.scrollParent.scrollTop = this.previousScrollTop;
    };
    VsForPanel.prototype.pageBack = function (curScrollTop) {
        this.currentPage--;
        this.currentPageOffset = Math.round(this.currentPage * this.pageCoefficient);
        this.previousScrollTop = curScrollTop + this.pageCoefficient;
        this.scrollParent.scrollTop = this.previousScrollTop;
    };
    VsForPanel.prototype.onScroll = function (viewportSize) {
        var scrollTop = this.scrollParent.scrollTop;
        if (Math.abs(scrollTop - this.previousScrollTop) > viewportSize) {
            return this.onBigScroll(scrollTop, viewportSize);
        }
        else {
            return this.onSmallScroll(scrollTop);
        }
    };
    VsForPanel.prototype.onSmallScroll = function (scrollTop) {
        if (scrollTop + this.currentPageOffset > (this.currentPage + 1) * this.pageSize) {
            this.pageForward(scrollTop);
        }
        else if (scrollTop + this.currentPageOffset < this.currentPage * this.pageSize) {
            this.pageBack(scrollTop);
        }
        else
            this.previousScrollTop = scrollTop;
        return this.previousScrollTop;
    };
    VsForPanel.prototype.getWindowScroll = function () {
        if ('pageYOffset' in window) {
            return {
                scrollTop: pageYOffset,
                scrollLeft: pageXOffset
            };
        }
        else {
            var sx, sy, d = document, r = d.documentElement, b = d.body;
            sx = r.scrollLeft || b.scrollLeft || 0;
            sy = r.scrollTop || b.scrollTop || 0;
            return {
                scrollTop: sy,
                scrollLeft: sx
            };
        }
    };
    VsForPanel.prototype.getViewportSize = function (element, sizeProp) {
        if (element === window) {
            return sizeProp === 'clientWidth' ? window.innerWidth : window.innerHeight;
        }
        else {
            return element[sizeProp];
        }
    };
    VsForPanel.prototype.getScrollPos = function (element, scrollProp) {
        return element === window ? this.getWindowScroll()[scrollProp] : element[scrollProp];
    };
    VsForPanel.prototype.getScrollOffset = function (vsElement, scrollElement) {
        var vsPos = vsElement.getBoundingClientRect()['top'];
        var scrollPos = scrollElement === window ? 0 : scrollElement.getBoundingClientRect()['top'];
        var correction = vsPos - scrollPos +
            (scrollElement === window ? this.getWindowScroll() : scrollElement)['scrollTop'];
        return correction;
    };
    VsForPanel.prototype.nextElementSibling = function (el) {
        if (el.nextElementSibling) {
            return el.nextElementSibling;
        }
        do {
            el = el.nextSibling;
        } while (el && el.nodeType !== 1);
        return el;
    };
    VsForPanel.prototype.onBigScroll = function (scrollTop, viewportSize) {
        this.currentPage = Math.floor(scrollTop * ((this.totalSize - viewportSize) / (this.scrollSize - viewportSize) * (1 / this.pageSize)));
        this.currentPageOffset = Math.round(this.currentPage * this.pageCoefficient);
        this.previousScrollTop = scrollTop;
        return this.previousScrollTop;
    };
    VsForPanel.prototype.calcTopNum = function (index) {
        return ((index + this.startIndex) * this.elementSize - this.currentPageOffset);
    };
    VsForPanel.prototype.calcTop = function (index) {
        return this.calcTopNum(index) + "px";
    };
    VsForPanel.prototype.getScrollBottom = function () {
        return this.scrollParent.scrollTop + this.getViewportSize(this.scrollParent, this.clientSizeProp);
    };
    VsForPanel.prototype.getScrollSize = function () {
        return Math.min(this.totalSize, VsForPanel.MAX_SCROLL_SIZE);
    };
    VsForPanel.prototype.getPageSize = function () {
        return VsForPanel.MAX_SCROLL_SIZE / 100;
    };
    VsForPanel.prototype.getNumberOfPages = function () {
        return Math.ceil(this.totalSize / this.getPageSize());
    };
    VsForPanel.prototype.getPageCoefficient = function () {
        return this.getNumberOfPages() <= 1 ? 0 : (this.totalSize - this.getScrollSize()) / (this.getNumberOfPages() - 1);
    };
    VsForPanel.prototype.getOffset = function (index) {
        return this.previousScrollTop; // (index + this.startIndex) * this.elementSize + this.vsOffsetBefore;
    };
    VsForPanel.prototype.closestElement = function (el, selector) {
        while (el !== document.documentElement && el != null && !el[this.matchingFunction](selector)) {
            el = el.parentNode;
        }
        if (el && el[this.matchingFunction](selector)) {
            return el;
        }
        else {
            return null;
        }
    };
    VsForPanel.MAX_SCROLL_SIZE = 1300000;
    return VsForPanel;
}());
export { VsForPanel };
