var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
import { Injectable, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/platform-browser';
var ClipboardService = /** @class */ (function () {
    function ClipboardService(document) {
        this.document = document;
    }
    ClipboardService.prototype.Copy = function (text) {
        var textArea = document.createElement("textarea");
        textArea.style.position = 'fixed';
        textArea.style.top = '0px';
        textArea.style.left = '0px';
        textArea.style.width = '2em';
        textArea.style.height = '2em';
        textArea.style.padding = '0px';
        textArea.style.border = 'none';
        textArea.style.outline = 'none';
        textArea.style.boxShadow = 'none';
        textArea.style.background = 'transparent';
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
        }
        catch (err) {
        }
        document.body.removeChild(textArea);
    };
    ClipboardService = __decorate([
        Injectable(),
        __param(0, Inject(DOCUMENT)),
        __metadata("design:paramtypes", [Object])
    ], ClipboardService);
    return ClipboardService;
}());
export { ClipboardService };
