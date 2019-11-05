var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, ChangeDetectorRef, ChangeDetectionStrategy, ViewContainerRef } from '@angular/core';
var SidenavComponent = /** @class */ (function () {
    function SidenavComponent(changeDetectorRef, viewContainerRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.viewContainerRef = viewContainerRef;
        this.el = viewContainerRef.element.nativeElement;
        this.changeDetectorRef.detach();
        this.clickEvent = this.HandleClick.bind(this);
    }
    SidenavComponent.prototype.ngOnInit = function () {
        this.changeDetectorRef.detectChanges();
        var body = document.querySelector('body');
        body.addEventListener('click', this.clickEvent, false);
    };
    Object.defineProperty(SidenavComponent.prototype, "IsSidenavOpen", {
        get: function () {
            return this.isSidenavOpen;
        },
        set: function (value) {
            this.isSidenavOpen = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    SidenavComponent.prototype.ToggleSidenav = function () {
        this.IsSidenavOpen = !this.IsSidenavOpen;
    };
    SidenavComponent.prototype.HandleClick = function (e) {
        if (!this.IsSidenavOpen || !e.target) {
            return;
        }
        ;
        if (this.el !== e.target && !this.el.contains(e.target)) {
            this.IsSidenavOpen = false;
            this.changeDetectorRef.detectChanges();
        }
    };
    SidenavComponent.prototype.ngOnDestroy = function () {
        var body = document.querySelector('body');
        body.removeEventListener('click', this.clickEvent, false);
    };
    __decorate([
        Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Boolean])
    ], SidenavComponent.prototype, "IsSidenavOpen", null);
    SidenavComponent = __decorate([
        Component({
            selector: 'pm-sidenav',
            //templateUrl: './app/controls/components/sidenav/sidenav.html',
            templateUrl: './sidenav.html',
            changeDetection: ChangeDetectionStrategy.OnPush
            // styles: [`
            // :host { 
            //     white-space: nowrap;
            //     overflow: hidden;
            //     text-overflow: ellipsis;
            // }
            // `],
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef])
    ], SidenavComponent);
    return SidenavComponent;
}());
export { SidenavComponent };
