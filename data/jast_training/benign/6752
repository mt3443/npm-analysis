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
import { ColumnGroup } from '../../../../objects/request/column-group';
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { Dictionary } from '../../../../objects/dictionary';
import { Column } from '../../../../objects/request/column';
import { GridLength } from '../../../../objects/request/grid-length';
var GridSettingsColumnGroupsPanelComponent = /** @class */ (function () {
    function GridSettingsColumnGroupsPanelComponent(clipboard, changeDetectorRef) {
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
        this.TrueFalseItemsSource = [
            "true",
            "false"
        ];
        this.AggregateItemsSource = [
            ColumnAggregate.Sum
        ];
    }
    Object.defineProperty(GridSettingsColumnGroupsPanelComponent.prototype, "Grid", {
        get: function () {
            return this.grid;
        },
        set: function (value) {
            this.grid = value;
            this.GridColumnGroups = this.grid.ColumnGroups ? this.grid.ColumnGroups.Values : [];
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(GridSettingsColumnGroupsPanelComponent.prototype, "SelectedItem", {
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
    Object.defineProperty(GridSettingsColumnGroupsPanelComponent.prototype, "Columns", {
        get: function () {
            return new Dictionary([
                { key: "Name", value: new Column("Name", "Name", "Name", ColumnType.String, new GridLength(140)) },
                { key: "Header", value: new Column("Header", "Header", "Header", ColumnType.String, new GridLength(100)) },
            ]);
        },
        enumerable: true,
        configurable: true
    });
    GridSettingsColumnGroupsPanelComponent.prototype.ngOnChanges = function (changes) {
        if (changes['Grid']) {
            var columnGroups = "";
            if (this.Grid.ColumnGroups) {
                for (var i = 0; i < this.Grid.ColumnGroups.Values.length; i++) {
                    var columnGroup = this.Grid.ColumnGroups.Values[i];
                    columnGroups += "{ key: \"" + columnGroup.Name + "\", value: new ColumnGroup(\"" + columnGroup.Name + "\", \"" + columnGroup.Header + ")) },\r\n";
                }
            }
            this.Code = columnGroups;
            this.changeDetectorRef.detectChanges();
        }
    };
    GridSettingsColumnGroupsPanelComponent.prototype.OnCopy = function () {
        this.clipboard.Copy(this.Code);
    };
    GridSettingsColumnGroupsPanelComponent.prototype.OnSave = function () {
        if (this.SelectedTabIndex == 0) {
            var columnGroups = this.GridColumnGroups;
            var index = columnGroups.indexOf(this.SelectedItem);
            columnGroups[index] = this.CurrentColumn;
            var toDictionary = [];
            for (var i = 0; i < columnGroups.length; i++) {
                var columnGroup = columnGroups[i];
                toDictionary.push({ key: columnGroup.Name, value: columnGroup });
            }
            this.Grid.ColumnGroups = new Dictionary(toDictionary);
            this.GridColumnGroups = columnGroups.slice();
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
    GridSettingsColumnGroupsPanelComponent.prototype.OnClose = function () {
        this.Dialog.Close(false);
    };
    GridSettingsColumnGroupsPanelComponent.prototype.OnSelectedItemChange = function ($event, property) {
        if (this.CurrentColumn[property] != $event) {
            this.CurrentColumn[property] = $event;
            this.changeDetectorRef.detectChanges();
        }
    };
    GridSettingsColumnGroupsPanelComponent.prototype.OnAdd = function () {
        var columnGroups = this.GridColumnGroups;
        var columnGroup = new ColumnGroup("Name", "Name");
        columnGroups.push(columnGroup);
        this.GridColumnGroups = columnGroups.slice();
        this.SelectedItem = columnGroup;
        this.changeDetectorRef.detectChanges();
    };
    GridSettingsColumnGroupsPanelComponent.prototype.OnDelete = function () {
        var columns = this.GridColumnGroups;
        var index = columns.indexOf(this.SelectedItem);
        columns.splice(index, 1);
        this.SelectedItem = columns[index];
        this.GridColumnGroups = columns.slice();
        this.changeDetectorRef.detectChanges();
    };
    __decorate([
        Input(),
        __metadata("design:type", ModalDialog)
    ], GridSettingsColumnGroupsPanelComponent.prototype, "Dialog", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Object)
    ], GridSettingsColumnGroupsPanelComponent.prototype, "CurrentColumn", void 0);
    __decorate([
        Input(),
        __metadata("design:type", Array)
    ], GridSettingsColumnGroupsPanelComponent.prototype, "GridColumnGroups", void 0);
    __decorate([
        Input('Grid'),
        __metadata("design:type", GridComponent),
        __metadata("design:paramtypes", [GridComponent])
    ], GridSettingsColumnGroupsPanelComponent.prototype, "Grid", null);
    __decorate([
        Input('SelectedItem'),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], GridSettingsColumnGroupsPanelComponent.prototype, "SelectedItem", null);
    GridSettingsColumnGroupsPanelComponent = __decorate([
        Component({
            selector: 'pm-grid-settings-column-groups-panel',
            //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-column-panel.html',
            templateUrl: './grid-settings-column-groups-panel.html',
            changeDetection: ChangeDetectionStrategy.OnPush
        }),
        __metadata("design:paramtypes", [ClipboardService,
            ChangeDetectorRef])
    ], GridSettingsColumnGroupsPanelComponent);
    return GridSettingsColumnGroupsPanelComponent;
}());
export { GridSettingsColumnGroupsPanelComponent };
