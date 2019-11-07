var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, EventEmitter, TemplateRef, Input, Output, ViewChild, ViewContainerRef } from '@angular/core';
import { ElementExtensions } from '../../../../objects/extensions/element-extensions';
var VirtualPanelComponent = /** @class */ (function () {
    function VirtualPanelComponent(changeDetectorRef, viewContainerRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.viewContainerRef = viewContainerRef;
        this.ScrollTop = 0;
        this.ShowHorizontalScrollbar = false;
        this.ShowVerticalScrollbar = false;
        this.ItemSelected = new EventEmitter();
        this.itemsSource = [];
        this.changeDetectorRef.detach();
        //this.el = viewContainerRef.element.nativeElement;
    }
    VirtualPanelComponent.prototype.ngAfterViewChecked = function () {
        var _this = this;
        setTimeout(function () {
            _this.SizeHorizontalScrollbar();
            _this.SizeVerticalScrollbar();
        }, 0);
    };
    VirtualPanelComponent.prototype.ngDoCheck = function () {
        this.SizeHorizontalScrollbar();
        this.SizeVerticalScrollbar();
    };
    Object.defineProperty(VirtualPanelComponent.prototype, "HighlightedItem", {
        get: function () {
            return this.highlightedItem;
        },
        set: function (value) {
            this.highlightedItem = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(VirtualPanelComponent.prototype, "ItemsSource", {
        get: function () {
            return this.itemsSource;
        },
        set: function (value) {
            if (value === this.itemsSource)
                return;
            this.itemsSource = value;
            this.createCollectionView();
            this.SizeHorizontalScrollbar();
            this.handleVerticalScroll(this.ScrollTop);
        },
        enumerable: true,
        configurable: true
    });
    VirtualPanelComponent.prototype.createCollectionView = function () {
        if (!this.ItemsSource)
            return;
        var items = this.ItemsSource.slice();
        //items = this.getAllItems(items);
        this.calculateRowHeights(items);
        this.Items = items;
    };
    VirtualPanelComponent.prototype.calculateRowHeights = function (items) {
        var totalHeight = 0;
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            item['_top'] = totalHeight;
            if (item['_itemResizeHeight'])
                item['_itemHeight'] = item['_itemResizeHeight'];
            else if (this.CalculateItemSize)
                item['_itemHeight'] = this.CalculateItemSize(item);
            else
                item['_itemHeight'] = parseInt(this.ItemHeight);
            totalHeight += item['_itemHeight'];
        }
        this.HeightPx = totalHeight;
        this.SizeVerticalScrollbar();
    };
    VirtualPanelComponent.prototype.onVerticalScroll = function (event) {
        var currentScrollTop = this.virtualItemContainer.nativeElement.scrollTop = event.target.scrollTop;
        this.handleVerticalScroll(currentScrollTop);
    };
    VirtualPanelComponent.prototype.handleVerticalScroll = function (scrollTop) {
        if (!this.Items)
            return;
        this.ScrollTop = scrollTop;
        var currentViewPortIndex = Math.floor(scrollTop / this.ItemHeight);
        var isPixelHeight = (this.ControlHeight + "").endsWith("px");
        var itemsPerViewPort;
        if (isPixelHeight)
            itemsPerViewPort = (Math.ceil(+this.ControlHeight.substr(0, this.ControlHeight.indexOf("px")) / this.ItemHeight) + 1);
        else
            itemsPerViewPort = (Math.ceil(this.ContainerHeight / this.ItemHeight) + 1);
        this.VisibleItems = this.Items.slice(currentViewPortIndex, currentViewPortIndex + itemsPerViewPort);
        if (isPixelHeight)
            this.ActualControlHeight = (this.Items.length * this.ItemHeight) + "px";
        else
            this.ActualControlHeight = this.ControlHeight;
        this.SizeHorizontalScrollbar();
        this.changeDetectorRef.detectChanges();
    };
    VirtualPanelComponent.prototype.onHorizontalScroll = function (event) {
        var currentScrollLeft = this.virtualItemContainer.nativeElement.scrollLeft = event.target.scrollLeft;
    };
    VirtualPanelComponent.prototype.mouseWheelUp = function (event) {
        if (this.itemScrollbarVerticalContainer)
            this.itemScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
    };
    VirtualPanelComponent.prototype.mouseWheelDown = function (event) {
        if (this.itemScrollbarVerticalContainer)
            this.itemScrollbarVerticalContainer.nativeElement.scrollTop -= event.wheelDelta;
    };
    VirtualPanelComponent.prototype.getItemDisplay = function (item) {
        if (!item)
            return;
        if (!this.DisplayMemberPath)
            return item;
        if (typeof this.DisplayMemberPath === "function")
            return this.DisplayMemberPath(item);
        else if (item[this.DisplayMemberPath])
            return item[this.DisplayMemberPath];
        return item;
    };
    VirtualPanelComponent.prototype.isHighlight = function (item) {
        return this.HighlightedItem == item;
    };
    VirtualPanelComponent.prototype.ScrollToItem = function (item) {
        if (this.itemScrollbarVerticalContainer) {
            if (item['_top'] || item['_top'] === 0) {
                var top = item['_top'];
                this.itemScrollbarVerticalContainer.nativeElement.scrollTop = top;
            }
        }
    };
    VirtualPanelComponent.prototype.SelectItem = function (item) {
        //   this.VisibleItems = this.VisibleItems.slice(); // get new reference of array to force change detection
        this.ItemSelected.emit(item);
        this.changeDetectorRef.detectChanges();
    };
    VirtualPanelComponent.prototype.IsItemSelected = function (item) {
        if (this.SelectedItems && this.SelectedItems.includes(item))
            return this.ItemSelectedClass;
        return;
    };
    VirtualPanelComponent.prototype.GetItemClass = function (item) {
        if (this.LastItemClass && this.VisibleItems[this.VisibleItems.length - 1] == item) {
            return this.LastItemClass;
        }
        return this.ItemClass;
    };
    VirtualPanelComponent.prototype.ResetScroll = function () {
        this.ScrollTop = 0;
        this.handleVerticalScroll(this.ScrollTop);
    };
    VirtualPanelComponent.prototype.SizeVerticalScrollbar = function () {
        if (this.ContainerHeight != ElementExtensions.height(this.virtualItemContainer)) {
            this.ContainerHeight = ElementExtensions.height(this.virtualItemContainer);
            this.ShowVerticalScrollbar = ElementExtensions.scrollHeight(this.virtualItemContainer) > ElementExtensions.height(this.virtualItemContainer);
            if (this.itemScrollbarVerticalContainer)
                this.ScrollTop = this.virtualItemContainer.nativeElement.scrollTop = this.itemScrollbarVerticalContainer.nativeElement.scrollTop;
            this.handleVerticalScroll(this.ScrollTop);
        }
    };
    VirtualPanelComponent.prototype.SizeHorizontalScrollbar = function () {
        if (this.WidthPx != ElementExtensions.scrollWidth(this.virtualItemContainer)) {
            var width = ElementExtensions.width(this.virtualItemContainer);
            if (width <= 0)
                return;
            this.WidthPx = ElementExtensions.scrollWidth(this.virtualItemContainer);
            this.ShowHorizontalScrollbar = this.WidthPx > ElementExtensions.width(this.virtualItemContainer);
        }
    };
    VirtualPanelComponent.prototype.RaiseChange = function () {
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], VirtualPanelComponent.prototype, "HeightPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Function)
    ], VirtualPanelComponent.prototype, "CalculateItemSize", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ItemHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ControlHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], VirtualPanelComponent.prototype, "ItemTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "LastItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], VirtualPanelComponent.prototype, "ShowHighlight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ItemHighlightClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "Items", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], VirtualPanelComponent.prototype, "VisibleItems", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ScrollTop", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ContainerHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "WidthPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "SelectedItems", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "Text", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "ItemSelectedClass", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], VirtualPanelComponent.prototype, "ItemSelected", void 0);
    __decorate([
        ViewChild('virtualItemContainer'),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "virtualItemContainer", void 0);
    __decorate([
        ViewChild('itemScrollbarVerticalContainer'),
        __metadata("design:type", Object)
    ], VirtualPanelComponent.prototype, "itemScrollbarVerticalContainer", void 0);
    __decorate([
        Input('HighlightedItem'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], VirtualPanelComponent.prototype, "HighlightedItem", null);
    __decorate([
        Input('ItemsSource'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], VirtualPanelComponent.prototype, "ItemsSource", null);
    VirtualPanelComponent = __decorate([
        Component({
            selector: 'pm-virtual-panel',
            //templateUrl: './app/controls/components/panels/virtual-panel/virtual-panel.html'
            templateUrl: './virtual-panel.html',
            changeDetection: ChangeDetectionStrategy.OnPush,
            styles: ["\n    :host { \n      display: block;\n      height: 100%;\n    }\n    "],
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef])
    ], VirtualPanelComponent);
    return VirtualPanelComponent;
}());
export { VirtualPanelComponent };
