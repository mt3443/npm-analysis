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
var ListBoxComponent = /** @class */ (function () {
    function ListBoxComponent(changeDetectorRef) {
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
    Object.defineProperty(ListBoxComponent.prototype, "ItemsSource", {
        get: function () {
            return this.itemsSource;
        },
        set: function (value) {
            this.itemsSource = value;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ListBoxComponent.prototype, "SelectedItems", {
        get: function () {
            return this.selectedItems;
        },
        set: function (value) {
            this.selectedItems = value;
        },
        enumerable: true,
        configurable: true
    });
    ListBoxComponent.prototype.ngOnInit = function () {
        this.filterItemSource();
        if (this.SelectedItem)
            this.SelectItem(this.SelectedItem);
        this.changeDetectorRef.detectChanges();
    };
    ListBoxComponent.prototype.ngOnChanges = function (changes) {
        if (changes['ItemsSource']) {
            this.filterItemSource();
        }
    };
    ListBoxComponent.prototype.filterItemSource = function () {
        this.filteredItemSource = this.ItemsSource;
        this.changeDetectorRef.detectChanges();
    };
    ListBoxComponent.prototype.UpdateSelectedItem = function () {
        this.SelectedItem = this.SelectedItems.length > 0 ? this.SelectedItems[0] : null;
        this.SelectedItemChange.emit(this.SelectedItem);
    };
    ListBoxComponent.prototype.isLastItem = function (item) {
        return item === this.filteredItemSource[this.filteredItemSource.length - 1];
    };
    ListBoxComponent.prototype.getItemDisplay = function (item) {
        if (!item)
            return;
        if (!this.DisplayMemberPath)
            return item;
        if (typeof this.DisplayMemberPath === "function")
            return this.DisplayMemberPath(item);
        else
            return item[this.DisplayMemberPath];
    };
    ListBoxComponent.prototype.SelectItem = function (item) {
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
    ListBoxComponent.prototype.removeSelectedItem = function (item) {
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
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "ListBoxClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "ListBoxItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "LastListBoxItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "ListBoxSelectedItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "ListBoxItemBackgroundClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "ListBoxBorderClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], ListBoxComponent.prototype, "ItemHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ListBoxComponent.prototype, "ControlHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ListBoxComponent.prototype, "ControlWidth", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ListBoxComponent.prototype, "SelectedItem", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ListBoxComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], ListBoxComponent.prototype, "ItemTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ListBoxComponent.prototype, "SelectionMode", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ListBoxComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ListBoxComponent.prototype, "SelectedItemChange", void 0);
    __decorate([
        ViewChild('virtualPanel'),
        __metadata("design:type", VirtualPanelComponent)
    ], ListBoxComponent.prototype, "virtualPanel", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ListBoxComponent.prototype, "filteredItemSource", void 0);
    __decorate([
        Input('ItemsSource'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], ListBoxComponent.prototype, "ItemsSource", null);
    __decorate([
        Input('SelectedItems'),
        __metadata("design:type", Array),
        __metadata("design:paramtypes", [Array])
    ], ListBoxComponent.prototype, "SelectedItems", null);
    ListBoxComponent = __decorate([
        Component({
            selector: 'pm-list-box',
            //templateUrl: './app/controls/components/boxes/list-box/list-box.html',
            templateUrl: './list-box.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], ListBoxComponent);
    return ListBoxComponent;
}());
export { ListBoxComponent };
