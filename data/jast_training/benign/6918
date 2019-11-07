var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { Input } from '@angular/core';
import { Property } from '../../../objects/request/properties/property';
import { SelectionMode } from '../../../objects/enums/selection-mode';
var ComboBoxProperty = /** @class */ (function (_super) {
    __extends(ComboBoxProperty, _super);
    function ComboBoxProperty(Label, item, displayMemberPath, watermark, selectionMode, items, itemsSource, orientation, isHidden, isDisabled) {
        var _this = _super.call(this, Label, orientation, isHidden, isDisabled) || this;
        _this.Label = Label;
        _this.IsComboBox = true;
        _this.Item = item;
        _this.Items = items || [];
        _this.ItemsSource = itemsSource;
        _this.Watermark = watermark;
        _this.DisplayMemberPath = displayMemberPath;
        _this.SelectionMode = selectionMode || SelectionMode.Single;
        return _this;
    }
    Object.defineProperty(ComboBoxProperty.prototype, "HasValue", {
        get: function () {
            if (this.SelectionMode == SelectionMode.Single && this.Item)
                return true;
            else if (this.SelectionMode == SelectionMode.Multiple && this.Items && this.Items.length > 0)
                return true;
            return false;
        },
        enumerable: true,
        configurable: true
    });
    ComboBoxProperty.prototype.Clear = function () {
        if (this.SelectionMode == SelectionMode.Single)
            this.Item = undefined;
        else if (this.SelectionMode == SelectionMode.Multiple && this.Items)
            this.Items.length = 0;
        this.Text = '';
    };
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboBoxProperty.prototype, "Item", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboBoxProperty.prototype, "Items", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], ComboBoxProperty.prototype, "ItemsSource", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxProperty.prototype, "Watermark", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxProperty.prototype, "DisplayMemberPath", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Number)
    ], ComboBoxProperty.prototype, "SelectionMode", void 0);
    __decorate([
        Input(),
        __metadata("design:type", String)
    ], ComboBoxProperty.prototype, "Text", void 0);
    return ComboBoxProperty;
}(Property));
export { ComboBoxProperty };
