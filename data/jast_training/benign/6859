var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, EventEmitter, Output, ViewChild, ElementRef } from '@angular/core';
import { ElementExtensions } from '../../../objects/extensions/element-extensions';
var SliderComponent = /** @class */ (function () {
    function SliderComponent() {
        this.dragging = false;
        this.DragStart = new EventEmitter();
        this.DragEnd = new EventEmitter();
        this.moveEvent = this.move.bind(this);
        this.dragendEvent = this.dragend.bind(this);
    }
    SliderComponent.prototype.dragstart = function (event) {
        this.DragStart.emit(event);
        document.addEventListener('mousemove', this.moveEvent);
        document.addEventListener('mouseup', this.dragendEvent);
        this.dragging = true;
        if (event.preventDefault)
            event.preventDefault();
        if (event.stopPropagation)
            event.stopPropagation();
    };
    SliderComponent.prototype.dragend = function (event) {
        this.DragEnd.emit(event);
        this.dragging = false;
        document.removeEventListener('mousemove', this.moveEvent, false);
        document.removeEventListener('mouseup', this.dragendEvent, false);
        if (event.preventDefault)
            event.preventDefault();
        if (event.stopPropagation)
            event.stopPropagation();
    };
    SliderComponent.prototype.getOffsetLeft = function (elem) {
        var offsetLeft = 0;
        do {
            if (!isNaN(elem.offsetLeft)) {
                offsetLeft += elem.offsetLeft;
            }
        } while (elem = elem.offsetParent);
        return offsetLeft;
    };
    SliderComponent.prototype.move = function (event) {
        if (!this.dragging)
            return;
        var raw1OffsetLeft = this.getOffsetLeft(this.slidercontainer.nativeElement);
        var maxWidth = ElementExtensions.width(this.slidercontainer);
        console.log("raw1OffsetLeft " + raw1OffsetLeft);
        var offset1 = event.pageX - raw1OffsetLeft;
        if (offset1 < 0) {
            offset1 = 0;
        }
        else if (offset1 > maxWidth) {
            offset1 = maxWidth;
        }
        this.sliderthumb.nativeElement.style['left'] = offset1 + 'px';
        // this.sliderthumb.nativeElement.style['left'] = x + 'px';
        //var pos = this.getRelativePosition(e);
        //var setPos = (this.orientation === 'vertical') ? (this.maxHandlePos - (pos - this.grabPos)) : (pos - this.grabPos);
        //this.setPosition(setPos);
        //value = this.getValueFromPosition(this.cap(pos, 0, this.maxHandlePos));
        //newPos = this.getPositionFromValue(value);
        // if (this.Resizer) {
        //     var size = this.Resizer.resize(event, this.gripperEle);
        //     this.Resize.emit(size);
        // }
        if (event.preventDefault)
            event.preventDefault();
        if (event.stopPropagation)
            event.stopPropagation();
        // event.cancelBubble = true;
        // event.returnValue = false;
        // return false;
    };
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], SliderComponent.prototype, "DragStart", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], SliderComponent.prototype, "DragEnd", void 0);
    __decorate([
        ViewChild('sliderthumb'),
        __metadata("design:type", ElementRef)
    ], SliderComponent.prototype, "sliderthumb", void 0);
    __decorate([
        ViewChild('slidercontainer'),
        __metadata("design:type", ElementRef)
    ], SliderComponent.prototype, "slidercontainer", void 0);
    SliderComponent = __decorate([
        Component({
            selector: 'pm-slider',
            //templateUrl: './app/controls/components/slider/slider.html'
            templateUrl: './slider.html'
        }),
        __metadata("design:paramtypes", [])
    ], SliderComponent);
    return SliderComponent;
}());
export { SliderComponent };
