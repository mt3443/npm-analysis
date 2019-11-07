var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, ChangeDetectorRef, EventEmitter, Input, Output, ViewChild, ViewContainerRef } from '@angular/core';
var ContextMenuComponent = /** @class */ (function () {
    function ContextMenuComponent(changeDetectorRef, viewContainerRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.Open = new EventEmitter();
        this.el = viewContainerRef.element.nativeElement;
        this.clickEvent = this.HandleClick.bind(this);
    }
    Object.defineProperty(ContextMenuComponent.prototype, "IsOpen", {
        get: function () {
            return this.isOpen;
        },
        set: function (value) {
            if (this.isOpen != value) {
                var body = document.querySelector('body');
                if (value) {
                    body.addEventListener('click', this.clickEvent, false);
                    this.Open.emit(true);
                }
                else {
                    body.removeEventListener('click', this.clickEvent, false);
                    this.Open.emit(false);
                }
            }
            this.isOpen = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    ContextMenuComponent.prototype.Show = function (left, top) {
        this.IsOpen = true;
        this.changeDetectorRef.detectChanges();
        var menu = this.ContextMenuContainerElement.nativeElement.getBoundingClientRect();
        if (left + menu.width > window.innerWidth) {
            // Part of the menu is off the right side of the viewable part of the screen.
            // Recalculate a new position for the left side of the menu.
            var viewableWidthOfMenu = window.innerWidth - left;
            var hiddenWidthOfMenu = menu.width - viewableWidthOfMenu;
            var buffer = 50;
            var potentialNewLeft = left - hiddenWidthOfMenu - buffer;
            // Guard against a wide menu and a narrow window that could push the
            // left side of the menu off the left side of the screen.
            this.Left = potentialNewLeft < 0 ? buffer : potentialNewLeft;
            this.changeDetectorRef.detectChanges();
        }
        else {
            this.Left = left;
        }
        this.Top = top;
    };
    ContextMenuComponent.prototype.HandleClick = function (e) {
        if (this.el !== e.target && !this.el.contains(e.target)) {
            this.IsOpen = false;
        }
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ContextMenuComponent.prototype, "ContextMenuTemplate", void 0);
    __decorate([
        ViewChild('ContextMenuContainer'),
        __metadata("design:type", Object)
    ], ContextMenuComponent.prototype, "ContextMenuContainerElement", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Boolean])
    ], ContextMenuComponent.prototype, "IsOpen", null);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ContextMenuComponent.prototype, "Top", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ContextMenuComponent.prototype, "Left", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ContextMenuComponent.prototype, "DataContext", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ContextMenuComponent.prototype, "Open", void 0);
    ContextMenuComponent = __decorate([
        Component({
            selector: 'pm-context-menu',
            //templateUrl: './app/controls/components/context-menu/context-menu.html',
            templateUrl: './context-menu.html'
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef])
    ], ContextMenuComponent);
    return ContextMenuComponent;
}());
export { ContextMenuComponent };
