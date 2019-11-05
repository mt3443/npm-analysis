var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Directive, Output, HostListener, EventEmitter } from '@angular/core';
var MouseWheelDirective = /** @class */ (function () {
    function MouseWheelDirective() {
        this.mouseWheelUp = new EventEmitter();
        this.mouseWheelDown = new EventEmitter();
    }
    MouseWheelDirective.prototype.onMouseWheelChrome = function (event) {
        this.mouseWheelFunc(event);
    };
    MouseWheelDirective.prototype.onMouseWheelFirefox = function (event) {
        this.mouseWheelFunc(event);
    };
    MouseWheelDirective.prototype.onMouseWheelIE = function (event) {
        this.mouseWheelFunc(event);
    };
    MouseWheelDirective.prototype.mouseWheelFunc = function (event) {
        var event = window.event || event; // old IE support
        var delta = Math.max(-1, Math.min(1, (event.wheelDelta || -event.detail)));
        if (delta > 0) {
            this.mouseWheelUp.emit(event);
        }
        else if (delta < 0) {
            this.mouseWheelDown.emit(event);
        }
        // for IE
        event.returnValue = false;
        // for Chrome and Firefox
        if (event.preventDefault) {
            event.preventDefault();
        }
    };
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], MouseWheelDirective.prototype, "mouseWheelUp", void 0);
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], MouseWheelDirective.prototype, "mouseWheelDown", void 0);
    __decorate([
        HostListener('mousewheel', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [Object]),
        __metadata("design:returntype", void 0)
    ], MouseWheelDirective.prototype, "onMouseWheelChrome", null);
    __decorate([
        HostListener('DOMMouseScroll', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [Object]),
        __metadata("design:returntype", void 0)
    ], MouseWheelDirective.prototype, "onMouseWheelFirefox", null);
    __decorate([
        HostListener('onmousewheel', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [Object]),
        __metadata("design:returntype", void 0)
    ], MouseWheelDirective.prototype, "onMouseWheelIE", null);
    MouseWheelDirective = __decorate([
        Directive({
            selector: '[mouseWheel]'
        })
    ], MouseWheelDirective);
    return MouseWheelDirective;
}());
export { MouseWheelDirective };
