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
import { TextBoxComponent } from '../text-box/text-box-component';
import { KeyCodes } from '../../../../objects/key-codes';
var MultiSelectTextBoxComponent = /** @class */ (function () {
    function MultiSelectTextBoxComponent() {
        this.SelectedItems = [];
        this.SelectedItemsChange = new EventEmitter();
        this.ShowRemoveItem = true;
        this.MultiSelectTextBoxClass = "text-box-input";
        this.MultiSelectTextBoxButtonClass = "button-icon-default";
        this.MultiSelectTextBoxSelectedItemsClass = "multi-select-text-box-selected-items";
    }
    MultiSelectTextBoxComponent.prototype.AddClick = function () {
        if (this.Text) {
            this.SelectedItems.push(this.Text);
            this.Text = undefined;
        }
    };
    MultiSelectTextBoxComponent.prototype.RemoveSelectedItem = function (item) {
        var idx = this.SelectedItems.indexOf(item);
        if (idx < 0) {
            console.error("Could not find selected item to remove.");
            console.trace();
            return;
        }
        this.SelectedItems.splice(idx, 1);
        this.SelectedItemsChange.emit(this.SelectedItems);
        this.textBox.Focus();
    };
    MultiSelectTextBoxComponent.prototype.OnKeyUp = function (event) {
        if (event.keyCode == KeyCodes.ENTER) {
            if (this.Text) {
                this.SelectedItems.push(this.Text);
                this.Text = undefined;
            }
        }
    };
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], MultiSelectTextBoxComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MultiSelectTextBoxComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MultiSelectTextBoxComponent.prototype, "Text", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], MultiSelectTextBoxComponent.prototype, "SelectedItems", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], MultiSelectTextBoxComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], MultiSelectTextBoxComponent.prototype, "ShowRemoveItem", void 0);
    __decorate([
        ViewChild(TextBoxComponent),
        __metadata("design:type", TextBoxComponent)
    ], MultiSelectTextBoxComponent.prototype, "textBox", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MultiSelectTextBoxComponent.prototype, "MultiSelectTextBoxClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MultiSelectTextBoxComponent.prototype, "MultiSelectTextBoxButtonClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], MultiSelectTextBoxComponent.prototype, "MultiSelectTextBoxSelectedItemsClass", void 0);
    MultiSelectTextBoxComponent = __decorate([
        Component({
            selector: 'pm-multi-select-text-box',
            //templateUrl: './app/controls/components/boxes/multi-select-text/multi-select-text-box.html',
            templateUrl: './multi-select-text-box.html',
        })
    ], MultiSelectTextBoxComponent);
    return MultiSelectTextBoxComponent;
}());
export { MultiSelectTextBoxComponent };
