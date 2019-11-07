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
var TreeItemComponent = /** @class */ (function () {
    function TreeItemComponent() {
        this.SelectedItems = [];
        this.SelectionMode = "SelectionMode.Single";
        this.SelectedItemsChange = new EventEmitter();
        this.SelectedItemChange = new EventEmitter();
    }
    TreeItemComponent.prototype.OnClick = function (item) {
        item._isExpanded = !item._isExpanded;
        //this.IsExpanded = !this.IsExpanded;
    };
    TreeItemComponent.prototype.HasChildren = function (item) {
        if (!item)
            return false;
        if (!this.ChildPath)
            return false;
        var items = item[this.ChildPath];
        return items && items.length > 0;
    };
    TreeItemComponent.prototype.GetChildren = function (item) {
        if (!item)
            return;
        if (!this.ChildPath)
            return;
        return item[this.ChildPath];
    };
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], TreeItemComponent.prototype, "ItemsSource", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], TreeItemComponent.prototype, "ItemTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], TreeItemComponent.prototype, "SelectedItems", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TreeItemComponent.prototype, "SelectedItem", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TreeItemComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], TreeItemComponent.prototype, "ChildPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], TreeItemComponent.prototype, "SelectionMode", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TreeItemComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], TreeItemComponent.prototype, "SelectedItemChange", void 0);
    TreeItemComponent = __decorate([
        Component({
            selector: 'pm-tree-item',
            //templateUrl: './app/controls/components/tree/tree-item.html',
            templateUrl: './tree-item.html'
        })
    ], TreeItemComponent);
    return TreeItemComponent;
}());
export { TreeItemComponent };
