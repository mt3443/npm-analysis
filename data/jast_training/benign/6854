var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input } from '@angular/core';
import { RadioTabsComponent } from '../radio/radio-tabs-component';
var RadioTabComponent = /** @class */ (function () {
    function RadioTabComponent(tabs) {
        this.tabs = tabs;
    }
    RadioTabComponent.prototype.ngOnInit = function () {
        this.tabs.addTab(this);
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], RadioTabComponent.prototype, "Name", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], RadioTabComponent.prototype, "selected", void 0);
    RadioTabComponent = __decorate([
        Component({
            selector: 'pm-radio-tab',
            //templateUrl: './app/controls/components/radio/radio-tab.html'
            templateUrl: './radio-tab.html'
        }),
        __metadata("design:paramtypes", [RadioTabsComponent])
    ], RadioTabComponent);
    return RadioTabComponent;
}());
export { RadioTabComponent };
