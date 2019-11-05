var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, ViewChild, ElementRef, ChangeDetectorRef } from '@angular/core';
var TooltipComponent = /** @class */ (function () {
    function TooltipComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.DEFAULT_TOOLTIP_WIDTH = 200;
        this.targetWidth = 200;
        this.EnableTooltip = true;
        this.Delay = 400; // Default milisecond timeout, used by the directive code.
        this.Duration = 5000; // Default milisecond duration, used by the directive code.
    }
    Object.defineProperty(TooltipComponent.prototype, "Width", {
        get: function () {
            if (this.width === undefined || this.width === null)
                return this.DEFAULT_TOOLTIP_WIDTH;
            else
                return this.width;
        },
        set: function (value) {
            if (value === undefined || value === null)
                this.width = this.DEFAULT_TOOLTIP_WIDTH;
            else
                this.width = value;
            this.targetWidth = value;
        },
        enumerable: true,
        configurable: true
    });
    TooltipComponent.prototype.Show = function (left, top) {
        if (this.Content === undefined || this.Content === null) {
            // There isn't anything to show.
            this.Hide();
            return;
        }
        if (this.EnableTooltip) {
            this.Left = left;
            this.Top = top + 12;
            this.width = this.targetWidth;
            this.ShowTooltip = true;
            this.changeDetectorRef.detectChanges();
            var borderRect = this.TooltipBorder.nativeElement.getBoundingClientRect();
            var textRect = this.TooltipText.nativeElement.getBoundingClientRect();
            if (textRect.width < borderRect.width - 5) {
                this.width = textRect.width + 5;
                this.changeDetectorRef.detectChanges();
            }
            if (window.innerWidth < borderRect.right || window.innerHeight < borderRect.bottom) {
                if (window.innerWidth < borderRect.right) {
                    this.Left = this.Left - borderRect.width;
                }
                if (window.innerHeight < borderRect.bottom) {
                    this.Top = (this.Top - borderRect.height) - 22;
                }
                this.changeDetectorRef.detectChanges();
            }
        }
    };
    TooltipComponent.prototype.Hide = function () {
        this.ShowTooltip = false;
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TooltipComponent.prototype, "Top", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TooltipComponent.prototype, "Left", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TooltipComponent.prototype, "DataContext", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TooltipComponent.prototype, "Content", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], TooltipComponent.prototype, "EnableTooltip", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], TooltipComponent.prototype, "Delay", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], TooltipComponent.prototype, "Duration", void 0);
    __decorate([
        ViewChild('tooltipBorder'),
        __metadata("design:type", ElementRef)
    ], TooltipComponent.prototype, "TooltipBorder", void 0);
    __decorate([
        ViewChild('tooltipText'),
        __metadata("design:type", ElementRef)
    ], TooltipComponent.prototype, "TooltipText", void 0);
    __decorate([
        Input('Width'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], TooltipComponent.prototype, "Width", null);
    TooltipComponent = __decorate([
        Component({
            selector: 'pm-tooltip',
            //templateUrl: './app/controls/components/tooltips/tooltip.html',
            templateUrl: './tooltip.html'
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], TooltipComponent);
    return TooltipComponent;
}());
export { TooltipComponent };
