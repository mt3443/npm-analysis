var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, EventEmitter, Input, Output, ViewContainerRef } from '@angular/core';
var MenuDropDownButtonComponent = /** @class */ (function () {
    function MenuDropDownButtonComponent(viewContainerRef) {
        this.ButtonClass = "menu-button-button";
        this.ContainerClass = "menu-button-container";
        this.IsDropDownOpenChange = new EventEmitter();
        this.el = viewContainerRef.element.nativeElement;
        this.clickEvent = this.HandleClick.bind(this);
    }
    MenuDropDownButtonComponent.prototype.ngOnInit = function () {
        this.IsDropDownOpen = this.IsDropDownOpen || false;
        var body = document.querySelector('body');
        body.addEventListener('click', this.clickEvent, false);
    };
    MenuDropDownButtonComponent.prototype.ngOnDestroy = function () {
        var body = document.querySelector('body');
        body.removeEventListener('click', this.clickEvent, false);
    };
    MenuDropDownButtonComponent.prototype.HandleClick = function (e) {
        if (!this.IsDropDownOpen || !e.target) {
            return;
        }
        ;
        if (this.el !== e.target && !this.el.contains(e.target)) {
            this.IsDropDownOpen = false;
            this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
        }
    };
    MenuDropDownButtonComponent.prototype.click = function () {
        this.IsDropDownOpen = !this.IsDropDownOpen;
        this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
    };
    MenuDropDownButtonComponent.prototype.mouseenter = function () {
        if (this.IsDropDownOpen)
            return;
        this.IsDropDownOpen = true;
        this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
    };
    MenuDropDownButtonComponent.prototype.mouseleave = function () {
        if (!this.IsDropDownOpen)
            return;
        this.IsDropDownOpen = false;
        this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
    };
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], MenuDropDownButtonComponent.prototype, "IsDropDownOpen", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], MenuDropDownButtonComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MenuDropDownButtonComponent.prototype, "HorizontalAlignment", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MenuDropDownButtonComponent.prototype, "ButtonClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MenuDropDownButtonComponent.prototype, "ContainerClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MenuDropDownButtonComponent.prototype, "DropDownClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], MenuDropDownButtonComponent.prototype, "OpenDropDownOnHover", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], MenuDropDownButtonComponent.prototype, "IsDropDownOpenChange", void 0);
    MenuDropDownButtonComponent = __decorate([
        Component({
            selector: 'pm-menu-drop-down-button',
            //templateUrl: './app/controls/components/menu/menu-drop-down-button/menu-drop-down-button.html',
            templateUrl: './menu-drop-down-button.html'
        }),
        __metadata("design:paramtypes", [ViewContainerRef])
    ], MenuDropDownButtonComponent);
    return MenuDropDownButtonComponent;
}());
export { MenuDropDownButtonComponent };
