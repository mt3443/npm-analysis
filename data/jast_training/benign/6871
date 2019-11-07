var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Directive, ElementRef, Renderer, Input, HostListener } from '@angular/core';
var Position = /** @class */ (function () {
    function Position(x, y) {
        this.x = x;
        this.y = y;
    }
    return Position;
}());
var DraggableDirective = /** @class */ (function () {
    function DraggableDirective(el, renderer) {
        this.el = el;
        this.renderer = renderer;
        this.allowDrag = true;
        this.moving = false;
        this.orignal = null;
        this.oldZIndex = '';
        this.oldPosition = '';
    }
    Object.defineProperty(DraggableDirective.prototype, "ngDraggable", {
        set: function (setting) {
            if (setting !== undefined && setting !== null && setting !== '') {
                this.allowDrag = !!setting;
                var element = this.handle ? this.handle : this.el.nativeElement;
                if (this.allowDrag) {
                    this.renderer.setElementClass(element, 'ng-draggable', true);
                }
                else {
                    this.renderer.setElementClass(element, 'ng-draggable', false);
                }
            }
        },
        enumerable: true,
        configurable: true
    });
    DraggableDirective.prototype.ngOnInit = function () {
        if (this.allowDrag) {
            var element = this.handle ? this.handle : this.el.nativeElement;
            this.renderer.setElementClass(element, 'ng-draggable', true);
        }
    };
    DraggableDirective.prototype.getPosition = function (x, y) {
        var left = parseInt(this.el.nativeElement.style.left.replace('px', ''));
        var top = parseInt(this.el.nativeElement.style.top.replace('px', ''));
        if (window) {
            left = parseInt(window.getComputedStyle(this.el.nativeElement, null).getPropertyValue("left"));
            top = parseInt(window.getComputedStyle(this.el.nativeElement, null).getPropertyValue("top"));
        }
        return new Position(x - left, y - top);
    };
    DraggableDirective.prototype.moveTo = function (x, y) {
        if (this.orignal) {
            this.renderer.setElementStyle(this.el.nativeElement, 'left', x - this.orignal.x + "px");
            this.renderer.setElementStyle(this.el.nativeElement, 'top', y - this.orignal.y + "px");
        }
    };
    DraggableDirective.prototype.pickUp = function () {
        // get old z-index and position:
        this.oldZIndex = this.el.nativeElement.style.zIndex ? this.el.nativeElement.style.zIndex : '';
        this.oldPosition = this.el.nativeElement.style.position ? this.el.nativeElement.style.position : '';
        if (window) {
            this.oldZIndex = window.getComputedStyle(this.el.nativeElement, null).getPropertyValue("z-index");
            this.oldPosition = window.getComputedStyle(this.el.nativeElement, null).getPropertyValue("position");
        }
        // setup default position:
        var position = 'relative';
        // check if old position is draggable:
        if (this.oldPosition && (this.oldPosition === 'absolute' ||
            this.oldPosition === 'fixed' ||
            this.oldPosition === 'relative')) {
            position = this.oldPosition;
        }
        this.renderer.setElementStyle(this.el.nativeElement, 'position', position);
        this.renderer.setElementStyle(this.el.nativeElement, 'z-index', '99999');
    };
    DraggableDirective.prototype.putBack = function () {
        if (this.oldZIndex) {
            this.renderer.setElementStyle(this.el.nativeElement, 'z-index', this.oldZIndex);
        }
        else {
            this.el.nativeElement.style.removeProperty('z-index');
        }
    };
    // Support Mouse Events:
    DraggableDirective.prototype.onMouseDown = function (event) {
        // 1. skip right click;
        // 2. if handle is set, the element can only be moved by handle
        if (event.button == 2 || (this.handle !== undefined && event.target !== this.handle)) {
            return;
        }
        this.moving = true;
        this.orignal = this.getPosition(event.clientX, event.clientY);
        this.pickUp();
    };
    DraggableDirective.prototype.onMouseUp = function () {
        this.putBack();
        this.moving = false;
    };
    DraggableDirective.prototype.onMouseLeave = function () {
        this.putBack();
        this.moving = false;
    };
    DraggableDirective.prototype.onMouseMove = function (event) {
        if (this.moving && this.allowDrag) {
            this.moveTo(event.clientX, event.clientY);
        }
    };
    __decorate([
        Input(),
        __metadata("design:type", HTMLElement)
    ], DraggableDirective.prototype, "handle", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], DraggableDirective.prototype, "ngDraggable", null);
    __decorate([
        HostListener('mousedown', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [MouseEvent]),
        __metadata("design:returntype", void 0)
    ], DraggableDirective.prototype, "onMouseDown", null);
    __decorate([
        HostListener('document:mouseup'),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", []),
        __metadata("design:returntype", void 0)
    ], DraggableDirective.prototype, "onMouseUp", null);
    __decorate([
        HostListener('document:mouseleave'),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", []),
        __metadata("design:returntype", void 0)
    ], DraggableDirective.prototype, "onMouseLeave", null);
    __decorate([
        HostListener('document:mousemove', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [MouseEvent]),
        __metadata("design:returntype", void 0)
    ], DraggableDirective.prototype, "onMouseMove", null);
    DraggableDirective = __decorate([
        Directive({
            selector: '[ngDraggable]'
        }),
        __metadata("design:paramtypes", [ElementRef, Renderer])
    ], DraggableDirective);
    return DraggableDirective;
}());
export { DraggableDirective };
