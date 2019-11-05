var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, ViewChild, ElementRef, ChangeDetectionStrategy, EventEmitter, Output } from '@angular/core';
import { FlexBasisResizeModel } from './flex-basis-resize-model';
import { FlexGrowResizeModel } from './flex-grow-resize-model';
import { Orientation } from '../../../../objects/enums/orientation';
var ThumbComponent = /** @class */ (function () {
    function ThumbComponent(thumbEle) {
        this.thumbEle = thumbEle;
        this.dragging = false;
        this.ItemOrientation = Orientation.Vertical; // orientation of items around thumb.
        this.ElementLocation = "previous";
        this.FirstElementFlexGrow = ".5";
        this.SecondElementFlexGrow = ".5";
        this.UseDefaultResizeModel = true;
        this.Mode = "Grow";
        this.DragStart = new EventEmitter();
        this.DragEnd = new EventEmitter();
        this.Resize = new EventEmitter();
        this.resizeEvent = this.resize.bind(this);
        this.dragendEvent = this.dragend.bind(this);
    }
    Object.defineProperty(ThumbComponent.prototype, "IsFlexGrow", {
        get: function () {
            if (this.Mode)
                return this.Mode.toLowerCase() == "grow";
            return false;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ThumbComponent.prototype, "IsFlexBasis", {
        get: function () {
            if (this.Mode)
                return this.Mode.toLowerCase() == "basis";
            return false;
        },
        enumerable: true,
        configurable: true
    });
    ThumbComponent.prototype.ngOnInit = function () {
        if (this.IsFlexGrow) {
            var firstEle = this.thumbEle.nativeElement.previousElementSibling;
            if (!firstEle)
                return;
            var secondEle = this.thumbEle.nativeElement.nextElementSibling;
            if (!secondEle)
                return;
            firstEle.style['flex-grow'] = Math.max(0.0, parseFloat(this.FirstElementFlexGrow));
            secondEle.style['flex-grow'] = Math.max(0.0, parseFloat(this.SecondElementFlexGrow));
            this.Resizer = new FlexGrowResizeModel([firstEle], [secondEle], this.isHorizontal());
        }
        else if (this.IsFlexBasis) {
            if (!this.ElementFlexBasis)
                return;
            this.Resizer = new FlexBasisResizeModel(this.ElementFlexBasis, this.isPrevious(), this.isHorizontal());
        }
    };
    ThumbComponent.prototype.useVerticalDefaultClass = function () {
        return (!this.CustomClass || this.CustomClass == "") && !this.isHorizontal();
    };
    ThumbComponent.prototype.useHorizontalDefaultClass = function () {
        return (!this.CustomClass || this.CustomClass == "") && this.isHorizontal();
    };
    ThumbComponent.prototype.isHorizontal = function () {
        return this.ItemOrientation == Orientation.Horizontal;
    };
    ThumbComponent.prototype.isPrevious = function () {
        return this.ElementLocation.toLowerCase() == "previous";
    };
    Object.defineProperty(ThumbComponent.prototype, "ThumbClass", {
        get: function () {
            if (this.CustomClass)
                return;
            return this.useVerticalDefaultClass() ? 'thumb-horizontal-dots' : 'thumb-vertical-dots';
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ThumbComponent.prototype, "GripperClass", {
        get: function () {
            if (this.CustomClass)
                return this.CustomClass;
            return this.useVerticalDefaultClass() ? 'default-thumb-ns' : 'default-thumb-ew';
        },
        enumerable: true,
        configurable: true
    });
    ThumbComponent.prototype.dragstart = function (event) {
        this.DragStart.emit(event);
        document.addEventListener('mousemove', this.resizeEvent);
        document.addEventListener('mouseup', this.dragendEvent);
        this.dragging = true;
        if (event.preventDefault)
            event.preventDefault();
        if (event.stopPropagation)
            event.stopPropagation();
    };
    ThumbComponent.prototype.dragend = function (event) {
        this.DragEnd.emit(event);
        if (this.UseDefaultResizeModel)
            this.resize(event);
        this.dragging = false;
        document.removeEventListener('mousemove', this.resizeEvent, false);
        document.removeEventListener('mouseup', this.dragendEvent, false);
        if (event.preventDefault)
            event.preventDefault();
        if (event.stopPropagation)
            event.stopPropagation();
    };
    ThumbComponent.prototype.resize = function (event) {
        if (!this.dragging)
            return;
        if (this.Resizer) {
            var size = this.Resizer.resize(event, this.gripperEle);
            this.Resize.emit(size);
        }
        if (event.preventDefault)
            event.preventDefault();
        if (event.stopPropagation)
            event.stopPropagation();
        // event.cancelBubble = true;
        // event.returnValue = false;
        // return false;
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ThumbComponent.prototype, "ItemOrientation", void 0);
    __decorate([
        Input(),
        __metadata("design:type", ElementRef)
    ], ThumbComponent.prototype, "ElementFlexBasis", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ThumbComponent.prototype, "ElementLocation", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ThumbComponent.prototype, "FirstElementFlexGrow", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ThumbComponent.prototype, "SecondElementFlexGrow", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ThumbComponent.prototype, "CustomClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ThumbComponent.prototype, "BackgroundClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ThumbComponent.prototype, "UseDefaultResizeModel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ThumbComponent.prototype, "Mode", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ThumbComponent.prototype, "DragStart", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ThumbComponent.prototype, "DragEnd", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ThumbComponent.prototype, "Resize", void 0);
    __decorate([
        ViewChild('gripper'),
        __metadata("design:type", ElementRef)
    ], ThumbComponent.prototype, "gripperEle", void 0);
    ThumbComponent = __decorate([
        Component({
            selector: 'pm-thumb',
            //templateUrl: './app/controls/components/base/thumb/thumb.html',
            templateUrl: './thumb.html',
            changeDetection: ChangeDetectionStrategy.OnPush,
        }),
        __metadata("design:paramtypes", [ElementRef])
    ], ThumbComponent);
    return ThumbComponent;
}());
export { ThumbComponent };
