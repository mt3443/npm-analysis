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
import { GridComponent } from '../../../../controls/components/grid/grid-component';
import { ModalDialog } from '../../../../controls/components/modal/modal-dialog';
var GridSettingsGeneralPanelComponent = /** @class */ (function () {
    function GridSettingsGeneralPanelComponent(changeDetectorRef) {
        this.changeDetectorRef = changeDetectorRef;
        changeDetectorRef.detach();
    }
    Object.defineProperty(GridSettingsGeneralPanelComponent.prototype, "Grid", {
        get: function () {
            return this.grid;
        },
        set: function (value) {
            this.grid = value;
            this.CurrentGrid =
                {
                    "ColumnHeaderHeight": value.ColumnHeaderHeight,
                    "FrozenColumnCount": value.FrozenColumnCount,
                    "HierarchyColumnIndex": value.HierarchyColumnIndex,
                    "HierarchyColumnProperty": value.HierarchyColumnProperty,
                    "ShowFooter": value.ShowFooter,
                    "ShowRowNumbers": value.ShowRowNumbers,
                    "ShowColumnGroups": value.ShowColumnGroups,
                    "RowHeight": value.RowHeight
                };
            this.changeDetectorRef.detectChanges();
        },
        enumerable: true,
        configurable: true
    });
    GridSettingsGeneralPanelComponent.prototype.OnSave = function () {
        this.Grid.ColumnHeaderHeight = this.CurrentGrid.ColumnHeaderHeight;
        this.Grid.FrozenColumnCount = this.CurrentGrid.FrozenColumnCount;
        this.Grid.HierarchyColumnIndex = this.CurrentGrid.HierarchyColumnIndex;
        this.Grid.HierarchyColumnProperty = this.CurrentGrid.HierarchyColumnProperty;
        this.Grid.ShowFooter = this.CurrentGrid.ShowFooter;
        this.Grid.ShowColumnGroups = this.CurrentGrid.ShowColumnGroups;
        this.Grid.ShowRowNumbers = this.CurrentGrid.ShowRowNumbers;
        this.Grid.RowHeight = this.CurrentGrid.RowHeight;
        this.Grid.RaiseChange();
    };
    GridSettingsGeneralPanelComponent.prototype.OnClose = function () {
        this.Dialog.Close(false);
    };
    __decorate([
        Input('Grid'),
        __metadata("design:type", GridComponent),
        __metadata("design:paramtypes", [GridComponent])
    ], GridSettingsGeneralPanelComponent.prototype, "Grid", null);
    __decorate([
        Input(),
        __metadata("design:type", ModalDialog)
    ], GridSettingsGeneralPanelComponent.prototype, "Dialog", void 0);
    GridSettingsGeneralPanelComponent = __decorate([
        Component({
            selector: 'pm-grid-settings-general-panel',
            //templateUrl: './app/controls/components/grid/grid-settings/grid-settings-general-panel.html',
            templateUrl: './grid-settings-general-panel.html'
        }),
        __metadata("design:paramtypes", [ChangeDetectorRef])
    ], GridSettingsGeneralPanelComponent);
    return GridSettingsGeneralPanelComponent;
}());
export { GridSettingsGeneralPanelComponent };
