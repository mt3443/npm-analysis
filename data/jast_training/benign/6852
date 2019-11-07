var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, Input } from '@angular/core';
var PropertiesComponent = /** @class */ (function () {
    function PropertiesComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.changeDetectorRef.detach();
    }
    Object.defineProperty(PropertiesComponent.prototype, "Item", {
        get: function () {
            return this.item;
        },
        set: function (value) {
            this.item = value;
        },
        enumerable: true,
        configurable: true
    });
    PropertiesComponent.prototype.ngOnInit = function () {
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], PropertiesComponent.prototype, "Item", null);
    PropertiesComponent = __decorate([
        Component({
            selector: 'pm-properties',
            //templateUrl: './app/controls/components/properties/properties.html'
            templateUrl: './properties.html',
            changeDetection: ChangeDetectionStrategy.OnPush,
            styles: ["\n    :host { \n      display: block;\n      height: 100%;\n    }\n    "],
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], PropertiesComponent);
    return PropertiesComponent;
}());
export { PropertiesComponent };
