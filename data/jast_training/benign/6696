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
import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
var ComboSelectedItemComponent = /** @class */ (function () {
    function ComboSelectedItemComponent(CompatibilityService) {
        this.CompatibilityService = CompatibilityService;
        this.OnDelete = new EventEmitter();
    }
    ComboSelectedItemComponent.prototype.removeItem = function () {
        this.OnDelete.emit(this.Item);
    };
    ComboSelectedItemComponent.prototype.getItemDisplay = function (item) {
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
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboSelectedItemComponent.prototype, "Item", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboSelectedItemComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboSelectedItemComponent.prototype, "ShowRemoveItem", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ComboSelectedItemComponent.prototype, "OnDelete", void 0);
    ComboSelectedItemComponent = __decorate([
        Component({
            selector: 'pm-combo-selected-item',
            //templateUrl: './app/controls/components/boxes/combo-box/combo-selected-item.html',
            templateUrl: './combo-selected-item.html',
            styles: ["\n  :host { \n    margin-right: 1px;\n    display: inline-block;\n    max-height:80px;\n    white-space: normal;\n  }\n  "],
        }),
        __metadata("design:paramtypes", [CompatibilityService])
    ], ComboSelectedItemComponent);
    return ComboSelectedItemComponent;
}());
export { ComboSelectedItemComponent };
