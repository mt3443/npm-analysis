var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, Output, EventEmitter } from '@angular/core';
var ExpanderComponent = /** @class */ (function () {
    function ExpanderComponent() {
        this.ExpanderClass = "expander-container-default";
        this.CaretAlignment = "Right";
        this.IsExpandedChange = new EventEmitter();
    }
    Object.defineProperty(ExpanderComponent.prototype, "ExpanderHeaderClass", {
        get: function () {
            if (this.CaretAlignment.toLowerCase() == "right")
                return "expander-header";
            return "expander-header expander-header-caret-left";
        },
        enumerable: true,
        configurable: true
    });
    ExpanderComponent.prototype.OnClick = function () {
        this.IsExpanded = !this.IsExpanded;
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ExpanderComponent.prototype, "ExpanderClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ExpanderComponent.prototype, "CaretAlignment", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ExpanderComponent.prototype, "IsExpanded", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ExpanderComponent.prototype, "IsExpandedChange", void 0);
    ExpanderComponent = __decorate([
        Component({
            selector: 'pm-expander',
            //templateUrl: './app/controls/components/expander/expander.html',
            templateUrl: './expander.html'
        })
    ], ExpanderComponent);
    return ExpanderComponent;
}());
export { ExpanderComponent };
