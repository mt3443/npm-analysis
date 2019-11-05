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
import { Component } from '@angular/core';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { ControlsModule } from '../../../../controls/controls-module';
var GridSettingsDialog = /** @class */ (function (_super) {
    __extends(GridSettingsDialog, _super);
    function GridSettingsDialog() {
        var _this = _super.call(this) || this;
        _this.Header = 'Grid Settings';
        _this.ItemsSource =
            [
                { Name: 'General' },
                { Name: 'Columns' },
                { Name: 'ColumnGroups' },
                { Name: 'Rows' }
            ];
        _this.SelectedItem = _this.ItemsSource[0];
        return _this;
    }
    GridSettingsDialog_1 = GridSettingsDialog;
    Object.defineProperty(GridSettingsDialog.prototype, "Dialog", {
        get: function () {
            return this;
        },
        enumerable: true,
        configurable: true
    });
    GridSettingsDialog.Show = function (grid) {
        var dialog = ControlsModule.dialog.Show(GridSettingsDialog_1);
        dialog.Grid = grid;
    };
    GridSettingsDialog = GridSettingsDialog_1 = __decorate([
        Component({
            //templateUrl: './app/controls/components/grid/grid-settings-dialog.html',
            templateUrl: './grid-settings-dialog.html',
            styles: ["\n    :host {   \n      position: absolute;\n      height: 100%;\n      width: 100%;\n      top: 0px;\n      z-index: 1000;\n      pointer-events: none;\n    }\n  "]
        }),
        __metadata("design:paramtypes", [])
    ], GridSettingsDialog);
    return GridSettingsDialog;
    var GridSettingsDialog_1;
}(ModalDialog));
export { GridSettingsDialog };
