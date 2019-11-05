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
import { Component, ElementRef, HostBinding, Input } from '@angular/core';
import { ElementExtensions } from '../../../objects/extensions/element-extensions';
var SidebarComponent = /** @class */ (function (_super) {
    __extends(SidebarComponent, _super);
    function SidebarComponent(element) {
        var _this = _super.call(this, element.nativeElement) || this;
        _this.element = element;
        _this.FlexBasisPx = 300;
        _this.MinWidthPx = 35;
        return _this;
    }
    SidebarComponent.prototype.ngDoCheck = function () {
        var flexBasis = this.element.nativeElement.style["flex-basis"];
        var size = ElementExtensions.parsePx(flexBasis);
        if (!size)
            return;
        if (this.IsCollapsed && size > this.MinWidthPx) {
            this.IsCollapsed = false;
            return;
        }
        if (!this.IsCollapsed && size < this.MinWidthPx) {
            this.IsCollapsed = true;
            return;
        }
    };
    SidebarComponent.prototype.OnToggleHeader = function () {
        if (this.IsCollapsed) {
            this.element.nativeElement.style["flex-basis"] = this.PreviousFlexBasis;
        }
        else {
            this.PreviousFlexBasis = this.element.nativeElement.style["flex-basis"];
            this.element.nativeElement.style["flex-basis"] = this.MinWidthPx + "px";
        }
        this.IsCollapsed = !this.IsCollapsed;
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], SidebarComponent.prototype, "Header", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], SidebarComponent.prototype, "RibbonHeader", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], SidebarComponent.prototype, "IsCollapsed", void 0);
    __decorate([
        Input(),
        HostBinding('style.flex-basis.px'),
        __metadata("design:type", Object)
    ], SidebarComponent.prototype, "FlexBasisPx", void 0);
    __decorate([
        Input(),
        HostBinding('style.min-width.px'),
        __metadata("design:type", Object)
    ], SidebarComponent.prototype, "MinWidthPx", void 0);
    SidebarComponent = __decorate([
        Component({
            selector: 'pm-sidebar',
            //templateUrl: './app/controls/components/sidebar/sidebar.html',
            templateUrl: './sidebar.html',
            styles: ["\n    :host { \n        white-space: nowrap;\n        overflow: hidden;\n        text-overflow: ellipsis;\n    }\n    "],
        }),
        __metadata("design:paramtypes", [ElementRef])
    ], SidebarComponent);
    return SidebarComponent;
}(ElementRef));
export { SidebarComponent };
