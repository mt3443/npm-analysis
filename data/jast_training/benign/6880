var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
import * as Bowser from 'bowser';
import { Injectable } from '@angular/core';
var CompatibilityService = /** @class */ (function () {
    function CompatibilityService() {
        this.IsLegacyBrowser = Bowser.msie && Bowser.version < 11;
        this.LegacyFlex = this.IsLegacyBrowser ? "legacy-flex" : "";
        this.LegacyFlexElement = this.IsLegacyBrowser ? "legacy-flex-element" : "";
        this.LegacyFlexElementFloatRight = this.IsLegacyBrowser ? "legacy-flex-element legacy-right" : "";
    }
    CompatibilityService.prototype.LegacyCustomClass = function (className) {
        return this.IsLegacyBrowser ? className : "";
    };
    CompatibilityService = __decorate([
        Injectable()
    ], CompatibilityService);
    return CompatibilityService;
}());
export { CompatibilityService };
