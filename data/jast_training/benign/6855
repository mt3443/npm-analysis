var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, EventEmitter, Output } from '@angular/core';
var RadioTabsComponent = /** @class */ (function () {
    function RadioTabsComponent() {
        this.tabs = [];
        this.selected = new EventEmitter();
    }
    RadioTabsComponent.prototype.addTab = function (tab) {
        if (this.tabs.length === 0) {
            tab.selected = true;
        }
        this.tabs.push(tab);
    };
    RadioTabsComponent.prototype.selectTab = function (tab) {
        this.tabs.map(function (tab) {
            tab.selected = false;
        });
        tab.selected = true;
        this.selected.emit({ selectedTab: tab });
    };
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], RadioTabsComponent.prototype, "selected", void 0);
    RadioTabsComponent = __decorate([
        Component({
            selector: 'pm-radio-tabs',
            //templateUrl: './app/controls/components/radio/radio-tabs.html',
            templateUrl: './radio-tabs.html'
        })
    ], RadioTabsComponent);
    return RadioTabsComponent;
}());
export { RadioTabsComponent };
