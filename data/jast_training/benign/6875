var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Directive, HostListener, Input } from '@angular/core';
import { TooltipComponent } from '../../components/tooltips/tooltip-component';
import { setTimeout } from 'core-js/library/web/timers';
var TooltipDirective = /** @class */ (function () {
    function TooltipDirective() {
    }
    TooltipDirective.prototype.mouseMove = function (event) {
        this.x = event.clientX;
        this.y = event.clientY;
    };
    TooltipDirective.prototype.onTooltip = function (event) {
        var _this = this;
        this.stillHover = true;
        this.hoverKey = Math.random();
        setTimeout(function () {
            if (_this.stillHover) {
                //console.log('mouseOver');
                //this.tooltip.DataContext = this.tooltipDataContext;
                //this.tooltip.tooltipTemplate = this.tooltipTemplate;
                _this.tooltip.Show(_this.x, _this.y);
                event.preventDefault();
                event.stopPropagation();
            }
        }, this.tooltip.Delay);
        this.DurationTimer(this.hoverKey);
    };
    TooltipDirective.prototype.DurationTimer = function (localKey) {
        var _this = this;
        setTimeout(function () {
            if (_this.stillHover && localKey == _this.hoverKey)
                _this.tooltip.Hide();
        }, (this.tooltip.Duration + this.tooltip.Delay));
    };
    TooltipDirective.prototype.offTooltip = function (event) {
        this.stillHover = false;
        //console.log('mouseLeave');
        //this.tooltip.DataContext = this.tooltipDataContext;
        //this.tooltip.tooltipTemplate = this.tooltipTemplate;
        this.tooltip.Hide();
    };
    TooltipDirective.prototype.ngOnInit = function () {
        //this.tooltip.Content = this.Content
    };
    __decorate([
        Input(),
        __metadata("design:type", TooltipComponent)
    ], TooltipDirective.prototype, "tooltip", void 0);
    __decorate([
        HostListener('mousemove', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [MouseEvent]),
        __metadata("design:returntype", void 0)
    ], TooltipDirective.prototype, "mouseMove", null);
    __decorate([
        HostListener('mouseover', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [MouseEvent]),
        __metadata("design:returntype", void 0)
    ], TooltipDirective.prototype, "onTooltip", null);
    __decorate([
        HostListener('mouseleave', ['$event']),
        __metadata("design:type", Function),
        __metadata("design:paramtypes", [MouseEvent]),
        __metadata("design:returntype", void 0)
    ], TooltipDirective.prototype, "offTooltip", null);
    TooltipDirective = __decorate([
        Directive({
            selector: '[tooltip]',
        })
    ], TooltipDirective);
    return TooltipDirective;
}());
export { TooltipDirective };
