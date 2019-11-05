var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, Component, Input } from '@angular/core';
import { ClipboardService } from '../../../services/clipboard/clipboard-service';
import { GridComponent } from '../grid-component';
import { ModalDialog } from '../../modal/modal-dialog';
import { Dictionary } from '../../../../objects/dictionary';
import { Column } from '../../../../objects/request/column';
import { ColumnType } from '../../../../objects/request/column-type';
import { GridLength } from '../../../../objects/request/grid-length';
var GridSettingsRowPanelComponent = /** @class */ (function () {
    function GridSettingsRowPanelComponent(changeDetectorRef, clipboard) {
        this.changeDetectorRef = changeDetectorRef;
        this.clipboard = clipboard;
        changeDetectorRef.detach();
    }
    GridSettingsRowPanelComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Grid']) {
            this.Data = JSON.stringify(this.Grid.ItemsSource, null, 4);
            this.changeDetectorRef.detectChanges();
        }
    };
    GridSettingsRowPanelComponent.prototype.OnAutoGenerate = function () {
        var items = JSON.parse(this.Data);
        if (items && items.length > 0) {
            var columns = new Dictionary();
            var item = items[0];
            for (var key in item) {
                if (key.startsWith('_')) {
                    continue;
                }
                var type;
                var column = new Column(key, key, key, ColumnType.String, new GridLength(100));
                columns.add(column.Key, column);
            }
            this.Grid.Columns = columns;
            this.Grid.RefreshGrid();
        }
    };
    GridSettingsRowPanelComponent.prototype.OnCopy = function () {
        this.clipboard.Copy(this.Data);
    };
    GridSettingsRowPanelComponent.prototype.OnSave = function () {
        this.Grid.ItemsSource = JSON.parse(this.Data);
    };
    GridSettingsRowPanelComponent.prototype.OnClose = function () {
        this.Dialog.Close(false);
    };
    __decorate([
        Input(),
        __metadata("design:type", GridComponent)
    ], GridSettingsRowPanelComponent.prototype, "Grid", void 0);
    __decorate([
        Input(),
        __metadata("design:type", ModalDialog)
    ], GridSettingsRowPanelComponent.prototype, "Dialog", void 0);
    GridSettingsRowPanelComponent = __decorate([
        Component({
            selector: 'pm-grid-settings-row-panel',
            //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-row-panel.html',
            templateUrl: './grid-settings-row-panel.html'
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef,
            ClipboardService])
    ], GridSettingsRowPanelComponent);
    return GridSettingsRowPanelComponent;
}());
export { GridSettingsRowPanelComponent };
