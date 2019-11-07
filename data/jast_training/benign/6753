var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { ChangeDetectorRef, ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { ClipboardService } from '../../../../controls/services/clipboard/clipboard-service';
import { ColumnType } from '../../../../objects/request/column-type';
import { ColumnAggregate } from '../../../../objects/request/column-aggregate';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
import { Column } from '../../../../objects/request/column';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Dictionary } from '../../../../objects/dictionary';
import { GridLength } from '../../../../objects/request/grid-length';
var GridSettingsColumnPanelComponent = /** @class */ (function () {
    function GridSettingsColumnPanelComponent(clipboard, changeDetectorRef) {
        this.clipboard = clipboard;
        this.changeDetectorRef = changeDetectorRef;
        this.SelectedTabIndex = 0;
        this.CurrentColumn = {};
        this.selectedItem = {};
        changeDetectorRef.detach();
        this.TypesItemsSource = [
            ColumnType.Boolean,
            ColumnType.Currency,
            ColumnType.Date,
            ColumnType.DateTime,
            ColumnType.Number,
            ColumnType.String
        ];
        this.AlignItemsSource = [
            "left",
            "center",
            "right"
        ];
        this.TrueFalseItemsSource = [
            "true",
            "false"
        ];
        this.AggregateItemsSource = [
            ColumnAggregate.Sum
        ];
    }
    Object.defineProperty(GridSettingsColumnPanelComponent.prototype, "Grid", {
        get: function () {
            return this.grid;
        },
        set: function (value) {
            this.grid = value;
            this.GridColumns = this.grid.Columns ? this.grid.Columns.Values : [];
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridSettingsColumnPanelComponent.prototype, "SelectedItem", {
        get: function () {
            return this.selectedItem;
        },
        set: function (value) {
            this.selectedItem = value;
            this.CurrentColumn = Object.assign({}, value);
            if (value) {
                this.HasSelection = true;
            }
            else {
                this.HasSelection = false;
            }
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridSettingsColumnPanelComponent.prototype, "Columns", {
        get: function () {
            return new Dictionary([
                { key: "Name", value: new Column("Name", "Name", "Name", ColumnType.String, new GridLength(140)) },
                { key: "Property", value: new Column("Property", "Property", "Property", ColumnType.String, new GridLength(100)) },
                { key: "Type", value: new Column("Type", "Type", "Type.Name", ColumnType.String, new GridLength(100)) },
                { key: "Width", value: new Column("Width", "Width", "Width.Value", ColumnType.String, new GridLength(100)) },
                { key: "IsHidden", value: new Column("IsHidden", "IsHidden", "IsHidden", ColumnType.String, new GridLength(80)) },
                { key: "HeaderTextAlign", value: new Column("HeaderTextAlign", "HeaderTextAlign", "HeaderTextAlign", ColumnType.String, new GridLength(100)) },
                { key: "CellTextAlign", value: new Column("CellTextAlign", "CellTextAlign", "CellTextAlign", ColumnType.String, new GridLength(100)) },
                { key: "CellTemplate", value: new Column("CellTemplate", "CellTemplate", "CellTemplate", ColumnType.String, new GridLength(100)) },
                { key: "HeaderTemplate", value: new Column("HeaderTemplate", "HeaderTemplate", "HeaderTemplate", ColumnType.String, new GridLength(100)) },
                { key: "Aggregate", value: new Column("Aggregate", "Aggregate", "Aggregate.Name", ColumnType.String, new GridLength(100)) },
                { key: "IsVisible", value: new Column("IsVisible", "IsVisible", "IsVisible", ColumnType.String, new GridLength(80)) },
            ]);
        },
        enumerable: true,
        configurable: true
    });
    GridSettingsColumnPanelComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Grid']) {
            var columns = "";
            if (this.Grid.Columns) {
                for (var i = 0; i < this.Grid.Columns.Values.length; i++) {
                    var column = this.Grid.Columns.Values[i];
                    var type = column.Type.constructor.name + "." + column.Type.Name;
                    columns += "{ key: \"" + column.Key + "\", value: new Column(\"" + column.Key + "\", \"" + column.Name + "\", \"" + column.Property + "\", " + type + " , new GridLength(" + column.Width.Value + ")) },\r\n";
                }
            }
            this.Code = columns;
            this.changeDetectorRef.detectChanges();
        }
    };
    GridSettingsColumnPanelComponent.prototype.OnCopy = function () {
        this.clipboard.Copy(this.Code);
    };
    GridSettingsColumnPanelComponent.prototype.OnSave = function () {
        if (this.SelectedTabIndex == 0) {
            var columns = this.GridColumns;
            var index = columns.indexOf(this.SelectedItem);
            columns[index] = this.CurrentColumn;
            var toDictionary = [];
            for (var i = 0; i < columns.length; i++) {
                var column = columns[i];
                toDictionary.push({ key: column.Key, value: column });
            }
            this.Grid.Columns = new Dictionary(toDictionary);
            this.GridColumns = columns.slice();
            this.changeDetectorRef.detectChanges();
        }
        else if (this.SelectedTabIndex == 1) {
            var items = JSON.parse(this.Code);
            // console.log('index - 1');
        }
        else {
            // console.log('index - else');
        }
    };
    GridSettingsColumnPanelComponent.prototype.OnClose = function () {
        this.Dialog.Close(false);
    };
    GridSettingsColumnPanelComponent.prototype.OnSelectedItemChange = function ($event, property) {
        if (this.CurrentColumn[property] != $event) {
            this.CurrentColumn[property] = $event;
            this.changeDetectorRef.detectChanges();
        }
    };
    GridSettingsColumnPanelComponent.prototype.OnAdd = function () {
        var columns = this.GridColumns;
        var column = new Column("Name", "Name", "Name", ColumnType.String, new GridLength(100));
        columns.push(column);
        this.GridColumns = columns.slice();
        this.SelectedItem = column;
        this.changeDetectorRef.detectChanges();
    };
    GridSettingsColumnPanelComponent.prototype.OnDelete = function () {
        var columns = this.GridColumns;
        var index = columns.indexOf(this.SelectedItem);
        columns.splice(index, 1);
        this.SelectedItem = columns[index];
        this.GridColumns = columns.slice();
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", ModalDialog)
    ], GridSettingsColumnPanelComponent.prototype, "Dialog", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridSettingsColumnPanelComponent.prototype, "CurrentColumn", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridSettingsColumnPanelComponent.prototype, "GridColumns", void 0);
    __decorate([
        Input('Grid'),
        __metadata("design:type", GridComponent),
        __metadata("design:paramtypes", [GridComponent])
    ], GridSettingsColumnPanelComponent.prototype, "Grid", null);
    __decorate([
        Input('SelectedItem'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], GridSettingsColumnPanelComponent.prototype, "SelectedItem", null);
    GridSettingsColumnPanelComponent = __decorate([
        Component({
            selector: 'pm-grid-settings-column-panel',
            //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-column-panel.html',
            templateUrl: './grid-settings-column-panel.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ClipboardService,
            ChangeDetectorRef])
    ], GridSettingsColumnPanelComponent);
    return GridSettingsColumnPanelComponent;
}());
export { GridSettingsColumnPanelComponent };
