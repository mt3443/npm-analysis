var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, Component, ElementRef, EventEmitter, Input, Output } from '@angular/core';
var TabsComponent = /** @class */ (function (_super) {
    __extends(TabsComponent, _super);
    function TabsComponent(element, changeDetectorRef) {
        var _this = _super.call(this, element.nativeElement) || this;
        _this.element = element;
        _this.changeDetectorRef = changeDetectorRef;
        _this.Tabs = [];
        _this.SelectedTabIndex = 0;
        _this.SelectedTabIndexChange = new EventEmitter();
        _this.Selected = new EventEmitter();
        _this.TabHeaderHeight = "40";
        return _this;
    }
    TabsComponent.prototype.AddTab = function (tab) {
        this.Tabs.push(tab);
        if (this.Tabs.indexOf(tab) == this.SelectedTabIndex)
            tab.IsSelected = true;
    };
    TabsComponent.prototype.SelectTab = function (tab) {
        this.Tabs.map(function (tab) {
            tab.IsSelected = false;
        });
        tab.IsSelected = true;
        this.Selected.emit({ selectedTab: tab });
        this.SelectedTabIndex = this.Tabs.indexOf(tab);
        this.SelectedTabIndexChange.emit(this.SelectedTabIndex);
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TabsComponent.prototype, "TabsClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], TabsComponent.prototype, "SelectedTabIndex", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], TabsComponent.prototype, "SelectedTabIndexChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], TabsComponent.prototype, "Selected", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TabsComponent.prototype, "TabHeaderHeight", void 0);
    TabsComponent = __decorate([
        Component({
            selector: 'pm-tabs',
            //templateUrl: './app/controls/components/tabs/tabs.html',
            templateUrl: './tabs.html'
        }),
        __metadata("design:paramtypes", [ElementRef,
            ChangeDetectorRef])
    ], TabsComponent);
    return TabsComponent;
}(ElementRef));
export { TabsComponent };
