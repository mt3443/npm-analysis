var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, EventEmitter, Output } from '@angular/core';
import { BreadcrumbPath } from '../../../controls/components/breadcrumb/breadcrumb-path';
var BreadcrumbComponent = /** @class */ (function () {
    function BreadcrumbComponent() {
        this.Click = new EventEmitter();
        this.Items = [];
    }
    Object.defineProperty(BreadcrumbComponent.prototype, "Path", {
        get: function () {
            return this.path;
        },
        set: function (value) {
            this.path = value;
            var paths = this.path.split("/");
            var crumbs = [];
            var fullPath = '';
            for (var i = 0; i < paths.length; i++) {
                var path = paths[i];
                if (!path)
                    continue;
                fullPath += path + "/";
                var breadcrumb = new BreadcrumbPath();
                breadcrumb.FullPath = fullPath;
                breadcrumb.Path = path;
                crumbs.push(breadcrumb);
            }
            this.Items = crumbs;
        },
        enumerable: true,
        configurable: true
    });
    BreadcrumbComponent.prototype.OnLinkClick = function (path) {
        this.Click.emit(path);
    };
    __decorate([
        Output(),
        __metadata("design:type", Object)
    ], BreadcrumbComponent.prototype, "Click", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String),
        __metadata("design:paramtypes", [String])
    ], BreadcrumbComponent.prototype, "Path", null);
    BreadcrumbComponent = __decorate([
        Component({
            selector: 'pm-breadcrumb',
            //templateUrl: './app/controls/components/breadcrumb/breadcrumb.html',
            templateUrl: './breadcrumb.html'
        })
    ], BreadcrumbComponent);
    return BreadcrumbComponent;
}());
export { BreadcrumbComponent };
