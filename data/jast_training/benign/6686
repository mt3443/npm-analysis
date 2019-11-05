var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, ElementRef, HostBinding, Input, ViewContainerRef, ViewChild } from '@angular/core';
import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
import { ElementExtensions } from '../../../../objects/extensions/element-extensions';
var DropDownComponent = /** @class */ (function () {
    function DropDownComponent(changeDetectorRef, viewContainerRef, CompatibilityService) {
        this.changeDetectorRef = changeDetectorRef;
        this.viewContainerRef = viewContainerRef;
        this.CompatibilityService = CompatibilityService;
        this.Padding = '1px 0px 0px 0px';
        this.changeDetectorRef.detach();
        this.el = viewContainerRef.element.nativeElement;
        this.scrollEvent = this.HandleScroll.bind(this);
        this.clickEvent = this.HandleClick.bind(this);
        this.resizeEvent = this.HandleResize.bind(this);
    }
    DropDownComponent.prototype.ngOnInit = function () {
        var body = document.querySelector('body');
        body.addEventListener('scroll', this.scrollEvent, true);
        this.el.addEventListener('click', this.clickEvent, false);
        window.addEventListener('resize', this.resizeEvent);
    };
    DropDownComponent.prototype.ngDoCheck = function () {
        this.HandleResize();
    };
    DropDownComponent.prototype.ngOnDestroy = function () {
        var body = document.querySelector('body');
        body.removeEventListener('scroll', this.scrollEvent, true);
        this.el.removeEventListener('click', this.clickEvent, false);
        window.removeEventListener('resize', this.resizeEvent);
    };
    Object.defineProperty(DropDownComponent.prototype, "IsDropDownOpen", {
        get: function () {
            return this.isDropDownOpen;
        },
        set: function (value) {
            if (value && !this.CompatibilityService.IsLegacyBrowser) {
                this.ContainerWidth = this.el.offsetWidth;
                var parentOffsetTop = ElementExtensions.getParentScrollTop(this.el);
                this.ContainerTop = this.el.offsetTop - parentOffsetTop;
                this.changeDetectorRef.detectChanges();
            }
            this.isDropDownOpen = value;
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    DropDownComponent.prototype.HandleScroll = function (e) {
        if (!this.IsDropDownOpen || !e.target) {
            return;
        }
        ;
        var parentOffsetTop = ElementExtensions.getParentScrollTop(this.el);
        this.ContainerTop = this.el.offsetTop - parentOffsetTop;
        this.changeDetectorRef.detectChanges();
    };
    DropDownComponent.prototype.HandleClick = function (e) {
        e.stopPropagation();
    };
    DropDownComponent.prototype.HandleResize = function () {
        if (!this.IsDropDownOpen) {
            return;
        }
        ;
        this.ContainerWidth = this.el.offsetWidth;
        var parentOffsetTop = ElementExtensions.getParentScrollTop(this.el);
        this.ContainerTop = this.el.offsetTop - parentOffsetTop;
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DropDownComponent.prototype, "Width", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DropDownComponent.prototype, "MaxWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DropDownComponent.prototype, "MinWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], DropDownComponent.prototype, "ContainerWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], DropDownComponent.prototype, "ContainerTop", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], DropDownComponent.prototype, "HorizontalAlignment", void 0);
    __decorate([
        HostBinding('style.padding'),
        Input(),
        __metadata("design:type", String)
    ], DropDownComponent.prototype, "Padding", void 0);
    __decorate([
        ViewChild('dropDownPane'),
        __metadata("design:type", ElementRef)
    ], DropDownComponent.prototype, "DropDownPane", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Boolean])
    ], DropDownComponent.prototype, "IsDropDownOpen", null);
    DropDownComponent = __decorate([
        Component({
            selector: 'pm-drop-down',
            //templateUrl: './app/controls/components/base/drop-down/drop-down.html',
            templateUrl: './drop-down.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef,
            CompatibilityService])
    ], DropDownComponent);
    return DropDownComponent;
}());
export { DropDownComponent };
