var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Component, Input, Output, EventEmitter, TemplateRef } from '@angular/core';
var TreeComponent = /** @class */ (function () {
    function TreeComponent() {
        this.SelectedItems = [];
        this.SelectionMode = "SelectionMode.Single";
        this.SelectedItemsChange = new EventEmitter();
        this.SelectedItemChange = new EventEmitter();
    }
    TreeComponent.prototype.getItemDisplay = function (item) {
        if (!item)
            return;
        if (!this.DisplayMemberPath)
            return item;
        if (typeof this.DisplayMemberPath === "function")
            return this.DisplayMemberPath(item);
        else if (item[this.DisplayMemberPath])
            return item[this.DisplayMemberPath];
        return item;
    };
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], TreeComponent.prototype, "ItemsSource", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], TreeComponent.prototype, "ItemTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], TreeComponent.prototype, "SelectedItems", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TreeComponent.prototype, "SelectedItem", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TreeComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TreeComponent.prototype, "ChildPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TreeComponent.prototype, "SelectionMode", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TreeComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TreeComponent.prototype, "SelectedItemChange", void 0);
    TreeComponent = __decorate([
        Component({
            selector: 'pm-tree',
            //templateUrl: './app/controls/components/tree/tree.html',
            templateUrl: './tree.html'
        })
    ], TreeComponent);
    return TreeComponent;
}());
export { TreeComponent };
