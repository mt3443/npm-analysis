var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
/*
    Incorporated paging as described here:
    http://jsfiddle.net/SDa2B/4/

Visual representation of the approach:

--------
   --------
      --------
         --------
            --------
               --------
                  --------
                     --------
                        --------
                           --------
                              --------
                                 --------
                                    --------
                                       --------
                                          --------

==================================================

[=] - real scrollable height (MAX_SCROLL_SIZE)
[-] - "pages";  total height of all (n) pages is (th) = (ph) * (n)

The overlap between pages is (cj) and is the distance the scrollbar
will jump when we adjust the scroll position during page switch.

To keep things smooth, we need to minimize both (n) and (cj).
Setting (ph) at 1/100 of (h) is a good start.
*/
import { Directive, Input, ViewContainerRef, TemplateRef, ElementRef, Renderer, NgZone, ChangeDetectorRef, } from '@angular/core';
import { VsForPanel } from './vs-for-panel';
var VsFor = /** @class */ (function () {
    function VsFor(_element, _viewContainer, _templateRef, _renderer, _ngZone, _changeDetectorRef) {
        this._element = _element;
        this._viewContainer = _viewContainer;
        this._templateRef = _templateRef;
        this._renderer = _renderer;
        this._ngZone = _ngZone;
        this._changeDetectorRef = _changeDetectorRef;
        this._originalCollection = [];
        var _prevClientSize;
        this.vsForPanel = new VsForPanel(_element, _viewContainer, _templateRef, _renderer, _ngZone, _changeDetectorRef);
    }
    Object.defineProperty(VsFor.prototype, "ItemHeight", {
        get: function () {
            return this.itemHeight;
        },
        set: function (value) {
            this.itemHeight = value;
            //this.virtualPanel.originalCollection = this._originalCollection;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(VsFor.prototype, "originalCollection", {
        get: function () {
            return this._originalCollection;
        },
        set: function (value) {
            this._originalCollection = value || [];
            this.vsForPanel.originalCollection = this._originalCollection;
        },
        enumerable: true,
        configurable: true
    });
    VsFor.prototype.ngOnChanges = function () {
        this.vsForPanel.onChanges();
    };
    VsFor.prototype.ngOnInit = function () {
        this.vsForPanel.init(this.vsScrollParent, this.itemHeight);
        this.vsForPanel.view.context.vsCalcTop = this.calcTop;
        this.vsForPanel.view.context.vsMoveItemIntoView = this.moveItemIntoView.bind(this);
        this.vsForPanel.view.context.vsVirtualPanel = this.vsForPanel;
    };
    VsFor.prototype.ngOnDestroy = function () {
        this.vsForPanel.destroy();
    };
    VsFor.prototype.moveItemIntoView = function (item) {
        this.vsForPanel.moveItemIntoView(item);
    };
    VsFor.prototype.moveItemToTop = function (item) {
        this.vsForPanel.moveItemToTop(item);
    };
    VsFor.prototype.moveItemToBottom = function (item) {
        this.vsForPanel.moveItemToBottom(item);
    };
    VsFor.prototype.calcTop = function (index) {
        return this.virtualVsForPanel.calcTop(index);
    };
    VsFor.MAX_SCROLL_SIZE = 1300000;
    __decorate([
        Input('vsForItemHeight'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], VsFor.prototype, "ItemHeight", null);
    __decorate([
        Input('vsForScrollParent'),
        __metadata("design:type", String)
    ], VsFor.prototype, "vsScrollParent", void 0);
    __decorate([
        Input('vsFor'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], VsFor.prototype, "originalCollection", null);
    VsFor = __decorate([
        Directive({
            selector: '[vsFor]',
        }),
        __metadata("design:paramtypes", [ElementRef,
            ViewContainerRef,
            TemplateRef,
            Renderer,
            NgZone,
            ChangeDetectorRef])
    ], VsFor);
    return VsFor;
}());
export { VsFor };
