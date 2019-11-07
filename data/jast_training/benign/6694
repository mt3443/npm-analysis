var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, ChangeDetectionStrategy, Component, Input, Output, EventEmitter, ViewChild, TemplateRef } from '@angular/core';
import { VirtualPanelComponent } from '../../panels/virtual-panel/virtual-panel-component';
var CheckBoxListBoxComponent = /** @class */ (function () {
    function CheckBoxListBoxComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        this.ListBoxClass = "list-box-container-border";
        this.ListBoxItemClass = "list-box-item";
        this.LastListBoxItemClass = "last-list-box-item";
        this.ListBoxSelectedItemClass = "list-box-list-item-selected";
        this.ListBoxBorderClass = "list-box-border";
        this.ItemHeight = 30;
        this.SelectionMode = "SelectionMode.Single";
        this.SelectedItemsChange = new EventEmitter();
        this.SelectedItemChange = new EventEmitter();
        this.itemsSource = [];
        this.selectedItems = [];
        this.changeDetectorRef.detach();
    }
    Object.defineProperty(CheckBoxListBoxComponent.prototype, "ItemsSource", {
        get: function () {
            return this.itemsSource;
        },
        set: function (value) {
            this.itemsSource = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(CheckBoxListBoxComponent.prototype, "SelectedItems", {
        get: function () {
            return this.selectedItems;
        },
        set: function (value) {
            this.selectedItems = value;
        },
        enumerable: true,
        configurable: true
    });
    CheckBoxListBoxComponent.prototype.ngOnInit = function () {
        this.filterItemSource();
        if (this.SelectedItem)
            this.SelectItem(this.SelectedItem);
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxListBoxComponent.prototype.ngOnChanges = function (changes) {
        if (changes['ItemsSource']) {
            this.filterItemSource();
        }
    };
    CheckBoxListBoxComponent.prototype.filterItemSource = function () {
        this.filteredItemSource = this.ItemsSource;
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxListBoxComponent.prototype.UpdateSelectedItem = function () {
        this.SelectedItem = this.SelectedItems.length > 0 ? this.SelectedItems[0] : null;
        this.SelectedItemChange.emit(this.SelectedItem);
    };
    CheckBoxListBoxComponent.prototype.isLastItem = function (item) {
        return item === this.filteredItemSource[this.filteredItemSource.length - 1];
    };
    CheckBoxListBoxComponent.prototype.getItemDisplay = function (item) {
        if (!item)
            return;
        if (!this.DisplayMemberPath)
            return item;
        if (typeof this.DisplayMemberPath === "function")
            return this.DisplayMemberPath(item);
        else
            return item[this.DisplayMemberPath];
    };
    CheckBoxListBoxComponent.prototype.SelectItem = function (item) {
        if (this.SelectionMode == "SelectionMode.Single")
            this.SelectedItems.length = 0;
        // only include unique items.
        if (this.SelectedItems.indexOf(item) == -1)
            this.SelectedItems.push(item);
        else {
            // remove the item if it's already selected
            this.removeSelectedItem(item);
            this.UpdateSelectedItem();
            return;
        }
        this.UpdateSelectedItem();
        this.SelectedItemsChange.emit(this.SelectedItems);
        this.virtualPanel.RaiseChange();
    };
    CheckBoxListBoxComponent.prototype.removeSelectedItem = function (item) {
        var idx = this.SelectedItems.indexOf(item);
        if (idx < 0) {
            console.error("Could not find selected item to remove.");
            console.trace();
            return;
        }
        this.SelectedItems.splice(idx, 1);
        this.UpdateSelectedItem();
        this.SelectedItemsChange.emit(this.SelectedItems);
    };
    CheckBoxListBoxComponent.prototype.IsCheckedChange = function () {
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxListBoxComponent.prototype.IsChecked = function (item) {
        if (this.SelectedItems && this.SelectedItems.includes(item))
            return true;
        return false;
    };
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "ListBoxClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "ListBoxItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "LastListBoxItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "ListBoxSelectedItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "ListBoxItemBackgroundClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "ListBoxBorderClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], CheckBoxListBoxComponent.prototype, "ItemHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxListBoxComponent.prototype, "ControlHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxListBoxComponent.prototype, "ControlWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxListBoxComponent.prototype, "SelectedItem", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxListBoxComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], CheckBoxListBoxComponent.prototype, "ItemTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxListBoxComponent.prototype, "SelectionMode", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], CheckBoxListBoxComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], CheckBoxListBoxComponent.prototype, "SelectedItemChange", void 0);
    __decorate([
        ViewChild('virtualPanel'),
        __metadata("design:type", VirtualPanelComponent)
    ], CheckBoxListBoxComponent.prototype, "virtualPanel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxListBoxComponent.prototype, "filteredItemSource", void 0);
    __decorate([
        Input('ItemsSource'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], CheckBoxListBoxComponent.prototype, "ItemsSource", null);
    __decorate([
        Input('SelectedItems'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], CheckBoxListBoxComponent.prototype, "SelectedItems", null);
    CheckBoxListBoxComponent = __decorate([
        Component({
            selector: 'pm-check-box-list-box',
            //templateUrl: './app/controls/components/boxes/check-box-list-box/check-box-list-box.html',
            templateUrl: './check-box-list-box.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], CheckBoxListBoxComponent);
    return CheckBoxListBoxComponent;
}());
export { CheckBoxListBoxComponent };
