var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, Component, Input } from '@angular/core';
import { TabsComponent } from '../tabs/tabs-component';
var TabComponent = /** @class */ (function () {
    function TabComponent(tabs, changeDetectorRef) {
        this.tabs = tabs;
        this.changeDetectorRef = changeDetectorRef;
    }
    Object.defineProperty(TabComponent.prototype, "IsSelected", {
        get: function () {
            return this.isSelected;
        },
        set: function (value) {
            this.isSelected = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    TabComponent.prototype.ngOnInit = function () {
        this.tabs.AddTab(this);
    };
    Object.defineProperty(TabComponent.prototype, "TabHeaderHeight", {
        get: function () {
            return "calc(100% - " + this.tabs.TabHeaderHeight + "px)";
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TabComponent.prototype, "Name", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TabComponent.prototype, "Height", void 0);
    __decorate([
        Input('IsSelected'),
        __metadata("design:type", Boolean),
        __metadata("design:paramtypes", [Boolean])
    ], TabComponent.prototype, "IsSelected", null);
    TabComponent = __decorate([
        Component({
            selector: 'pm-tab',
            //templateUrl: './app/controls/components/tab/tab.html',
            templateUrl: './tab.html'
        }),
        __metadata("design:paramtypes", [TabsComponent, ChangeDetectorRef])
    ], TabComponent);
    return TabComponent;
}());
export { TabComponent };
