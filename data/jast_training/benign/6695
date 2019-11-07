var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, EventEmitter, Input, Output, TemplateRef, ViewContainerRef, ViewChild } from '@angular/core';
import { CompatibilityService } from '../../../services/compatibility/compatibility-service';
import { SelectionMode } from '../../../../objects/enums/selection-mode';
import { TextBoxComponent } from '../text-box/text-box-component';
import { VirtualPanelComponent } from '../../panels/virtual-panel/virtual-panel-component';
import { StringExtensions } from '../../../../objects/extensions/string-extensions';
import { KeyCodes } from '../../../../objects/key-codes';
import { ArrayExtensions } from '../../../../objects/extensions/array-extensions';
var ComboBoxComponent = /** @class */ (function () {
    function ComboBoxComponent(changeDetectorRef, viewContainerRef, CompatibilityService) {
        this.changeDetectorRef = changeDetectorRef;
        this.viewContainerRef = viewContainerRef;
        this.CompatibilityService = CompatibilityService;
        this.ComboBoxItemClass = "combo-box-item";
        this.ComboBoxPanelClass = "combo-box-panel-default";
        this.ComboBoxButtonClass = "button-icon-default";
        this.ItemHeight = 30;
        this.ShowRemoveItem = true;
        this.IsDropDownOpenChange = new EventEmitter();
        this.SelectionMode = SelectionMode.Single;
        this.ShowClearButton = true;
        this.SelectedItems = [];
        this.SelectedItemsChange = new EventEmitter();
        this.SelectedItemChange = new EventEmitter();
        this.TextChange = new EventEmitter();
        this.ComboBoxListItemSelectedClass = "combo-box-list-item-selected";
        this.ShowHighlight = true;
        this.DropDownWidth = "100%";
        if (this.CompatibilityService.IsLegacyBrowser)
            this.DropDownWidth = "";
        this.changeDetectorRef.detach();
        this.el = viewContainerRef.element.nativeElement;
        this.clickEvent = this.HandleClick.bind(this);
    }
    ComboBoxComponent.prototype.ngOnInit = function () {
        this.IsDropDownOpen = this.IsDropDownOpen || false;
        this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
        this.filterItemSource();
        var body = document.querySelector('body');
        body.addEventListener('click', this.clickEvent, false);
    };
    Object.defineProperty(ComboBoxComponent.prototype, "Text", {
        get: function () {
            return this.text;
        },
        set: function (value) {
            if (this.text != value) {
                this.text = value;
                this.TextChange.emit(this.text);
                this.changeDetectorRef.detectChanges();
            }
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ComboBoxComponent.prototype, "SelectedItem", {
        get: function () {
            return this.selectedItem;
        },
        set: function (value) {
            this.selectedItem = value;
            if (this.SelectionMode == SelectionMode.Single)
                this.SelectedItems.length = 0;
            if (this.selectedItem && this.SelectedItems.indexOf(this.selectedItem) == -1)
                this.SelectedItems.push(this.selectedItem);
            if (this.SelectionMode == SelectionMode.Single)
                this.IsDropDownOpen = false;
            else
                this.SelectedItemsChange.emit(this.SelectedItems);
            this.Text = "";
            this.TextChange.emit(this.Text);
            this.filterItemSource();
            this.SelectedItemChange.emit(this.SelectedItem);
        },
        enumerable: true,
        configurable: true
    });
    ComboBoxComponent.prototype.SelectItem = function (item) {
        if (!this.SelectedItems)
            this.SelectedItems = [];
        if (this.SelectedItems.indexOf(item) == -1)
            this.SelectedItem = item;
        else {
            this.RemoveSelectedItem(item);
        }
        this.changeDetectorRef.detectChanges();
    };
    ComboBoxComponent.prototype.ngOnDestroy = function () {
        var body = document.querySelector('body');
        body.removeEventListener('click', this.clickEvent, false);
    };
    ComboBoxComponent.prototype.HandleClick = function (e) {
        if (!this.IsDropDownOpen || !e.target) {
            return;
        }
        ;
        if (this.el !== e.target && !this.el.contains(e.target)) {
            this.IsDropDownOpen = false;
            this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
            this.virtualPanel.ResetScroll();
            this.changeDetectorRef.detectChanges();
        }
    };
    Object.defineProperty(ComboBoxComponent.prototype, "AllSelected", {
        get: function () {
            var _this = this;
            if (this.SelectedItems && this.ItemsSource && this.ItemsSource.length > 1)
                return this.ItemsSource.every(function (r) { return _this.SelectedItems.includes(r); });
            return false;
        },
        enumerable: true,
        configurable: true
    });
    ComboBoxComponent.prototype.highlight = function () {
        if (this.filteredItemSource && this.filteredItemSource.length > 0) {
            this.HighlightedItem = this.filteredItemSource[0];
        }
    };
    ComboBoxComponent.prototype.filterItemSource = function () {
        var _this = this;
        if (this.Text) {
            var lowerCaseText = this.Text.toLowerCase();
            this.filteredItemSource = this.ItemsSource.filter(function (item) { return _this.getItemDisplay(item).toLowerCase().indexOf(lowerCaseText) != -1; });
        }
        else {
            this.filteredItemSource = this.ItemsSource;
        }
        this.highlight();
        this.changeDetectorRef.detectChanges();
    };
    ComboBoxComponent.prototype.OnClickClear = function () {
        this.IsDropDownOpen = false;
        this.Clear();
    };
    ComboBoxComponent.prototype.Clear = function () {
        this.SelectedItems.length = 0;
        this.SelectedItem = undefined;
        this.changeDetectorRef.detectChanges();
    };
    ComboBoxComponent.prototype.SelectAll = function () {
        this.SelectedItems = this.ItemsSource.slice();
        this.SelectedItemsChange.emit(this.SelectedItems);
        this.changeDetectorRef.detectChanges();
    };
    Object.defineProperty(ComboBoxComponent.prototype, "WatermarkDisplay", {
        get: function () {
            if (this.SelectedItem || (this.SelectedItems && this.SelectedItems.length > 0))
                return;
            return this.Watermark;
        },
        enumerable: true,
        configurable: true
    });
    ComboBoxComponent.prototype.RemoveSelectedItem = function (item) {
        var idx = this.SelectedItems.indexOf(item);
        if (idx < 0) {
            console.error("Could not find selected item to remove.");
            console.trace();
            return;
        }
        this.SelectedItems.splice(idx, 1);
        if (this.SelectedItem == item) {
            this.SelectedItem = undefined;
        }
        else {
            this.SelectedItemsChange.emit(this.SelectedItems);
        }
        this.textBox.Focus();
    };
    ComboBoxComponent.prototype.RemoveAllItem = function () {
        this.Clear();
    };
    ComboBoxComponent.prototype.onDropDownClick = function (event) {
        this.IsDropDownOpen = !this.IsDropDownOpen;
        this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
        if (this.IsDropDownOpen)
            this.textBox.Focus();
        this.changeDetectorRef.detectChanges();
    };
    ComboBoxComponent.prototype.onFocusChange = function (event) {
        this.IsDropDownOpen = true;
        this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
        this.filterItemSource();
    };
    ComboBoxComponent.prototype.onTextChange = function (value) {
        this.Text = value;
        this.TextChange.emit(this.Text);
        this.filterItemSource();
        if (StringExtensions.isNullOrEmpty(this.Text) == false) {
            this.IsDropDownOpen = true;
        }
    };
    ComboBoxComponent.prototype.onKeyDown = function (event) {
        if (event.keyCode == KeyCodes.DOWN) {
            var item = ArrayExtensions.findNextItem(this.filteredItemSource, this.HighlightedItem);
            if (item) {
                this.HighlightedItem = item;
                this.virtualPanel.ScrollToItem(item);
                this.changeDetectorRef.detectChanges();
            }
        }
        if (event.keyCode == KeyCodes.UP) {
            var item = ArrayExtensions.findPreviousItem(this.filteredItemSource, this.HighlightedItem);
            if (item) {
                this.HighlightedItem = item;
                this.virtualPanel.ScrollToItem(item);
                this.changeDetectorRef.detectChanges();
            }
        }
        if (event.keyCode == KeyCodes.BACKSPACE) {
            if (StringExtensions.isNullOrEmpty(this.Text)) {
                if (this.SelectedItems.length > 0)
                    this.RemoveSelectedItem(this.SelectedItems[this.SelectedItems.length - 1]);
            }
            if (this.SelectionMode == SelectionMode.Single)
                this.IsDropDownOpen = true;
        }
    };
    ComboBoxComponent.prototype.getItemDisplay = function (item) {
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
    ComboBoxComponent.prototype.onKeyUp = function (event) {
        if (event.keyCode == KeyCodes.ESCAPE) {
            this.IsDropDownOpen = false;
            this.IsDropDownOpenChange.emit(this.IsDropDownOpen);
            this.virtualPanel.ResetScroll();
            this.changeDetectorRef.detectChanges();
        }
        if (event.keyCode == KeyCodes.ENTER)
            this.SelectedItem = this.HighlightedItem;
    };
    Object.defineProperty(ComboBoxComponent.prototype, "ComboBoxModeClass", {
        get: function () {
            return this.SelectionMode == SelectionMode.Single ? "combo-box-panel-single" : "combo-box-panel-multiple";
        },
        enumerable: true,
        configurable: true
    });
    ComboBoxComponent.prototype.RaiseChange = function () {
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboBoxComponent.prototype, "Label", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxComponent.prototype, "ComboBoxItemClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxComponent.prototype, "ComboBoxPanelClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxComponent.prototype, "ComboBoxButtonClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], ComboBoxComponent.prototype, "ItemHeight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxComponent.prototype, "Width", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "IsBusy", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "IsDisabled", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "IsReadOnly", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "ShowRemoveItem", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "IsDropDownOpen", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ComboBoxComponent.prototype, "IsDropDownOpenChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], ComboBoxComponent.prototype, "SelectionMode", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "ShowClearButton", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], ComboBoxComponent.prototype, "ItemsSource", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], ComboBoxComponent.prototype, "SelectedItems", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboBoxComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ComboBoxComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ComboBoxComponent.prototype, "SelectedItemChange", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], ComboBoxComponent.prototype, "TextChange", void 0);
    __decorate([
        ViewChild(TextBoxComponent),
        __metadata("design:type", TextBoxComponent)
    ], ComboBoxComponent.prototype, "textBox", void 0);
    __decorate([
        Input(),
        __metadata("design:type", TemplateRef)
    ], ComboBoxComponent.prototype, "ItemTemplate", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxComponent.prototype, "ComboBoxListItemSelectedClass", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], ComboBoxComponent.prototype, "ShowHighlight", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboBoxComponent.prototype, "HighlightedItem", void 0);
    __decorate([
        ViewChild('virtualPanel'),
        __metadata("design:type", VirtualPanelComponent)
    ], ComboBoxComponent.prototype, "virtualPanel", void 0);
    __decorate([
        Input('Text'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], ComboBoxComponent.prototype, "Text", null);
    __decorate([
        Input('SelectedItem'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], ComboBoxComponent.prototype, "SelectedItem", null);
    ComboBoxComponent = __decorate([
        Component({
            selector: 'pm-combo-box',
            //templateUrl: './app/controls/components/boxes/combo-box/combo-box.html',
            templateUrl: './combo-box.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef,
            CompatibilityService])
    ], ComboBoxComponent);
    return ComboBoxComponent;
}());
export { ComboBoxComponent };
