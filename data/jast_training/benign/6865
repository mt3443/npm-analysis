var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Output, EventEmitter } from '@angular/core';
import 'rxjs/add/observable/fromEvent';
import { Observable } from 'rxjs/Observable';
import { KeyCodes } from '../../../objects/key-codes';
var Toast = /** @class */ (function () {
    function Toast() {
        this.OnClosed = new EventEmitter();
    }
    Toast.prototype.Close = function (result) { this.OnClosed.emit(result); };
    Toast.prototype.Initialize = function () {
        var that = this;
        this.KeyPress = Observable.fromEvent(document, 'keydown').subscribe(function (e) {
            if (e.keyCode == KeyCodes.ESCAPE)
                that.Close(false);
        });
    };
    Toast.prototype.Destroy = function () {
        this.KeyPress.unsubscribe();
    };
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], Toast.prototype, "OnClosed", void 0);
    return Toast;
}());
export { Toast };
