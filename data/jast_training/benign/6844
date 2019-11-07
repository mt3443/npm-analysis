var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Input, Output, EventEmitter } from '@angular/core';
import 'rxjs/add/observable/fromEvent';
import { Observable } from 'rxjs/Observable';
import { KeyCodes } from '../../../objects/key-codes';
var ModalDialog = /** @class */ (function () {
    function ModalDialog() {
        this.CanResize = true;
        this.OnClosed = new EventEmitter();
    }
    ModalDialog.prototype.Close = function (result) { this.OnClosed.emit(result); };
    ModalDialog.prototype.Initialize = function () {
        var that = this;
        this.KeyPress = Observable.fromEvent(document, 'keydown').subscribe(function (e) {
            if (e.keyCode == KeyCodes.ESCAPE)
                that.Close(false);
        });
    };
    ModalDialog.prototype.Destroy = function () {
        this.KeyPress.unsubscribe();
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ModalDialog.prototype, "Header", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ModalDialog.prototype, "CanResize", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ModalDialog.prototype, "OnClosed", void 0);
    return ModalDialog;
}());
export { ModalDialog };
