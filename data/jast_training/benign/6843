var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, Output, EventEmitter, ViewChild } from '@angular/core';
var ModalComponent = /** @class */ (function () {
    function ModalComponent() {
        this.OnClosed = new EventEmitter();
        this.dragging = false;
    }
    ModalComponent.prototype.ngOnInit = function () {
        this.PreviousHeight = this.HeightPx ? this.HeightPx + "px" : "auto";
        this.PreviousWidth = this.WidthPx ? this.WidthPx + "px" : "auto";
        this.PreviousBodyHeight = this.BodyHeightPx + "px";
        this.PreviousBodyWidth = this.BodyWidthPx + "px";
        this.ResetContainer();
        this.ResetBody();
    };
    ModalComponent.prototype.Show = function () {
        this.ShowModal = true;
    };
    ModalComponent.prototype.Close = function (result) {
        this.OnClosed.emit(result);
        this.ShowModal = false;
    };
    ModalComponent.prototype.Minimize = function () {
        if (this.IsMinimized) {
            this.IsMinimized = false;
            this.Right = this.Bottom = "auto";
            this.Left = this.PreviousLeft;
            this.Top = this.PreviousTop;
            this.Position = "relative";
            this.ResetBody();
            this.ResetContainer();
        }
        else {
            this.IsMinimized = true;
            this.IsMaximized = false;
            this.Bottom = "10px";
            this.PreviousLeft = this.modal.nativeElement.style.left;
            this.PreviousTop = this.modal.nativeElement.style.top;
            this.Top = this.Left = "auto";
            this.Right = "10px";
            this.Position = "absolute";
            this.SetContainer("30px", "200px");
        }
    };
    ModalComponent.prototype.Maximize = function () {
        if (this.IsMaximized) {
            this.IsMaximized = false;
            this.Left = this.PreviousLeft;
            this.Top = this.PreviousTop;
            this.Position = "relative";
            this.ResetBody();
            this.ResetContainer();
        }
        else {
            this.IsMaximized = true;
            this.IsMinimized = false;
            this.PreviousLeft = this.modal.nativeElement.style.left;
            this.PreviousTop = this.modal.nativeElement.style.top;
            this.Top = this.Left = "0px";
            this.Position = "absolute";
            this.SetBody("100%", "100%");
            this.SetContainer("calc(100% - 40px)", "100%");
        }
    };
    ModalComponent.prototype.SetBody = function (height, width) {
        // this.PreviousBodyHeight = this.BodyHeightPx + "px";
        // this.PreviousBodyWidth =  this.BodyWidthPx + "px";
        this.BodyWidth = width;
        this.BodyHeight = height;
    };
    ModalComponent.prototype.ResetBody = function () {
        this.BodyHeight = this.PreviousBodyHeight;
        this.BodyWidth = this.PreviousBodyWidth;
    };
    ModalComponent.prototype.SetContainer = function (height, width) {
        // this.PreviousHeight = this.Height;
        // this.PreviousWidth = this.Width;
        this.Width = width;
        this.Height = height;
    };
    ModalComponent.prototype.ResetContainer = function () {
        this.Height = this.PreviousHeight;
        this.Width = this.PreviousWidth;
    };
    ModalComponent.prototype.OnDoubleClick = function () {
        if (this.IsMaximized)
            this.Maximize();
        else
            this.Minimize();
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ModalComponent.prototype, "BackgroundColor", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ModalComponent.prototype, "ShowModal", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ModalComponent.prototype, "Header", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ModalComponent.prototype, "OnClosed", void 0);
    __decorate([
        ViewChild('modal'),
        __metadata("design:type", Object)
    ], ModalComponent.prototype, "modal", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ModalComponent.prototype, "BodyHeightPx", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ModalComponent.prototype, "BodyWidthPx", void 0);
    ModalComponent = __decorate([
        Component({
            selector: 'pm-modal',
            //templateUrl: './app/controls/components/modal/modal.html',
            templateUrl: './modal.html'
        }),
        __metadata("design:paramtypes", [])
    ], ModalComponent);
    return ModalComponent;
}());
export { ModalComponent };
