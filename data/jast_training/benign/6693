var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, forwardRef, EventEmitter, Input, Output, ViewContainerRef, ViewChild, IterableDiffers } from '@angular/core';
import { SelectionMode } from '../../../../objects/enums/selection-mode';
import { ComboBoxComponent } from '../combo-box/combo-box-component';
var CheckBoxComboBoxComponent = /** @class */ (function () {
    function CheckBoxComboBoxComponent(changeDetectorRef, viewContainerRef, _iterableDiffers) {
        this.changeDetectorRef = changeDetectorRef;
        this.viewContainerRef = viewContainerRef;
        this._iterableDiffers = _iterableDiffers;
        this.SelectionMode = SelectionMode.Multiple;
        this.SelectedItemsChange = new EventEmitter();
        this.iterableDiffer = this._iterableDiffers.find([]).create(null);
        this.changeDetectorRef.detach();
    }
    CheckBoxComboBoxComponent.prototype.ngOnInit = function () {
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxComboBoxComponent.prototype.ngOnChanges = function (changes) {
        if (changes['SelectedItems']) {
            this.comboBox.RaiseChange();
            this.SelectedItemsChange.emit(this.selectedItems);
            this.changeDetectorRef.detectChanges();
        }
    };
    CheckBoxComboBoxComponent.prototype.ngDoCheck = function () {
        var changes = this.iterableDiffer.diff(this.selectedItems);
        if (changes) {
            this.comboBox.RaiseChange();
            this.SelectedItemsChange.emit(this.selectedItems);
            this.changeDetectorRef.detectChanges();
        }
    };
    CheckBoxComboBoxComponent.prototype.OnUncheckAllClick = function () {
        this.comboBox.Clear();
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxComboBoxComponent.prototype.OnCheckAllClick = function () {
        this.comboBox.SelectAll();
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxComboBoxComponent.prototype.IsCheckedChange = function () {
        this.changeDetectorRef.detectChanges();
    };
    CheckBoxComboBoxComponent.prototype.IsChecked = function (item) {
        if (this.comboBox.SelectedItems && this.comboBox.SelectedItems.includes(item))
            return true;
        return false;
    };
    Object.defineProperty(CheckBoxComboBoxComponent.prototype, "ItemsSource", {
        get: function () {
            return this.itemsSource;
        },
        set: function (value) {
            this.itemsSource = value;
            this.comboBox.RaiseChange();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(CheckBoxComboBoxComponent.prototype, "SelectedItems", {
        get: function () {
            return this.selectedItems;
        },
        set: function (value) {
            this.selectedItems = value;
        },
        enumerable: true,
        configurable: true
    });
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], CheckBoxComboBoxComponent.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], CheckBoxComboBoxComponent.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Output(),
        __metadata("design:type", EventEmitter)
    ], CheckBoxComboBoxComponent.prototype, "SelectedItemsChange", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Boolean)
    ], CheckBoxComboBoxComponent.prototype, "IsDisabled", void 0);
    __decorate([
        ViewChild(forwardRef(function () { return ComboBoxComponent; })),
        __metadata("design:type", ComboBoxComponent)
    ], CheckBoxComboBoxComponent.prototype, "comboBox", void 0);
    __decorate([
        Input('ItemsSource'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], CheckBoxComboBoxComponent.prototype, "ItemsSource", null);
    __decorate([
        Input('SelectedItems'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], CheckBoxComboBoxComponent.prototype, "SelectedItems", null);
    CheckBoxComboBoxComponent = __decorate([
        Component({
            selector: 'pm-check-box-combo-box',
            //templateUrl: './app/controls/components/boxes/check-box-combo-box/check-box-combo-box.html',
            templateUrl: './check-box-combo-box.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ViewContainerRef,
            IterableDiffers])
    ], CheckBoxComboBoxComponent);
    return CheckBoxComboBoxComponent;
}());
export { CheckBoxComboBoxComponent };
